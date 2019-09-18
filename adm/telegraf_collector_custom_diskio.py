#!/usr/bin/env python

import os
import time
import psutil
from datetime import datetime
from telegraf_unixsocket_client import TelegrafUnixSocketClient
from mflog import getLogger

MFMODULE_RUNTIME_HOME = os.environ["MFMODULE_RUNTIME_HOME"]
SOCKET_PATH = os.path.join(MFMODULE_RUNTIME_HOME, "var", "telegraf.socket")
LOGGER = getLogger("telegraf_collector_custom_diskio")


old_read_bytes = None
old_write_bytes = None
old_dt = None
first = True
while True:
    LOGGER.debug("waiting 10s...")
    time.sleep(10)
    client = TelegrafUnixSocketClient(SOCKET_PATH)
    try:
        client.connect()
    except Exception:
        LOGGER.warning("can't connect to %s, wait 10s and try again...",
                       SOCKET_PATH)
        continue
    stats = psutil.disk_io_counters(perdisk=False)
    new_dt = datetime.now()
    new_read_bytes = stats.read_bytes
    new_write_bytes = stats.write_bytes
    if first:
        first = False
    else:
        delta = (new_dt - old_dt).total_seconds()
        read_bytes_per_second = (new_read_bytes - old_read_bytes) / delta
        write_bytes_per_second = (new_write_bytes - old_write_bytes) / delta
        if read_bytes_per_second >= 0 and write_bytes_per_second >= 0:
            data = {
                "read_bytes_per_second": read_bytes_per_second,
                "write_bytes_per_second": write_bytes_per_second
            }
            msg = client.send_measurement("custom_diskio", data)
            LOGGER.debug("sended msg: %s" % msg)
    old_dt = new_dt
    old_read_bytes = new_read_bytes
    old_write_bytes = new_write_bytes
    client.close()

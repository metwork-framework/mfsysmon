#!/usr/bin/env python

import os
import time
import psutil
from datetime import datetime
from telegraf_unixsocket_client import TelegrafUnixSocketClient
from mflog import getLogger

MFMODULE_RUNTIME_HOME = os.environ["MFMODULE_RUNTIME_HOME"]
SOCKET_PATH = os.path.join(MFMODULE_RUNTIME_HOME, "var", "telegraf.socket")
LOGGER = getLogger("telegraf_collector_custom_netio")


old_bytes_sent = None
old_bytes_recv = None
old_packets_sent = None
old_packets_recv = None
old_errin = None
old_errout = None
old_dropin = None
old_dropout = None
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
    stats = psutil.net_io_counters(pernic=False)
    new_dt = datetime.now()
    new_bytes_sent = stats.bytes_sent
    new_bytes_recv = stats.bytes_recv
    new_packets_sent = stats.packets_sent
    new_packets_recv = stats.packets_recv
    new_errin = stats.errin
    new_errout = stats.errout
    new_dropin = stats.dropin
    new_dropout = stats.dropout

    if first:
        first = False
    else:
        delta = (new_dt - old_dt).total_seconds()
        bytes_sent_per_second = (new_bytes_sent - old_bytes_sent) / delta
        bytes_recv_per_second = (new_bytes_recv - old_bytes_recv) / delta
        packets_sent_per_second = (new_packets_sent - old_packets_sent) / delta
        packets_recv_per_second = (new_packets_recv - old_packets_recv) / delta
        errin_per_second = (new_errin - old_errin) / delta
        errout_per_second = (new_errout - old_errout) / delta
        dropin_per_second = (new_dropin - old_dropin) / delta
        dropout_per_second = (new_dropout - old_dropout) / delta
        if bytes_sent_per_second >= 0 and bytes_recv_per_second >= 0 and \
                packets_sent_per_second >= 0 and packets_recv_per_second >= 0 \
                and errin_per_second >= 0 and errout_per_second >= 0 and \
                dropin_per_second >= 0 and dropout_per_second >= 0:
            dropin_percent = 100.0 * dropin_per_second \
                / packets_recv_per_second
            dropin_percent = min(max(0.0, dropin_percent), 100.0)
            dropout_percent = 100.0 * dropout_per_second \
                / packets_sent_per_second
            dropout_percent = min(max(0.0, dropout_percent), 100.0)
            data = {
                "bytes_sent_per_second": bytes_sent_per_second,
                "bytes_recv_per_second": bytes_recv_per_second,
                "packets_sent_per_second": packets_sent_per_second,
                "packets_recv_per_second": packets_recv_per_second,
                "errin_per_second": errin_per_second,
                "errout_per_second": errout_per_second,
                "dropin_per_second": dropin_per_second,
                "dropout_per_second": dropout_per_second,
                "dropin_percent": dropin_percent,
                "dropout_percent": dropout_percent
            }
            msg = client.send_measurement("custom_netio", data)
            LOGGER.debug("sended msg: %s" % msg)
    old_dt = new_dt
    old_bytes_sent = new_bytes_sent
    old_bytes_recv = new_bytes_recv
    old_packets_sent = new_packets_sent
    old_packets_recv = new_packets_recv
    old_errin = new_errin
    old_errout = new_errout
    old_dropin = new_dropin
    old_dropout = new_dropout
    client.close()

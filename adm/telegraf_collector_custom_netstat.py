#!/usr/bin/env python

# inspired from
# https://github.com/monitoring-tools/telegraf-plugins/tree/master/netstat

import os
import time
import psutil
from datetime import datetime
from telegraf_unixsocket_client import TelegrafUnixSocketClient
from mflog import getLogger
from mfutil import BashWrapper

MODULE_RUNTIME_HOME = os.environ["MODULE_RUNTIME_HOME"]
SOCKET_PATH = os.path.join(MODULE_RUNTIME_HOME, "var", "telegraf.socket")
LOGGER = getLogger("telegraf_collector_custom_netstat")
CMD = "ss -t -a -n"
STATES = {
    "ESTAB": "tcp_established",
    "SYN-SENT": "tcp_syn_sent",
    "SYN-RECV": "tcp_syn_recv",
    "FIN-WAIT-1": "tcp_fin_wait1",
    "FIN-WAIT-2": "tcp_fin_wait2",
    "TIME-WAIT": "tcp_time_wait",
    "UNCONN": "tcp_close",
    "CLOSE-WAIT": "tcp_close_wait",
    "LAST-ACK": "tcp_last_ack",
    "LISTEN": "tcp_listen",
    "CLOSING": "tcp_closing",
    "UNKNOWN": "tcp_none",
    "__TOTAL": "tcp_total"
}
STATES_VALUES = STATES.values()
STATES_KEYS = STATES.keys()


def get_stats():
    results = BashWrapper(CMD)
    if not results:
        LOGGER.warning("can't execute %s: %s" % (CMD, results))
        return None
    lines = results.stdout.splitlines()
    stats = {x: 0 for x in STATES_VALUES}
    for line in lines[1:]:
        tmp = line.strip().split()
        if tmp[0] not in STATES_KEYS:
            stats["tcp_none"] = stats.get("tcp_none") + 1
            continue
        stats[STATES[tmp[0]]] = stats.get(STATES[tmp[0]]) + 1
    stats["tcp_total"] = sum(stats.values())
    return stats


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
    stats = get_stats()
    if stats:
        msg = client.send_measurement("custom_netstat", stats)
        LOGGER.debug("sended msg: %s" % msg)
    client.close()

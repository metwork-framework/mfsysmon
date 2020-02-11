#!/usr/bin/env python

# inspired from
# https://github.com/monitoring-tools/telegraf-plugins/tree/master/netstat

import os
import time
from telegraf_unixsocket_client import TelegrafUnixSocketClient
from mflog import getLogger
from mfutil import BashWrapper

MFMODULE_RUNTIME_HOME = os.environ["MFMODULE_RUNTIME_HOME"]
SOCKET_PATH = os.path.join(MFMODULE_RUNTIME_HOME, "var", "telegraf.socket")
LOGGER = getLogger("telegraf_collector_custom_netstat")
CMD1 = "ss -t -a -n"
CMD2 = "nstat -az"
STATES1 = {
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
STATES1_VALUES = STATES1.values()
STATES1_KEYS = STATES1.keys()
STATES2 = {
    "TcpExtListenDrops": "syn_to_listen_dropped",
    "TcpExtListenOverflows": "listen_queue_overflowed",
    "TcpExtTCPBacklogDrop": "packets_dropped_tcp_backlog_full",
    "TcpExtPruneCalled": "packets_pruned_from_receive_queue",
    "TcpExtSyncookiesFailed": "invalid_syn_cookies_received"
}


def get_stats1():
    results = BashWrapper(CMD1)
    if not results:
        LOGGER.warning("can't execute %s: %s" % (CMD1, results))
        return None
    lines = results.stdout.splitlines()
    stats = {x: 0 for x in STATES1_VALUES}
    for line in lines[1:]:
        tmp = line.strip().split()
        if tmp[0] not in STATES1_KEYS:
            stats["tcp_none"] = stats.get("tcp_none") + 1
            continue
        stats[STATES1[tmp[0]]] = stats.get(STATES1[tmp[0]]) + 1
    stats["tcp_total"] = sum(stats.values())
    return stats


def get_stats2():
    stats = {}
    results = BashWrapper(CMD2)
    if not results:
        LOGGER.warning("can't execute %s: %s" % (CMD2, results))
        return None
    lines = results.stdout.splitlines()
    for line in lines:
        tmp = line.strip()
        for system_name, name in STATES2.items():
            if tmp.startswith(system_name):
                try:
                    stats[name] = int(tmp.split()[1])
                except Exception:
                    pass
                continue
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
    stats = get_stats1()
    if stats is None:
        stats = {}
    stats2 = get_stats2()
    if stats2 is not None:
        stats.update(stats2)
    if len(stats) > 0:
        msg = client.send_measurement("custom_netstat", stats)
        LOGGER.debug("sended msg: %s" % msg)
    client.close()

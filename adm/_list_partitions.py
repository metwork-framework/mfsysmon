#!/usr/bin/env python3

import os
import json
from mfutil import BashWrapper

# List partitions of the system (and not block devices)

# see https://github.com/sysstat/sysstat/issues/185

cmd = "cat /proc/diskstats |awk '{print $3;}'"
partitions = []
output = BashWrapper(cmd)
if output:
    for dev in output.stdout.split():
        if not os.path.islink("/sys/block/%s" % dev):
            partitions.append(dev)

print(json.dumps(partitions))

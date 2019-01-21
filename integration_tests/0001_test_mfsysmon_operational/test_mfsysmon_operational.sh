#!/bin/bash

# Test if mfsysmon.status is ok
mfsysmon.status
if test $? -ne 0; then
    echo "Test mfsysmon.status KO"
    exit 1
else
    echo "Test mfsysmon.status OK"
fi
exit 0

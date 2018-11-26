#!/bin/bash

# Test if mfsysmon.start/status/stop are ok
su --command="mfsysmon.start" - mfdata
if test $? -ne 0; then
    echo "Test mfsysmon.start KO"
    exit 1
else
    echo "Test mfsysmon.start OK"
fi
su --command="mfsysmon.status" - mfdata
if test $? -ne 0; then
    echo "Test mfsysmon.status KO"
    exit 1
else
    echo "Test mfsysmon.status OK"
fi
su --command="mfsysmon.stop" - mfdata
if test $? -ne 0; then
    echo "Test mfsysmon.stop KO"
    exit 1
else
    echo "Test mfsysmon.stop OK"
fi
exit 0

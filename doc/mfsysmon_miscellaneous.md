
# Miscellaneous

## Debugging telegraf

You can :index:`debug` metrics sent to :index:`telegraf` by dumping them into telegraf.log file. In order to do this, edit the Metwork module (MFDATA, MFSERV, ...)  `config/config.ini` file and, in the `[telegraf]` section, set the `debug` argument to 1:
```cfg
[telegraf]

# Default value is 0. If debug=1, all metrics are (also) dumped into telegraf.log file
debug=1
```

## Collecting external metrics

You may use MFSYSMON module to collect external/:index:`non-metwork metrics`. In order to do this, edit the Metwork module (MFDATA, MFSERV, ...)  `config/config.ini` file and, in the `[telegraf]` section, fill up the `external_service_address` argument:
```cfg
[telegraf]

# If you want to use mfsysmon telegraf as a collector for external
# (ie. non-metwork) metrics, you can use this to listen to a particular port
# in TCP or UDP
# null => no specific listening
# tcp4://:8094 => listen to TCP port 8094
# udp4://:8094 => listen to UDP port 8094
# see https://github.com/influxdata/telegraf/tree/master/plugins/inputs/socket_listener
# for details
external_service_address=tcp4://:8094

```

.. seealso::
    `telegraf socket listener service <https://github.com/influxdata/telegraf/tree/master/plugins/inputs/socket_listener>`_

<!--
Intentional comment to prevent m2r from generating bad rst statements when the file ends with a block .. xxx ::
-->
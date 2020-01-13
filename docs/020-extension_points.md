# Extension points

The **MFSYSMON** module does not support plugins.

But there are some extensions points if you want to add your own metrics.

Before going further, you have to know that the main component of **MFSYSMON** module is [telegraf](https://github.com/influxdata/telegraf). It collects and forwards all metrics.

## statsD

??? note "You do not know about statsD ?"
    If you don't know [statsD](https://github.com/statsd/statsd) software and concepts, here is
    a good [statsD introduction](https://thenewstack.io/collecting-metrics-using-statsd-a-standard-for-real-time-monitoring/).

We don't provide the original `statsD` software but the corresponding protocol is
activated on `telegraf` on **MFSYSMON**.

So you can fed this service on UDP port: `${MFSYSMON_TELEGRAF_STATSD_PORT}` (18129 by default)
with the following [protocol](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/statsd) (compatible with most `statsd` client libraries).

## external_service_address

In the **MFSYSMON** configuration, under `[telegraf]` group, you will find a configuration key: `external_service_address`.

It's set to `null` by default but if you change it with `tcp4://:8094` for example, the **MFSYSMON** `telegraf` will listen to this port for external metrics sent with [InfluxDB Line Protocol format](https://docs.influxdata.com/influxdb/v1.7/write_protocols/line_protocol_tutorial/).

## external_commands

In the **MFSYSMON** configuration, under `[telegraf]` group, you will find a configuration key: `external_commands`.

It's set to `null` by default but if you provide in it a coma separated list of command full paths, they will be executed through [telegraf exec plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/exec). So if your provided commands output some [InfluxDB Line           Protocol format](https://docs.influxdata.com/influxdb/v1.7/write_protocols/line_protocol_tutorial/) lines, there will be parsed as metrics and sent to **MFADMIN** module.

## debug

If you want to debug, set the key `debug` to `1` under `[telegraf]` group and restart the **MFSYSMON** service. All metrics will be dumped in `${MFMODULE_RUNTIME_HOME}/log/telegraf.log` log file.

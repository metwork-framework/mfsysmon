# Introduction to MFSYSMON


## What is mfsysmon?

MFSYSMON is a Metwork module which contains **tools and libraries** used to monitor the overall resources of the operating system on which Metwork is running.

.. index:: MFADMIN module,telegraf
## How it works?

MFSYSMON collects the following metrics:
- disk I/O statistics
- network information and I/O statistics

The retrieved metrics are sent to [telegraf server agent](https://www.influxdata.com/time-series-platform/telegraf/) through an unix socket (see [Metwork telegraf-unixsocket-python-client](https://github.com/metwork-framework/telegraf-unixsocket-python-client) for more details).

![image](./_images/overall_architecture.svg)

[Circus](https://circus.readthedocs.io/en/latest/) is a Python program in order to monitor and control processes and sockets.

[Telegraf](https://docs.influxdata.com/telegraf/) is a plugin-driven server agent for collecting and sending metrics and events from databases, systems, and IoT sensors.

`mflog2mfadmin` (based on [jsonlog2elasticsearch](https://github.com/metwork-framework/jsonlog2elasticsearch)) on is a daemon to send [mflog](https://github.com/metwork-framework/mflog) to elasticsearch.

Circus acts as a process watcher and runner. You may check the full `circus.ini` configuration file in the `/home/mfsysmon/tmp/config_auto/` directory. Check the [Circus architecture](https://circus.readthedocs.io/en/latest/design/architecture/)

:index:`Monitoring` and :index:`Dashboards` are available through :doc:`MFADMIN <mfadmin:mfadmin_monitoring_plugins>`.

.. seealso::
    | :doc:`MFADMIN Documentation <mfadmin:index>`
    | :doc:`mfadmin:mfadmin_monitoring_plugins`.

<!--
Intentional comment to prevent m2r from generating bad rst statements when the file ends with a block .. xxx ::
-->

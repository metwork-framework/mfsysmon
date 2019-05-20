# Introduction to MFSYSMON


## What is mfsysmon?

MFSYSMON is a Metwork module which contains **tools and libraries** used to monitor the overall resources of the operating system on which Metwork is running.

.. index:: MFADMIN module,telegraf
## How it works?

MFSYSMON collects the following metrics:
- disk I/O statistics
- network information and I/O statistics

The retrieved metrics are sent to [telegraf](https://www.influxdata.com/time-series-platform/telegraf/) through an unix socket (see [Metwork telegraf-unixsocket-python-client](https://github.com/metwork-framework/telegraf-unixsocket-python-client) for more details).

:index:`Dashboards` are available through :doc:`The MFADMIN module <mfadmin:index>`.

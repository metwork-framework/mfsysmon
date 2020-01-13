# What is it?

**MFSYSMON** is the **M**etwork **F**framework **SYS**tem **MON**intoring module.

It's a very small module which collect system metrics (CPU, RAM, disks, network...) of
the current machine and send them to a configured **MFADMIN** module through the network.
So, **MFSYSMON** is only a small agent, not a database or a monitoring dashboard.

By default, harvested metrics are sent to `localhost` (so, in this default case,
you should have a `MFADMIN` module running on the same host) but a very common use case
is to have several hosts with **MFSYSMON** which feed a single `MFADMIN` instance.

??? question "You want to feed a remote `MFADMIN` module (rather than a local one)?"
    You just have to change the `hostname` key in the `[admin]` configuration group,
    set the corresponding hostname (i.e., the one which hosts the `MFADMIN` module)
    and reload your `MFSYSMON` service.

!!! note
    The configured `MFADMIN` module fed by the current instance of `MFSYSMON`
    is shown at the end of the welcome banner when you log in as `mfsysmon` unix user
    (`su - mfsysmon` from `root` for example):

    ```
               __  __      ___          __        _
              |  \/  |    | \ \        / /       | |
              | \  / | ___| |\ \  /\  / /__  _ __| | __
              | |\/| |/ _ \ __\ \/  \/ / _ \| '__| |/ /
              | |  | |  __/ |_ \  /\  / (_) | |  |   <
              |_|  |_|\___|\__| \/  \/ \___/|_|  |_|\_\

     13:11:17 up 459 days,  1:32,  1 user,  load average: 0.10, 0.10, 0.10

    Sending metrics and logs to mfadmin module: (localhost, 127.0.0.1)
    ```

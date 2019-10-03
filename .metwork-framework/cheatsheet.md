# MetWork/mfsysmon cheatsheet

## `root` service commands

As `root` unix user:

| Command | Description |
| --- | --- |
| `service metwork start` | start all installed metwork services |
| `service metwork stop` | stop all installed metwork services |
| `service metwork status` | check all installed metwork services |

| `service metwork start mfsysmon` | start mfsysmon metwork services |
| `service metwork stop mfsysmon` | stop mfsysmon metwork services |
| `service metwork status mfsysmon` | check mfsysmon metwork services |


> Note: if you don't have `service` command on your Linux distribution, you can use `/etc/rc.d/init.d/metwork` instead of `service metwork`. For example: `/etc/rc.d/init.d/metwork start` instead of `service metwork start`. If your Linux distribution uses `systemd`component, you can also start metwork services with classic `systemctl` commands.


## root files or directories

| Path | Description |
| --- | --- |
| `/etc/metwork.config.d/mfsysmon/config.ini` | override the `mfdata` module configuration at system level |
| `/etc/metwork.config.d/mfsysmon/external_plugins/` | put some `.plugin` files here and they will be installed during `mfserv` service startup |




## module commands

As `mfsysmon` user:

| Command | Description |
| --- | --- |

| `mfsysmon.start` | start mfsysmon services |
| `mfsysmon.stop` | stop mfsysmon services |
| `mfsysmon.status` | check mfsysmon services |

| `layers`| FIXME |
| `components` | FIXME | 






FIXME:

- layer_load
- layer_unload

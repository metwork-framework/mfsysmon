# release_0.7 CHANGELOG

## v0.7.1 (2019-06-26)

### New Features

- mfsysmon first version on metwork-framework (from thefab version)
- add (only one) integration test
- add trigger mfsysmon-integration-tests-runner
- add telegraf monitoring
- better diskio configuration
- add a custom implementation of diskio plugin
- add a custom netstat telegraf collector
- add a custom netio telegraf collector
- add an entry-point for external systems to inject metrics
- Changes in management of layer dependencies and metapackage names
- execute integration tests directly from mfsysmon module
- use envtpl new option --reduce-multi-blank-lines
- replace MODULE* environment variables names by MFMODULE* (MODULE_HOME becomes MFMODULE_HOME and so on)
- build mfsysmon without mfcom (mfcom layers are now included in mfext)
- provide a way to execute external commands to collect external
- publish more statistics about network

### Bug Fixes

- typo in layer dependencies
- fix user used
- fix building issues with proxy
- send_mflog_logs config key was missing

## v0.7.0 (2019-05-24)

### New Features

- mfsysmon first version on metwork-framework (from thefab version)
- add (only one) integration test
- add trigger mfsysmon-integration-tests-runner
- add telegraf monitoring
- better diskio configuration
- add a custom implementation of diskio plugin
- add a custom netstat telegraf collector
- add a custom netio telegraf collector
- add an entry-point for external systems to inject metrics
- Changes in management of layer dependencies and metapackage names
- execute integration tests directly from mfsysmon module
- use envtpl new option --reduce-multi-blank-lines
- replace MODULE* environment variables names by MFMODULE* (MODULE_HOME becomes MFMODULE_HOME and so on)
- build mfsysmon without mfcom (mfcom layers are now included in mfext)
- provide a way to execute external commands to collect external
- publish more statistics about network

### Bug Fixes

- typo in layer dependencies
- fix user used
- fix building issues with proxy
- send_mflog_logs config key was missing



# release_0.8 CHANGELOG

## v0.8.0 (2019-08-14)

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

### Bug Fixes

- typo in layer dependencies
- fix user used
- fix building issues with proxy
- send_mflog_logs config key was missing



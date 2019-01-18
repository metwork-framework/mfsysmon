<a name="unreleased"></a>
## [Unreleased]

### Feat
- Changes in management of layer dependencies and metapackage names (only minimal and full) Associated with changes in mfext _metwork.spec, this reduces the number of layers installed by default when installing mfsysmon (only necessary mfext layers are installed) Metapackage metwork-mfsysmon-minimal only installs the necessary layers for mfsysmon to work properly Metapackage metwork-mfsysmon or metwork-mfbase-full installs all mfsysmon layers
- add a custom netio telegraf collector
- add an entry-point for external systems to inject metrics

<a name="v0.4.2"></a>
## [v0.4.2] - 2019-01-09

<a name="v0.4.1"></a>
## [v0.4.1] - 2019-01-08

<a name="v0.4.0"></a>
## [v0.4.0] - 2019-01-08
### Feat
- add (only one) integration test (mfsysmon.start/status/stop is working)
- add a custom implementation of diskio plugin
- add a custom netstat telegraf collector
- add telegraf monitoring
- add trigger mfsysmon-integration-tests-runner
- better diskio configuration
- mfsysmon first version on metwork-framework (from thefab version)

### Fix
- fix user used
- typo in layer dependencies


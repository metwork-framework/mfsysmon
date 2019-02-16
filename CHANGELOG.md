<a name="unreleased"></a>
## [Unreleased]

<a name="v0.5.6"></a>
## [v0.5.6] - 2019-02-09

<a name="v0.5.5"></a>
## [v0.5.5] - 2019-02-06

<a name="v0.5.4"></a>
## [v0.5.4] - 2019-01-31

<a name="v0.5.3"></a>
## [v0.5.3] - 2019-01-31

<a name="v0.5.2"></a>
## [v0.5.2] - 2019-01-31

<a name="v0.5.1"></a>
## [v0.5.1] - 2019-01-31

<a name="v0.5.0"></a>
## [v0.5.0] - 2019-01-29
### Feat
- Changes in management of layer dependencies and metapackage names (only minimal and full) Associated with changes in mfext _metwork.spec, this reduces the number of layers installed by default when installing mfsysmon (only necessary mfext layers are installed) Metapackage metwork-mfsysmon-minimal only installs the necessary layers for mfsysmon to work properly Metapackage metwork-mfsysmon or metwork-mfbase-full installs all mfsysmon layers
- add a custom netio telegraf collector
- add an entry-point for external systems to inject metrics
- execute integration tests directly from mfsysmon module and lauch them on a pull request on the module

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


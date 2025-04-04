#!/bin/bash

set -eu
set -x

cd /src


echo -e "[metwork_${DEP_BRANCH}]" >/etc/yum.repos.d/metwork.repo
echo -e "name=Metwork Continuous Integration Branch ${DEP_BRANCH}" >> /etc/yum.repos.d/metwork.repo
echo -e "baseurl=http://metwork-framework.org/pub/metwork/continuous_integration/rpms/${DEP_BRANCH}/${OS_VERSION}/" >> /etc/yum.repos.d/metwork.repo
echo -e "gpgcheck=0\n\enabled=1\n\metadata_expire=0\n" >>/etc/yum.repos.d/metwork.repo

    yum -y localinstall ./rpms/metwork-mfsysmon*.rpm
    yum -y install make

    su --command="mfsysmon.init" - mfsysmon
    su --command="mfsysmon.start" - mfsysmon
    su --command="mfsysmon.status" - mfsysmon
    if test -d "integration_tests"; then chown -R mfsysmon integration_tests; cd integration_tests; su --command="cd `pwd`; ./run_integration_tests.sh" - mfsysmon; cd ..; fi
    su --command="mfsysmon.stop" - mfsysmon


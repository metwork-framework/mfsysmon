MODULE=MFSYSMON
MODULE_LOWERCASE=mfsysmon

-include adm/root.mk
-include $(MFEXT_HOME)/share/main_root.mk

all:: directories
	echo "root@mfcom" >$(MFSYSMON_HOME)/.layerapi2_dependencies
	cd adm && $(MAKE)
	cd config && $(MAKE)

clean::
	cd config && $(MAKE) clean
	cd adm && $(MAKE) clean

directories:
	@for DIR in config bin; do mkdir -p $(MFSYSMON_HOME)/$$DIR; done

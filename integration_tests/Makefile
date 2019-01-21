test_list = $(shell ls */test*)

all:
	for tst in $(test_list) ; do \
		if test -x $$tst; then \
	        ./$$tst ; \
		fi ; \
	done

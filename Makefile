.ONESHELL: 

DEPENDENCIES = ./dependencies
SWAPFILE = /swapfile

# install dependencies 
install: setup-dependencies install-logr

setup-dependencies: 
	mkdir -p ${DEPENDENCIES} 
	touch ${DEPENDENCIES}/__init__.py

install-logr:
	# install logr-py
	git clone https://github.com/samueleishion/logr-py
	cp logr-py/logr.py ${DEPENDENCIES}/logr.py
	rm -rf ./logr-py

reinstall: 
	rm -rf ${DEPENDENCIES} 
	make install

# start 
start: 
	python3 main.py

# clean 
clean:
	rm -rf logs

.PHONY: all
PROJECTS=$(patsubst ./%,%,$(shell find . -mindepth 1 -maxdepth 1 -type d))

all: servers.yaml
	echo $(PROJECTS) | xargs -n1 ./generate.py

servers.txt:
	./generate_servers_txt.py > $@

servers.yaml: servers.txt
	./generate_servers_yaml.py

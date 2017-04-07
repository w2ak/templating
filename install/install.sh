#!/bin/sh
ask () {
    echo -n "(y/n)" $@
    read ok
    case "$ok" in
        y|Y) $@;;
        *) exit 1;;
    esac;
}

ask sudo apt-get update
ask sudo apt-get install python3 python3-pip
ask sudo pip3 install --upgrade pip setuptools
ask sudo pip3 install PyYAML Jinja2 matplotlib

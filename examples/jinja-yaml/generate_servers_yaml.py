#!/usr/bin/env python3
import sys,re,yaml

if __name__=='__main__':
    """
    Generates 'servers.yaml' from 'servers.txt'.
    """
    db={}
    with open('servers.txt','r+') as f:
        separator=re.compile(r'\s+')
        for line in f.readlines():
            fields=separator.split(line.strip())
            key=fields[0]
            if key not in db:
                db[key]={'name':key,'cards':list()}
            l=db[key]['cards']
            pci=fields[1]
            card=fields[2]
            mac=fields[3]
            l.append({ 'pci': pci, 'card': card, 'mac': mac })
    with open('servers.yaml','w+') as g:
        yaml.dump(db,stream=g,default_flow_style=False)

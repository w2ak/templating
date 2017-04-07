#!/usr/bin/env python3
import sys
import hashlib as h
import yaml as y

def main(filename):
    with open(filename, mode='r+') as f:
        obj = y.load(f)
        print(obj)
    print("----")
    print(y.dump(obj,default_flow_style=False))

if __name__=='__main__':
    if len(sys.argv)<2:
        sys.exit('Should give a filename.')
    main(sys.argv[1])
    sys.exit(0)

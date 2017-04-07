#!/usr/bin/env python3
cards=[(6,0),(10,0),(10,1),(10,2),(10,3),(96,0),(96,1)]
for srvnum in range(1,6):
    for a,b in cards:
        print("bigSrv-{0:d} 0000:{1:02x}:00.{2:d} enp{1:02x}s0f{2:d} 0{0:d}:de:ad:00:{1:02x}:{2:02x}".format(srvnum,a+srvnum,b))

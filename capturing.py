#!/usr/bin/python3.6
import pcapy
from struct import *
devs = pcapy.findalldevs()
print(devs)
cap = pcapy.open_live("eno1", 65536, 1, 0)
count = 1
while count:
    (header, payload) = cap.next()
    print(count)
    count = count+1
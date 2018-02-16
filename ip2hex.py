#!/usr/bin/python3.6
from sys import argv, exit
import re
#import exit
script, ip = argv
print (type(ip[0]))
# Divide the ip address into blocks each 0f 3 digits
regex=r"^\d{1,3}(?:\.\d{1,3}){3}$"
valid_ip=re.findall(regex, ip)
print(valid_ip)
if valid_ip:
    print(ip)
else:
    print("Not a vlid ip")
    exit(0)
octets=re.split('\.', ip)
binaries=[]:
for octs in octets:
    while octs !=0:
        binaries=
    
    print(octs)


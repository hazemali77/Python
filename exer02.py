#!usr/bin/python
import re
names =["Hazem", "Sarah", "Sirin", "Layan", "Hiba", "Iman", "AYMAN" "Iyad"]
#for name in names:
 #   print(name)


##for i in range(len(names)) :
   
   ##print("{}is element No.{}, in names list".format(names[i], i) )
    
    ##print(" This is element No. %d,  in names list %s" %(i, names[i]))
regex=r"^[aeiouAEIOU]"
for name in names :
    L=len(re.findall(regex, name)
        if L>0:
        print(name)

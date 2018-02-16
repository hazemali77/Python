#!/usr/bin/div python
import math 
import sys
a = float(sys.argv[1])
b=float(sys.argv[2])
N=int(sys.argv[3])
#f=str(sys.argv[4])
step=float((b-a)/N)
print (a, b, N)
data= []

n=0

while n <= N:
  
  data.append(a)
  print ("Hello\n", data, end='\n')
  a=a+step
  n += 1


y=0
out=[]
i=0
while i <= N :
  x=data[i]
  y=x**2
  out.append(y)
  i +=1
  
  #print ("Hello", out)
  
  
  def integrate(x, s):
    y=x*s
    return y,
  
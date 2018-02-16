coefficients =([1, 2, 3, 0, 5, 6, 0, 0 , 9])
poly1= ""
i =1
if coefficients[0] != 0:
  poly1= str(coefficients[0])
while  i < len(coefficients):

  if coefficients[i] != 0:
    poly1= poly1 + " + " + str(coefficients[i]) +("x^")+str(i)
    print(poly1)
    print (i)
    i += 1
  else:
    i += 1
      
    
print (poly1) 
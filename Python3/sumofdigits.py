while(True):
  try:
    number=int(input("Enter any number: "))
  except ValueError as e:
    print (e.args)
  else:
    break

sumofdigits=0
while(number!=0):
  sumofdigits+=number%10
  number=number//10
  if(sumofdigits > 9 and number==0):
    number=sumofdigits
    sumofdigits=0
  
print(sumofdigits)

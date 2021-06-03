st="abcd-efgh-xyz@ijkl-mnop-"

temp=""
lst1=[]

for var in st:
  if(var=="-" or var=="@"):
    lst1.append(temp)
    temp=""
  else:
    temp=temp + var

if(temp):
  lst1.append(temp)
  
print(lst1)

import re

#extract strings between quotes
inputstring = ' some strings are present in between "geeks" "for" "seeks" '
  
result=re.search('"([^"]*)"', inputstring)
print(result.group(1))

st="dbagath@gmail.com bagath.dhandapani@infinite.com bagath.singh@india.nec.com"

result=re.findall('(?<=@)\S+',st)

print(result)

result=re.finditer('\S+(?=@)',st)

for itr in result:
  print(itr.group())
  
st="list of email dbagath@gmail.com bagath.dhandapani@infinite.com bagath.singh@india.nec.com ids for sample"

regex=re.compile('([\w.-]+)@([\w.-]+)')
result=regex.findall(st)

print(result)

strs="""this is 9894075134 sample mobile number 7010318528 for
this regular this expression 
this is sample multiline text"""

match=re.sub(r'^this','**********',strs,2,flags=re.MULTILINE)

print(match)

strs="this is 101 sample 202 text for script"

result=re.split(r'\d\d\d',strs)

print(result)

import re

ipaddress="this is 255.30.30.10 sample ip address"

result=re.search(r'\b((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\b',ipaddress)

if(result):
  print(result.group())
else:
  print("None")
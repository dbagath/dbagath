from schema import Schema, And, Use, Optional, SchemaError

schema = Schema({'name': And(str, len),\
'age':  And(Use(int), lambda n: 18 <= n <= 99),\
Optional('gender'): And(str, Use(str.lower),\
lambda s: s in ('squid', 'kid'))})

data = {'name': 'asd', 'age': '28', 'gender': 'Squid'}
#{'name': 'Sam', 'age': '42'},\
#{'name': 'Sacha', 'age': '20', 'gender': 'KID'}
try:
  validated = schema.validate(data)
  print(validated)
except SchemaError as e:
  print(e)
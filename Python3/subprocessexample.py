import subprocess as sb

result=sb.run(['ls','-l'],stdout=sb.PIPE)
result=result.stdout.decode('utf-8')
print(result)

result=sb.getoutput('ls -l')
print(result)

p = sb.Popen(["ping", "-c 2", "demo.snmplabs.com"], stdout=sb.PIPE)

result=p.communicate()[0]

print(result.decode('utf-8'))


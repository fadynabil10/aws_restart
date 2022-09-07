import subprocess

mycommand1 = ["ls"]
mycommand2 = ["wc" , "-l"]

o1 = subprocess.Popen(mycommand1,stdout=subprocess.PIPE)
o2 = subprocess.Popen(mycommand2,stdin=o1.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]

output,error = o1.communicate()
print(type(output))
print(output)
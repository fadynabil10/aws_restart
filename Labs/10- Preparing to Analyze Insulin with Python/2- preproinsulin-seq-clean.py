# Clean Code
s = "ORIGIN 1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed 61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn //"

t = s.replace("ORIGIN 1", "")

z = t.replace("61", "")

y = z.replace(" ", "")

x = y.rstrip('/')

print (x)

# amino acids 1–24
lsinsulin = x[0:24]
print (lsinsulin)

#  amino acids 25–54
binsulin = x[24:54]
print (binsulin)

# amino acids 55–89
cinsulin = x[54:89]
print (cinsulin)

# amino acids 90–110
ainsulin = x[89:110]
print (ainsulin)
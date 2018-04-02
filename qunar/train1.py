import math
a,b=raw_input().split()
a=int(a)
b=int(b)
sum=0
for i in range(b):
    sum=sum+a
    a=math.sqrt(a)
print "%.2f" % sum
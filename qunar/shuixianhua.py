import math
a,b=raw_input().split()
a=int(a)
b=int(b)
class Solution:
    def Print(self, a,b):
        if (a < 100 or b > 999 or a > b):
            print "no"
        flag = False
        for i in range(a, b + 1):
            x = i // 100
            y = (i % 100) // 10
            z = ((i % 100) % 10)
            if (math.pow(x, 3) + math.pow(y, 3) + math.pow(z, 3) == i):
                print i
                flag = True
        if (not flag):
            print  "no"



if __name__ == '__main__':
  s=Solution()
  a=s.Print(100,200)

if (a < 100 or b > 999 or a > b):
    print "no"
flag = False
for i in range(a, b + 1):
    x = i // 100
    y = (i % 100) // 10
    z = ((i % 100) % 10)
    if (math.pow(x, 3) + math.pow(y, 3) + math.pow(z, 3) == i):
        print i
        flag = True
if (not flag):
    print  "no"



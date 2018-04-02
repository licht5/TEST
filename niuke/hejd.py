import  sys
a=input()
s=list(a)
print(s)
lenth=len(s)
max=pow(10,lenth)-1
# print(max)
for k in range(1,max):
    zanshi=s
    tem=list(str(k))
    for i in range(len(tem)):
        for j in range(len(zanshi)):
            if zanshi[j]==tem[i]:
                del zanshi[j]
            else:
                sys.stdout.write(k)
                break
#


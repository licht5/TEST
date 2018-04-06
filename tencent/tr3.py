#coding=utf-8
import sys
canshu=sys.stdin.readline().split()
n=int(canshu[0])
m=int(canshu[1])
jiqi=[]
renwu=[]
for i in range(n+m):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = map(int, line.split())
    if(i<n):
        jiqi.append(values)
    else:
        renwu.append(values)
s=0
num=0
if(n<=m):
    sorted(jiqi, cmp=None, key=lambda x: x[])
    for i in range(n):
        max_1=0
        index=0
        for j in range(m):
            if(jiqi[i][0]>=renwu[j][0] and jiqi[i][1]>=renwu[j][1]):
                tem=200*renwu[j][0]+3*renwu[j][1]
                if(tem>max_1):
                    max_1=tem
                    index=j
                    num=num+1

        s=s+max_1
        del renwu[index]
else:
    sorted(renwu, cmp=None, key=lambda x: x[])
    for i in range(m):
        max_2=0
        index=0
        for j in range(n):
            if(jiqi[i][0]>=renwu[j][0] and jiqi[i][1]>=renwu[j][1]):
                tem = 200 * renwu[j][0] + 3 * renwu[j][1]
                if (tem > max_2):
                    max_1 = tem
                    index = j
                    num = num + 1

            s = s + max_2
            del jiqi[index]



print  num,s






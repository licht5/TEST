# coding=utf-8
import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().split()
a=int(line[0])
anum=int(line[1])
b=int(line[2])
bnum=int(line[3])

if(n<a or n<b):
    print 0
if(n<a and n==b):
    print bnum
if(n==a and n<b):
    print anum
if(n>a and n>b):
    count=0
    for i in range(n):
        for j in range(n):
            if (a*i+b*j)==n:
                x1=1
                x11=1
                x2=1
                x22=1
                for a1 in range(i):
                    x1=x1*(anum-a1)
                    x11=x11*(a1+1)
                res1=x1/x11
                for b1 in range(j):
                    x2=x2*(bnum-b1)
                    x22=x22*(b1+1)
                res2=x2/x22
                count=count+res1*res2
    print  count

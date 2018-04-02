#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    ans=[]
    n = int(sys.stdin.readline().strip())
    for i in range(n+2):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        ans.append(values)
    s=[]
    while(ans[-1][1]<ans[-2][0]):
        ans[-1][1]=ans[-1][1]+60
        ans[-1][0]=ans[-1][0]-1
    s.append(ans[-1][0])

    s.append(ans[-1][1]-ans[-2][0])
    n=ans[0:n]
    for x in reversed(n):
        if(x[0]<s[0] or (x[0]==s[0] and x[1]<=s[1])):
            print(str(x[0])+" "+str(x[1]))
            break

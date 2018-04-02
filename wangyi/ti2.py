#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    ans=[]
    n = int(sys.stdin.readline().strip())
    for i in range(4):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        ans.append(values)
    zuobiao=[]
    for j in range(n):
        s=[]
        s.append(ans[0][j])
        s.append(ans[1][j])
        s.append(ans[2][j])
        s.append(ans[3][j])
    dic={}
    for x in range(n):
        for y in range(x+1,n):
            if (max(zuobiao[x][0],zuobiao[x][2])>min(zuobiao[y][0],zuobiao[y][2])
or max(zuobiao[x][1],zuobiao[x][3])>min(zuobiao[y][1],zuobiao[y][3]) ):
                if(x in dic):
                    pass
                else:
                    dic[x]=1
                if (y in dic):
                    pass
                else:
                    dic[y] = 1
    print(len(dic))
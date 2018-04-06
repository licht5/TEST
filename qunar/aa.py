def som(n,m,L):
    if(n==1):
        flag=1
        for k in range(len(L)):
            if m==L[k]:
                print "perfect"
                flag=0
                break
        if(flag==1):
            print "good"
    for i,itn in enumerate(L):
        if(itn<=m):
            L=L.pop(i)
            som(n-1,m-itn,L)





num,sits=raw_input().split()
eve=raw_input().split()
chu=[]
for i in eve:
    chu.append(int(i))
chu=sorted(chu)
num=int(num)
sits=int(sits)

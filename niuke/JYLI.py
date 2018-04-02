import  sys
s=input()
t=input()
slen=len(s)
tlen=len(t)
slist=list(s)
tlist=list(t)
cmp=slen-tlen+1
count=0
if (slen==0 and tlen==0):
    sys.stdout.write('0'+'\n' )
elif (slen>0 and tlen==0):
    sys.stdout.write(str(slen)+'\n' )
else:
    for i in range(cmp):
        temp = slist[i:i + tlen]
        for j in range(tlen):
            if temp[j] != tlist[j]:
                count += 1
    sys.stdout.write(str(count)+'\n')
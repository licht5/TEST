n=input()
ni=n[-1: :-1]
s=""
for i in range(len(n)):
    s=s+str(int(n[i])+int(ni[i]))
print(s)



def com(a,b):
    tot=0
    for i in range(len(a)):
        if (a[i]!=b[i]):
            tot+=1
    if(tot<=1):
        return True
    else:
        return False
def find(a,b,L,c):
    if(c<100):
        if (com(a, b)):
            return c
        else:
            for k in L:
                if com(k, b):
                    return find(a, k, L, c + 1)
                else:
                    continue
    else:
        return 0




word="hot"
word_ni="toh"
word_list=["doh","got", "dot" ,"god", "tod", "dog", "lot", "log"]
print find(word,word_ni,word_list,1)

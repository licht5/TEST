
def get_formed_function(first,last):
    full_name=first+" "+last
    return full_name.title()

def get_line_len(k):
    if k<2:
        return  0
    if k==2:
        return 1
    if k==3:
        return 2
    result=[0,1,2,3]
    max=0
    for i in range(4,k+1):
        max=0
        for j in range(1,int(i/2)+1):
            res=result[j]*result[i-j]
            if res>max:
                max=res
        result.append(max)

    max=result[k]
    return max


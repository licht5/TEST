import sys


def list2str(li):
    while li[0] == 0:
        del li[0]
    res = ''
    for i in li:
        res += str(i)
    return res


def multi(stra, strb):
    aa = list(stra)
    bb = list(strb)
    drugelen=0
    if (aa[0]=="-"):
        aa=aa[1:]
        drugelen+=1
    if (bb[0] == "-"):
        bb = bb[1:]
        drugelen += 1
    if (aa[0]=="+"):
        aa=aa[1:]
    if (bb[0] == "+"):
        bb = bb[1:]
    lena = len(stra)
    lenb = len(strb)
    result = [0 for i in range(lena + lenb)]
    for i in range(lena):
        for j in range(lenb):
            result[lena - i - 1 + lenb - j - 1] += int(aa[i]) * int(bb[j])
    for i in range(len(result) - 1):
        if result[i] >= 10:
            result[i + 1] += result[i] // 10
            result[i] = result[i] % 10
    if (drugelen%2==0):
        print (list2str(result[::-1]))
    else:
        print (list2str(result[::-1]))
a=input()
b=raw_input()
result=multi(a,b)
print(result)

# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print('请输入两个大数')
#         exit()
#     a = sys.argv[1]
#     b = sys.argv[2]
#     res = multi(a, b)
#     print('multi', res)
#     print(int(a) * int(b))



    # import math
# a=input()
# num1,num2=a.split(" ")
# # a=int(math.fabs(a))
# # b=int(math.fabs(b))
# # print a,b
# d=[]
# for i in num2:
#     c=[]
#     for j in num1:
#         c.append(int(i)*int(j))
#     d.append(c)
# big=[]
#
# for i in range(len(num1)+len(num2)-1):
#     for
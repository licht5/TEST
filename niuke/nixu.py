class Solution:
    def InversePairs(self, data):
        # write code here
        num=0
        for i in range(len(data)):
            for j in range(i+1,len(data)):
                if data[i]>data[j]:
                    num+=1
        return num
if __name__ == '__main__':
    s=Solution()
    a=s.InversePairs([1,2,3,4,5,6,7,0])
    print(a)
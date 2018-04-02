class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        l = []
        for i in range(1,tsum):
            su = 0
            d = []
            for j in range(i, tsum):
                if (su < tsum):
                    d.append(j)
                    su = su + j
                    if (su == tsum):
                        l.append(d)
                        break
                    if(su>tsum):
                        break


        return l
if __name__ == '__main__':
  s=Solution()
  a=s.FindContinuousSequence(3)
  print(a)
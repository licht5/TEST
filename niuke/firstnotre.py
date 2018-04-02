class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        d={}
        for i in s:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for j in range(len(s)-1):
            if d[s[j]]==1:
                return j
if __name__ == '__main__':
  s=Solution()
  a=s.FirstNotRepeatingChar("google")
  print(a)
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        d=[]
        if(pRoot==None):
            return d
        if(pRoot!=None and pRoot.left==None and pRoot.right==None):
            c=[]
            c.append(pRoot.val)
            d.append(c)
            return d
        a=[]
        a.append(pRoot)
        d.append(a)
        i=0
        while(d[i]!=None):
            c=[]
            for k in d[i]:
                if k.left!=None :
                    c.append(k.left)
                if k.right!=None :
                    c.append(k.right)
            if(len(c)>0):
                d.append(c)
                i=i+1
            else:
                break
        l=[]
        for item in  d:
            f=[]
            for p in item:
                f.append(p.val)
            l.append(f)
        return l
if __name__ == '__main__':
  s=Solution()
  a0=TreeNode(0)
  a1 = TreeNode(1)
  a2 = TreeNode(2)
  # a4 = TreeNode(4)
  # a5 = TreeNode(5)
  # a6 = TreeNode(6)
  # a7 = TreeNode(7)
  a0.left=a1
  a0.right=a2
  # a1.left = a4
  # a1.right = a5
  # a2.left = a6
  # a2.right = a7
  a=s.Print(a0)
  print(a)
class node:
    '''
    data:节点保存的数据
    _next:保存下一个节点对象  
    '''
    def __init__(self,data,pnext=None):
        self.data=data
        self.__next=pnext
    def __repr__(self):
        '''
        用来定义node字符输出
        :return: 输出data
        '''
        return str(self.data)
    def isEmpty(self):
        return (self.length==0)

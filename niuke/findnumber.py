# -*- coding:utf-8 -*-

def find(self):
    while True:
        stringlist = input()
        maxLenth, maxStr, Len, Str = 0, [], 0, ""
        for i, v in enumerate(stringlist):
            if (v.isdigit()):
                Len += 1
                Str += v
                if Len > maxLenth:
                    maxLenth = Len
                    maxStr = [Str]
                elif Len == maxLenth:
                    maxStr.append(Str)
            else:
                Len = 0
                Str = ""
        print("".join(maxStr) + "," + str(maxLenth))


find()

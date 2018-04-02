#!/bin/python
import sys
import os




def calculate(M, strs):
    d={}
    for i in range(M):
        lenth=len(list(strs[i]))
        for j in range(lenth):
            tem = strs[i][j]
            if j%2==0 and j+1<lenth:
                if tem in d:
                    d[tem].append(strs[i][j+2])
                    d[tem].append(strs[i][j+1])
                else:
                    yu=[]
                    yu.append(strs[i][j+2])
                    yu.append(strs[i][j+1])
                    d[tem]=yu
    newhu=[]
    for i in d:
        max = 0
        tem=i
        while(tem):
            if d[tem][2]:
                max = max + int(d[tem][2])
                tem=d[tem][1]


    return max









_M = int(raw_input())

_strs_cnt = _M
_strs_i = 0
_strs = []
while _strs_i < _strs_cnt:
    try:
        _strs_item = raw_input()
    except:
        _strs_item = None
    _strs.append(_strs_item)
    _strs_i += 1

res = calculate(_M, _strs)

print str(res) + "\n"
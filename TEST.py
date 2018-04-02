# import numpy as np
# import matplotlib.pyplot as plt
# import os
# # x = [1, 2, 3, 4, 5]
# #
# # y = [1, 4, 9, 16, 25]
# # plt.plot(x, y,'or')
# # plt.show()

# # fields = [1,2,3]
# # total=0;
# # for field in fields:
# #     total += int(field)
# # print total

# # f = open('data.txt', 'w')
# # f.write('1 2 3 4\n')
# # f.write('2 3 4 5\n')
# # f.close()

# # f=open('data.txt')
# # data=[]
# # for line in f:
# #     data.append([int(filed) for filed in line.split()])
# # f.close()
# # for row in data:
# #     print row
# #
# # os.remove('data.txt')
# url = 'http://ichart.finance.yahoo.com/table.csv?s=GE&d=10&e=5&f=2013&g=d&a=0&b=2&c=1962&ignore=.csv'
# import urllib2
# ge_csv = urllib2.urlopen(url)
# data = []
# for line in ge_csv:
#     data.append(line.split(','))
# data[:4]

name=raw_input("what is your name ?")
print "hello "+ name


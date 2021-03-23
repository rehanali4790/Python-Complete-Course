import numpy as np
# lis = ["2", "3", "4"]
#
# lis = list(map(int,lis))
# # for item in range(len(lis)):
# #     lis[item] = int(lis[item])
#
# lis[2] = lis[2] + 3
# print(lis[2])
# data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
# mean_ = np.mean(data)
# std_ = np.std(data)
# higher_r = mean_ + std_
# lower_r = mean_ - std_
# def with_in_r(a):
#     if a < higher_r and a > lower_r:
#         return a
# data = list(map(with_in_r, data))
# print(len(data))
# for i in range(int(lower_r),int(higher_r)):
#     if i in data:
# lis = [1,2,3,4,5,6,7,8,9]

# def sq(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func = [sq,cube]
# for i in range(5):
#     value = list(map(lambda x:x(i),func))
#     print(value)
# import math
# players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
#
# mean_ = sum(players)/len(players)
#
# def var(a):
#     return (a-mean_)**2
#
#
# varience_ = list(map(var,players))
# varience_ = sum(varience_)
# varience_ = (varience_)/len(players)
# std_ = math.sqrt(varience_)
#
# higher_r = mean_ + std_
# lower_r = mean_ - std_
#
#
# def with_in_r(a):
#     return a > lower_r and a < higher_r
# with_in_r_ = list(filter(with_in_r,players))
# print(len(with_in_r_))

from functools import reduce

list = [1,2,3,4,5]
num = reduce(lambda x,y:x*y,list)
print(num)



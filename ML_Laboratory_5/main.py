

# #1
# d1 = {0:10,1:20}
# d2 = {2:'barbi',3:'barbare'}
# d1.update(d2)
# print(d1)
#
# #2
# dic1 = {1:10,2:20}
# dic2 = {3:30,4:40}
# dic3 = {5:50,6:60}
# dic4 = {**dic1,**dic2,**dic3}
# print(dic4)
#
# #3
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for key in d.keys():
#     if key == 2:
#         print("barbi")
#
# #4
# d = {'x': 10, 'y': 20, 'z': 30}
# for k,v in d.items():
#     print(k,'->',v)
# #5
# d = {}
# for key in  range(10):
#     d[key] = key*key
# print(d)

# -- #6
# import random

# t = open('email.txt','r')
# t2 = t.read()
# print(t2)
# d = {k: random.randint(1,31) for k in t2}
# print(d)


# - - #7
# s1 = [0,1,2,3,4]
# k = 0
# for i in range(3,6):
#     k = i*100
#     s1.append(k)
#
# print(*s1, sep = "\n")
# print('len :',len(s1))

#--#8
# set1= {'green', 'blue' }
# set2 = {'blue', 'yellow'}
#
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))

# #9
# set1 = {12,23,2434,3434,3,56,4322}
# print(max(set1))
# print(min(set1))


# #10
# t = tuple(pow(k,3) for k in range(1,100)  if k%5 == 0)
# print(t)
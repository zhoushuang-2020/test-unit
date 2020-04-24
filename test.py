#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# import time
# # n=int(input('请输入一个整数：'))
# # a=0
# # b=1
# # start = time.time()
# # def F(n,a,b):
# #     if n==0:
# #         return a
# #     return F(n-1,b,a+b)
# # print(F(n,a,b))
# # end=time.time()
# # print("运行时间：%.2f秒"%(end-start))
# import sys
# list =[1,2,3,4]
# it=iter(list)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()
# for x in it:
#     print(x,end="  ")
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
#
# printme(str="菜鸟教程")
#
# def p1(list1):
#     print(list1)
#     return

# p1(list1=[1,1,2,2])
#
# def p2(arg1,*var):
#     print("输出：")
#     print(arg1)
#     for v in var:
#         print(v)
#     return
# p2(10)
# p2(70,60,50)
#
# sum = lambda arg1,arg2:arg1+arg2
# print("相加后的值为：",sum(10,20))
# print("相加后的值为：",sum(50,20))
def sum(arg1,arg2):
    total=arg1+arg2
    print("函数内：",total)
    return total

#调用sum函数
total=sum(20,20)
print("函数外：",total)

a=[1,2,3,4,5]
a.append(1)
print(a)
b=[9,0]
a.extend(b)
print(a)
print(a.count(1))
a.insert(0,22)
print("插入后的a：",a)
a.remove(22)#移除值为22的元素
print("删除后的a：",a)
a.pop(1)#删除下标的元素
print(a)
print(a.index(0))
# a.sort()#排序
# print(a)
a.reverse()#倒排
print(a)
b=a.copy()
print("b:",b)
b.pop()
print(b)
b.append(100)
print("插入了100：",b)
b.pop()
print("释放后：",b)

vec=[2,4,6]
print([3*x for x in vec])

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
aaa=[[row[i] for row in matrix] for i in range(4)]
print(aaa)

trans=[]
for i in range(4):
    trans.append([row[i] for row in matrix])
print(trans)

a=set('12313234')
print(a)
print('1' in a)
b=set('345873')
print(b)
print(a-b)#在a中但是不在b中
print(a|b)#在a或者b中
print(a&b)#在a并且也在b中
print(a^b)#a或b中，但不同时在a，b中

print("======")
# tel={'1':'zhou','2':'yang'}
# tel['3']='zhao'
# print(tel)
# del tel['1']
# print(tel)
# tel['2']='yanggeg'
# print(tel)
#
# print(list(tel.keys()))
# print(sorted(tel.keys()))#排序
# print('zhao' in tel)
knights={'11':'ss','22':'dd','33':'rr'}
for k,v in knights.items():
    print("k=",k,"v=",v)

for i,n in enumerate(['tic','tac','toe']):
    print(i,n)
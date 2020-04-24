#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multi(a,b):
    return a*b

def divide(a,b):
    return a/b

if __name__=='__main__':
    print("和：",add(2,3))
    print("差：",minus(4,2))
    print("积：", multi(4, 2))
    print('商：',divide(4,2))
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests

def login():
    url = 'http://218.17.39.34:7909/AuthService/oauth/token'
    headers = {'Authorization': 'Basic TUFOQUdFUjoxMjM0NTY='}
    data = {'username': 'zhou', 'password': '123456', 'grant_type': 'password'}
    res = requests.post(url=url, headers=headers, data=data)
    print(res.status_code)
    print(res.text)

if __name__=='__main__':
    print(login())
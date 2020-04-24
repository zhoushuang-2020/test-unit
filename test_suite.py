#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner
import test_login


if __name__=='__main__':
    suite = unittest.TestSuite()

    #tests=[TestMathFunc('test_add'),TestMathFunc('test_minus'),TestMathFunc('test_multi'),TestMathFunc('test_divide')]
    tests=[test_login.MyTestCase('test_login'),test_login.MyTestCase('test_login_error')]
    suite.addTests(tests)


    with open('HTMLReport.html','w', encoding='utf-8') as f:
        runner = HTMLTestRunner(stream=f,verbosity=2,title='Test_HTMLReport',description='登录接口的测试报告')
        runner.run(suite)



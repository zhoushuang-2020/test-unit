#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver =webdriver.Chrome()

driver.maximize_window()
time.sleep(1)

driver.get("http://218.17.39.34:7909/")
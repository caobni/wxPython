# -*- coding: utf-8 -*-
__author__ = 'Melissa'
"""
Module: compile
Author: Melissa
Created: 2014/8/22 15:16
Purpose:  
"""

import py_compile
import os
import re

print os.getcwd()
print re.escape(os.getcwd())
py_compile.compile(r'D:\Users\DayJob.py')
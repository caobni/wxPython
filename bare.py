# -*- coding: utf-8 -*-
__author__ = 'Melissa'
"""
Module: bare.py
Author: Melissa
Created: 2014/8/21 13:01
Purpose:  
"""

import wx #1

class App(wx.App):#2

    def OnInit(self): #3
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True

app = App() #4
app.MainLoop() #5
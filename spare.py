# -*- coding: utf-8 -*-
__author__ = 'Melissa'
"""
Module: spare
Author: Melissa
Created: 2014/8/21 14:44
Purpose:  
"""

import wx

class Frame(wx.Frame):   #3
    pass

class App(wx.App):

    def OnInit(self):
        self.frame = Frame(parent=None, title='Spare')   #4
        self.frame.Show()
        self.SetTopWindow(self.frame)   #5
        return True

if __name__ == '__main__':   #6
    app = App()
    app.MainLoop()
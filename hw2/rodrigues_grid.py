# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 09:41:55 2014

@author: abigail
"""
dimensions = 4

def rows():
    r1 = '+ - - - - '*dimensions
    r2 = '|         |'
    r3 = '         |'*(dimensions-1)+'\n'
    one_grid = r1 + '+' + '\n' + (r2 +r3)*4
    final = '+ - - - - '*dimensions + '+'
    print one_grid*dimensions+final
  
rows()
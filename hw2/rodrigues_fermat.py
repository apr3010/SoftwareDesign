# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 20:08:52 2014

@author: abigail
"""

def check_fermat(a,b,c,n):
    left_side = (a^n) + (b^n)
    right_side = (c^n)
    return left_side, right_side
    
left_side, right_side = check_fermat(1,2,3,4)
    
if left_side != right_side:
    print ('No, that does not work')
else:
    print ('Holy smokes! Fermat was wrong!')

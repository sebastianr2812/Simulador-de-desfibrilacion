# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:27:01 2020

@author: Sebastian
"""
dirRl = {1: [63],
      2: [66],
      3: [63],
      4: [81],
      5: [114]   }
def resL(v):
    if v>=1500:
        indr=1
    elif 1500>v>=900:
        indr=2
    elif 900>v>=400:
        indr=3
    elif 400>v>=300:
        indr=4
    elif 300>v>=100:
        indr=5
    
    return dirRl[indr]

# x=resL(2)
# print(x)
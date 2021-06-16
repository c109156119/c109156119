# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:26:41 2021

@author: User c109156119
"""

def main():
    dict1 = {"蘋果": "紅色", "香蕉": "黃色", "葡萄": "紫色", "藍莓": "藍色", "橘子": "橘色"}
    print("dict_keys(['蘋果','香蕉','葡萄','藍莓','橘子'])")
    key = input()
    print(key + "是" + dict1[key])
    
main()
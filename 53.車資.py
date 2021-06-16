# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:29:12 2021

@author: c109156119
取整數math
"""
import math
def main():
    km = float(input("請輸入路程公里數(km)："))
    money = s(km)
    print("所需車資為：", money)

def s(km):
    return int(75 + math.ceil(km-1.5)//0.25 * 5)

main()


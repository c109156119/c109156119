# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:29:12 2021

@author: c109156119
"""

def main():
    a = int(input("搭了幾次電梯: "))
    start = 1
    sum = 0
    for i in range(a):
        Val = int(input())
        sum += elevator(start, Val)
        start = Val
    print(sum, "元")
    
def elevator(start, end):
    return cmp(end - start) * 20 + cmp(start - end) * 10
    
def cmp(a):
    return a * int(a > 0)

main()

    
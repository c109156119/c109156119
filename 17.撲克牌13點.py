# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:25:50 2021

@author: User c109156119
"""
def main():
    list1 = input().split()
    dict1 = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, \
             "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
    sum1 = 0
    for i in list1: sum1 += dict1[i]
    print(sum1)
    
main()

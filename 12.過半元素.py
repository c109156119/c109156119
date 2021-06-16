# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:24:18 2021

@author: User c109156119
"""
def main():
    list1 = input("輸入一整數序列為: ").split()
    set1 = set(list1)
    if len(set1) > (len(list1)+1)//2: print("NO")
    else: 
        while len(list1) > 1: 
            for i in list(set(list1)): list1.remove(i)
        print(list1[0])
    
main()

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:23:38 2021

@author: User c109156119
"""

def main():
    n = int(input("輸入第一行正整數為: "))
    val = input("第二行中數列中的數字為:").split()
    if len(set(val)) == n: 
        print("每個數字剛好只出現1次")
    else:
        i = 1
        while True:
            for j in list(set(val)): val.remove(j)
            i += 1
            if len(val) == 1: 
                print("最大出現次數的數字為:" + val[0])
                print("出現次數為:" + str(i))
                break
            
main()
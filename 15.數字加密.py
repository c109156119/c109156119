# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:28:01 2021

@author: c109156119
"""
def main():
    list1=list(input("輸入一組4位數字為:"))
    for i in range(4):
        list1[i]=str((int(list1[i])+7)%10)
    list1[0],list1[2]=list1[2],list1[0]
    list1[1],list1[3]=list1[3],list1[1]
    print("輸出加密後的數字為:",(list1))
main()w
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 12:24:37 2021

@author: c109156119
"""
def main():
    n=int(input("請輸入n:"))
    k=int(input("請輸入k:"))
    print(cal(n,k))
def cal(a,b ,i=0):
    if a+i//b>0:return a +i//b+cal(a//b,b,i%b+a%b)
    else:return 0
main()
    

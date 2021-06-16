# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:08:04 2021

@author: c109156119
"""

def main():
    i=int(input("請出入十進位的正整數:"))
    print(i,"的三進位為",three(i))
def three(n):
    if n//3>0:return three(n//3)+str(n%3)
    else:return str(n)
main()
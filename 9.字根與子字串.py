# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:06:02 2021

@author: c109156119
"""
def main():
    str1=input("輸入s1為:")
    str2=input("輸入s2為:")
    if len(str2.replace(str1, ""))!=len(str2):print("YES")
main()
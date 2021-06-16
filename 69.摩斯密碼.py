# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:44:22 2021

@author: c109156119
"""

def main():
    a ={"-----":"0",
        ".----":"1",
           "..---":"2",
           "...--":"3",
    "....-":"4",}
    val = input().split()
    s=""
    for i in val: s+=a[i]
    print(s)
main()

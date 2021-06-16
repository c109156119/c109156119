# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:53:25 2021

@author: User
"""

def main():
    frienda=set(input("請輸入a的好友:").split())
    friendb=set(input("請輸入b的好友").split())
    print(len(frienda&friendb))
main()
        
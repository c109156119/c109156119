# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:53:15 2021

@author: c109156119
"""
    
def main():
    m=int(input("請輸入階層值M:"))
    N=0
    z=1
    while z<m:
        N+=1
        z*=N
    print("超過M為",m,"的最小階層N值為",N)
main()
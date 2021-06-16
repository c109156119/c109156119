# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:40:48 2021

@author: c109156119
"""

def main():
    ani = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", \
              "horse", "sheep", "monkey", "rooster", "dog", "pig"]
    Year = int(input())
    print(ani[(Year + 8) % 12])

main()
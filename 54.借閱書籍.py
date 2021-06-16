# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:10:05 2021

@author: c109156119
"""

def main():
    book= [["飢餓遊戲3", "解憂雜貨店", "怪獸與牠們的產地", "哈利波特6", "我的阿富汗摯友", "祈念之樹", "樓下的房客", "小王子"],
           ["房思琪的初戀樂園", "等一個人咖啡", "鬼滅之刃14", "神農嘗百草", "麥田捕手", "老人與海", "傲慢與偏見", "與神同行"]]
    Val=input("輸入我要的書籍:")
    if Val in book[0]: print("在書架A的第", book[0].index(Val)+1, "本")
    elif Val in book[1]: print("在書架B的第", book[1].index(Val)+1, "本")
    else: print("查無此書籍")
main()
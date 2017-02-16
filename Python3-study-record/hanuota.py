#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def hanuota(n,a,b,c):               #定义一个汉诺塔函数，接受参数n代表柱子A上的圆环个数         
    if n == 1:
        print(a,'-->',c)            #当n=1时，直接移动到C
    else:
        hanuota(n-1, a, c, b)       #抽象为一种方法：把A上的n-1个圆环先搬移到B上
        print(a,'-->',c)            #把A上余下的最后一个大圆环移动到C上
        hanuota(n-1, b, a, c)       #抽象方法： 把B上的n-1个圆环搬移到C上
hanuota(3, 'A', 'B', 'C')
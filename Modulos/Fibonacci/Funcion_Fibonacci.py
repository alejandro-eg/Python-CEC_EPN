# -*- coding: utf-8 -*-
def fib(n):
    a, b = 0,1
    while a <= n:
        print(a, end=' ')
        """c=a+b
         a=b
            b=c"""
        a, b = b, a+b
    print()
#fib(8)   
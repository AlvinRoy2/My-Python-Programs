# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 22:35:08 2022

@author: HP
"""
def gcd(m,n):
    for i in range(min(m,n),1,-1):
        if(m%i==0) and (n%i==0):
            return i
        else:
            continue

m=int(input("Enter a number:"))
n=int(input("Enter a number:"))
g=gcd(m,n)
print("The Gcd of",m,"and",n,"is",g)
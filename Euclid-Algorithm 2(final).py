# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 22:57:44 2022

@author: HP
"""

def gcd(m,n):
    if m<n:
        m,n=n,m
    if(m%n==0):
        return n
    else:
        return gcd(n,m%n)

m=int(input("Enter a number:"))
n=int(input("Enter a number:"))
g=gcd(m,n)
print("The gcd of",m,"and",n,"is",g)
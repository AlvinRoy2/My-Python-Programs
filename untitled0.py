# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 21:17:53 2022

@author: HP
"""

def gcd(m,n):
    #Assume m>n
    if(m<n):
        m,n=n,m
        
    if(m%n==0):
        return n
    else:
        diff=m-n
        # Diff>n(Possible)
        return gcd(max(n,diff),min(n,diff))
    
m=int(input("Enter a number:"))
n=int(input("Enter a number:"))
g=gcd(m,n)
print("The gcd of",m,"and",n,"is",g)
        
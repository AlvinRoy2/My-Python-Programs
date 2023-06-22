# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:28:37 2022

@author: HP
"""

str1=input("Enter the first string:")

str2=input("Enter the second string:")

if(sorted(str1)==sorted(str2)):
    print("These are Anagrams")
else:
    print("These are not Anagrams")
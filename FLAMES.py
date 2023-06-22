# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:16:35 2022

@author: HP
"""
import string

def remove_matching_letter(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l=list(l1+['*']+l2)
                return [l,True]
    l=list(l1+['*']+l2)
    return [l,False]

p1=input("Enter the First Person name:")
p1=p1.lower()
p1.replace(" ","")

p2=input("Enter the Second Person name:")
p2=p2.lower()
p2.replace(" ","")

l1=list(p1)
l2=list(p2)
proceed=True
while proceed:
    ret_list=remove_matching_letter(l1,l2)
    con_list=ret_list[0]
    proceed=con_list[1]
    star_index=con_list.index('*')
    l1=con_list[:star_index]
    l2=con_list[star_index+1:]
    
count1=len(l1)+len(l2)
print(count1)
result=['Friends','Love','Affection','Marriage','Enemy','Siblings']

while len(result)>1:
    split_index=(count1 % len(result))-1
    if split_index>=0:
        right=result[split_index+1:]
        left=result[:split_index]
        result=right+left
    else:
        result=result[:len(result)-1]

print(result[0])
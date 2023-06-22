# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:57:07 2022

@author: HP
"""

import turtle
turtle.bgcolor("black")
surat=turtle.Turtle()
from random import randint

width=5
height=7
 
dot=25 #distance of the dot
surat.penup()
list_colour=["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]

surat.setpos(-250,250)
 
def spiral(m,n):
    k=0
    l=0
    
    f=0
    col=randint(0,10)
    surat.color(list_colour[col])
    
    '''
    k=index of starting row
    l=index of starting column
    '''
    
    while(k<m and l<n):
        if(f==1):
            surat.right(90)
            
        #Printing the first row from the remaining rows
        
        for i in range(l,n):
            surat.dot()
            surat.forward(dot)
            #print(a[k][i],end=" ")
            
        k=k+1
        f=1
        
        surat.right(90)
        col=randint(0,10)
        surat.color(list_colour[col])
        
        #Printing the last column from the remaining columns
        for i in range(k,m):
            surat.dot()
            surat.forward(dot)
            #print(a[i][n-1],end=" ")
            
        n-=1
        
        surat.right(90)
        col=randint(0,10)
        surat.color(list_colour[col])
        
        if(k<m):
            #Printing the last row from the remaining rows
            for i in range(n-1,l-1,-1):
                surat.dot()
                surat.forward(dot)
                #print(a[m-1][i],end=" ")
            m-=1
        surat.right(90)
        col=randint(0,10)
        surat.color(list_colour[col])
        
        if(l<n):
            #Printing the first column from the remaining columns
            for i in range(m-1,k-1,-1):
                surat.dot()
                surat.forward(dot)
                #print(a[i][l],end=" ")
            l+=1
            
            
            
spiral(20,20)
        
        
        
        
        
        
        
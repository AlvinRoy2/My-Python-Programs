# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:20:32 2022

@author: HP
"""
def instructions():
    print('This is Rock Paper Scissors.Welcome to the Game.')
    print('\nIntroducing  the Instructions and Working:\n')
    print("1) Give your random number Enter the Random number in\n") 
    print("10 digits to increase the randomness of the variable\n")
    print("2) After giving the two random numbers\n")
    print("3) Enter the Secret bit code\n")
    print("4) The Given Bit Code's Remainder is got by dividing the bit code by 3\n")
    print("5) The Remainder is compared with the dictionary and checked")
    print("Have a Fun time playing the Game")
    return
        
def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(int(num1[bit1])%3)
    p2=int(int(num2[bit2])%3)
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player One Wins")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print("Player Two Wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissor"):
        print("Player Two Wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("Player One Wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
        print("Player Two Wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        print("Player One Wins")
player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Scissor',1:'Rock',2:'Paper'}
instructions()
while(1):
    num1=input("Player One,Enter your choice:")
    num2=input("Player Two,Enter your choice:")
    bit1=int(input("Player one,Enter the secretbit position and which is in the random number:"))
    bit2=int(input("Player Two,Enter the secretbit position and which is in the random number:"))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do You want to play or quit (y/n):")
    if(ch=='n'):
        break
    
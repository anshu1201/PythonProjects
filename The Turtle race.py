#!/usr/bin/env python
# coding: utf-8

# # Turtle

# In[6]:


#importing libraries
import turtle
import random


# In[7]:


#Setting Up the Turtles and Homes
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)


# In[3]:


player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)


# In[4]:


die = [1,2,3,4,5,6]


# In[5]:


#Developing the Game
for i in range(20):
    
    if player_one.pos() >= (300,100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (300,-100):
        print("Player Two Wins!")
        break
    else:
        player_one_turn = input("------Press 'Enter' to roll the die for player1---------- ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)
        player_two_turn = input("----------Press 'Enter' to roll the die for player2---------- ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)
              


# In[ ]:





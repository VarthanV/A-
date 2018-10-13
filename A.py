# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:38:46 2018

@author: Vishnu Varthan
Building a simple chat bot apologies if it is like a shit

"""
import random
import webbrowser
import time
import sys
import pyttsx3
from weather import Weather,Unit
from pyttsx3 import voice
small_data={"What is your name":["My name is A"," Vichu named  me A but you can name me whatever you like",
                                 "A is how people call me"],
            "Are you single":["Yes he wants me to be like him as he is single",
                                    "I'm not single I am surrounded by lines of code alwayss",
                                    "This  question is hypothetical","Being single is the  best"]
                                    
                                    
                                    
            }
positive_responses=['yes','yah','y','Y']
negative_responses=['nah','no','n','N']

engine=pyttsx3.init()
Voice=engine.getProperty('voices') # To bring the voice of my bae

def say(msg):
    print(msg)
    engine.say(msg)
    engine.runAndWait()

default="Sorry I couldn't understand you since I am trained a little bit only"
def ques():
            sayer="Ask me your questions I will answer myy best"
            say(sayer)
            ques=input()
            
            if ques in small_data:
                            c=random.choice(small_data[ques])
                        
                            
                            say(c)
                            
                            
        
                
            else:
                
                            say(default)
def weather():
    weather=Weather(unit=Unit.CELSIUS)
    location=weather.lookup_by_location('Coimbatore')
    say(location.condition)
def joke():
    a=(i in range (100))
    with open('Jokes.txt','r') as jok:
        for line in jok:
            text=(jok[random.choice(a)])
            say(text)
            
        
    
    
                                   
            
                    
                    
    
             
def web():
         ans=input("Where you wanna search Youtube or web")
         
         say(ans)
         if(ans==1):
             
             url="What song you want"
            
             say(url)
             search=input()
             
             
             webbrowser.open("https://www.youtube.com/watch?v={}".format(search))
       
           
            
''' Main Code'''
            
a=input("Enter 1 to confirm that you are a human")
say("Thanks for your patience and we are confirming your request")

if(a=='1' or 1):
            print("Welcome")
            say("Welcome")
        
            time.sleep(5)
            string="Hello, Iam A ,your simple commandline  assistant I do simple tasks I am yet to be developed"
            print(string)
            say(string)
            print("Do you want to ask me something??")
            say("Do you want to ask me something")
            response=input()
            if response in positive_responses:
                ques()
            else:
                apology="I am sorry take care"
                print(apology)
                say(apology) 
                string=" You have other options like surfing web,weather checking etcc..."
                
                say(string)
                ans=input("If  you wanna continue give your response or else give your response")
                if(ans in positive_responses):
                    web()
                    
                
                sys.exit()

         
     
           
            
            
              


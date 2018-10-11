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
small_data={"What is your name":["My name is A"," Vichu named  me A but you can name me whatever you like",
                                 "A is how people call me"],
            "Are you still single":["Yes he wants me to be like him as he is single",
                                    "I'm not single I am surrounded by lines of code alwayss",
                                    "This  question is hypothetical","Being single is the  best"]
                                    
                                    
                                    
            }
positive_responses=['yes','yah','y','Y']
negative_responses=['nah','no','n','N']

default="Sorry I couldn't understand you since I am trained a little bit only"
def ques():
            ques=input("Ask me your  questions i think i can answer")
            if ques in small_data:
                            print(random.choice(small_data[ques]))
                
            else:
                            print(default)
      
                        
            
            
                   
def  access():
    pass
''' Updates yet to come'''
    
            
                    
                    
    
             
def web():
         ans=input("Where you wanna search Youtube or web")
         if(ans==1):
            url=input("What sitee you want")
            webbrowser.open("https://www.youtube.com/watch?v={}".format(url))
a=input("Enter 1 to confirm that you are a human")
if(a=='1' or 1):
    print("Validating pls wait")
    time.sleep(5)
    print("Hello, Iam A your simple commandline  assistant I do simple tasks I am yet to be developed")
    response=input("Do you want to ask me something??")
    if response in positive_responses:
        ques()
    else:
        print("I am sorry take care")
        sys.exit()
         
     
           
            
            
              


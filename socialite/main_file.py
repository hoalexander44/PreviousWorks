#This program uses object oriented programming to store people's information into socialite objects
from socialite import Socialite
#list that holds all created objects
socialite_list = []
#variable that checks input for Number of Socialites
stopper = 0
print("Welcome to CS 172: Socialite Homework")
#asks for how many socialites user wants to create
while stopper == 0:
    try:
        Socialite_Number = int(input("How many Socialites do you want to create?\n"))
        stopper = 1
    except ValueError:
        print("Please enter a number")
#where the object will be created and the attributes will be set and WHEN the objects will be stored
for i in range (0,Socialite_Number):
    print("Enter Data for Socialite",i+1)
    socialite_create = Socialite()
    First_Name = input("Enter First Name:\n")
    socialite_create.setFirstName(First_Name+" ")
    Last_Name = input("Enter Last Name:\n")
    socialite_create.setLastName(Last_Name)
    UserID = input("Enter User ID:\n")
    socialite_create.setUserID(UserID)
    Picture = input("Enter URL for Picture:\n")
    socialite_create.setPicture(Picture)
    Website = input("Enter URL for Website:\n")
    socialite_create.setWebsite(Website)
    Description = input("Enter Website Description:\n")
    socialite_create.setDescription(Description)
    socialite_list.append(socialite_create)
    print("Socialite Created\n")
#The Final output for the program where each individual object that is stored in the list will have the string representations printed
print("========Socialite Information===========")
for i in range (0,len(socialite_list)):
    a = socialite_list[i]
    print(a.str()+"\n")
#!/usr/bin/python3

user = input("What is your name? ")

print("Welcome to python" + user)  #Changed to lower case and removed ,

age = int(input("Please enter your age: "))
if age <= 17 :
    print("You have a curfew. Don't be late.")
elif age ==' 22' :
    print("You were born in 2000.")
elif age < 21 :
    print("Sorry, you're not old enough to buy alcohol.")
else:    #Removed statement
    print("You've come a long way. You should be proud of yourself.")

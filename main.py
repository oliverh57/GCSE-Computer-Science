# python GCSE computer sicence task
from utils import *
from game import *
from highscore import *

user1NAME = "Bob"  #define user1NAME name var
user1SCORE = 0

user2NAME = "Fred"  #define user2NAME name var
user2SCORE = 0

def authenticate():  #login function, returns username that has been authenticated
    INusername = input("Waht is your username?")
    if INusername in users:  #if the username exists in the array
        INpassowrd = input("What is your passowrd?")
        if INpassowrd == passwords[users.index(
                INusername
        )]:  #if the password is in the same position as the username
            if not INusername == user1NAME or INusername == user2NAME:
                print_ok("Succses! User logged in")
                return INusername  #return the username of the user
            else:
                print_error("Sorry, user is already logged in")
                return False
        else:
            print_error("Incorect password")
            return False
    else:
        print_error ("User does not exist")
        return False


users = []  #array that stores usernames
passwords = []  #array that stores passwords

f = open("users.txt", "r")  #open the txt with the users
for x in f:
    users.append(
        x.rstrip("\n").split(",")[0])  #add the username elm to user array
    passwords.append(
        x.rstrip("\n").split(",")[1])  #add the passowrd elm to the array
f.close  #close password data file

printlarge("GCSE Computer sicence")  #prtin title to comandline

while user1NAME == False:  #while value has not been set
    print("Enter details for user 1")
    user1NAME = authenticate()

while user2NAME == False:  #dito as 1
    print("\nEnter details for user 2")
    user2NAME = authenticate()

#users is now logged in. Next section handles gameplay
printlarge("game section")
printnl()

for i in range(1):
  printlarge("Round " + str(i+1))
  print(user1NAME + " is rolling...\n")
  user1SCORE = calscore(user1SCORE, user1NAME)
  input("\npress enter to continute\n")
  print(user2NAME + " is rolling...\n")
  user2SCORE = calscore(user2SCORE, user2NAME)
  input("\npress enter to continute\n")

printlarge("The Game has ended")
print(user1NAME + "'s score is " + str(user1SCORE))
print(user2NAME + "'s score is " + str(user2SCORE))


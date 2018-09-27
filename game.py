import random
import time
from utils import *

def roll():  #returns array with two rolls,total, if total is even
    time.sleep(1)  #pause for effect
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    even = ((a + b) % 2 == 0)
    return [a, b, a + b, even]

def calscore(scoretotal, username):
  diceinfo = roll()  #return array with useful info
  scoretotal += diceinfo[2]
  print(username + " rolled " + str(diceinfo[0]) + " and " + str(diceinfo[1]) + " totaling " + str(diceinfo[2]))
  if diceinfo[3] == True:
      print_green("Because total of the two rolls is even, you have had ten points added on")
      scoretotal += 10
  else:
    print_red("Because total of the two rolls is odd, five points have been subtracted")
    scoretotal -= 5
  if diceinfo[0] == diceinfo[1]:
    print_green("Because you rolled a double, you can now roll one dice again")
    a = roll()
    print_green("You rolled a " + str(a[0]) + " your roll has been added to your score")
    scoretotal += a[0]
  if scoretotal < 1: #if score is less than 1
    scoretotal = 0 #set score to 0
  print("\nyou have now got " + str(scoretotal) + " points")
  return scoretotal
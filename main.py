"""
Q4 2020 sample text adventure game Part 2
Author: Victor Truong
version 1.2
May 15, 2020
...
author : mr Truong
p1 basic scenes
p2 invnetory
p3 fight
"""
from random import randint # allows creation of random numbers
name = "" #variable for character name
playerHP = 100 #varible to hold player's health points
inventory = ["cheap sword"] #variable for player's inventory using a list data structure
gold = 0 #variable containing amount of gold user has

def startGame():#first scene of the adventure
  global name #allows the use of the name variable in line 13 so it doesn't overwrite with a local variable
  name = input("You are a Pythonian, a villager of Codeia. What is your name? ")
  adventure = input("\nHello " + name +" Do you want to go on an adventure? \nEnter 1 for yes or 2 for No. > ")

  if adventure == "1":#remember input is in string format
    goAdventure()#calls the next scene in the game
  else:
      print("\n" + name.upper() + "!!! You\'re lame and live out your life in boredom!!")#ends the game with a lame message
        
def goAdventure():
  global name
  
  choice = input("\n" + name + """ Do you want to go to the forest or the mountain?\n
Options - enter the number you want to go to:
      1. go to the dark forest
      2. go to the mountain
      Choice: > """)
      
      #check user input to find out what function to call next
  if(choice == "1"):
    goToForest()
  elif(choice == "2"):
    goToMountain()

def goToForest():
  print("\nYou head to the dark...")
  choice = input("""\nDo you take the LONG route or the SHORT route\n
  Options - Enter the number of your choice
  1. Take the Short route
  2. Take the Long round
  Choice: > """)
  
  if choice == "1":
    getLost()
  elif choice == "2":
    goToMountain()
  else:
    goToForest()

def goToMountain():
  global inventory
  global gold
  global playerHP

  print("\nYou have reach the mountain of the Blah Blahs ")
    
  print("You see a treasure box!")
  choice = input("""
  What do you do?
  options:
  1. Open it
  2. Check your Inventory
  3. continue down the trail
  4. go to forest
  Choice: > """)
  
  #possible logic error for infinite repeating treasure pick 
  # up - could use flag to prevent
  if (choice == "1"):
    print("You find a Healing Potion")
    inventory.append("healing potion")
    print("*** Healing potion added to inventory ***")
    print("\nYou find 10 gold pieces and a shiny sword")
    gold = gold + 10
    inventory.append("shiny sword")
    print("you throw away your cheap sword for the shiny sword")
    inventory.remove("cheap sword")
    print("You now have " + str(gold) + " gold pieces and In your inventory:")
    print(inventory)
  
  elif (choice == "2"):
    print("\nInventory: ")
    print(inventory)
    choice = input("What would you like to use? " + 
    "\nType nothing to use nothing")
    if(choice == "nothing"):
      print("Nothing used")
    elif (choice.lower() in inventory):
      if(choice.lower() == "healing potion"):
        playerHP += 10
        print("You feel refreshed! your HP is at: " + playerHP)
      print("Used " + choice + " from inventory")
      inventory.remove(choice.lower())
    else:
      print("Item does not exist in inventory")
    goToMountain()

  elif (choice == "3"):
    winGame()#you wouldn't actually win the game here as it is too early but this is just an example so it's ending here. you would put your next function here for the next scene
  else:
    goToForest()#loops back to different part of game

def getLost():#end of game
  global playerHP
  print("""\nYou got lost... and hit your head 
  You LOSE 5 HP
  you make it back to the start of the forest""")
  if(playerHP - 5 > 0):
    playerHP -= 5
    goToForest()
  else:
    gameOver();  

def winGame():#end of game
  print("\nYou win!! game over")
  exit()

def gameOver():#end of game
  print("\nYou DIED!! game over")
  exit()

# Create more functions to complete the game

# Don't forget to call the startGame function!  
startGame()

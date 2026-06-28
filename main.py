print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
print("     Type 'left' or 'right'" )
condition = input("")
if condition == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    print("   Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    con2 = input("")

    if con2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print(" One red, one yellow and one blue. Which colour do you choose?")
        con3 = input("")
        if con3 == "blue":
            print("ou enter a room of beasts. Game Over.")
        elif con3 == "yellow":
            print("You Win")
        elif con3 == "red":
            print("Burned by fire. Game Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over.")
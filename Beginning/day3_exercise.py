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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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


#Write your code below this line 👇
print("There are two routes. Which route you want go?")
direction = input("Left or right?")
if direction.lower() == "left":
    print(f"you chose {direction}. You've successfully completed the first step.\n")
    print("You see a desserted island across the river. Do you wanna take your chance?")
    direction = input("Do you wanna 'swim' or 'wait'?")
    if direction.lower() == "wait":
        print(f"you chose {direction}. Well done. You are closer to your destination.\n")
        print("Congratulations!! you've found a treasure house. Be mindful which door to chose from.\n")
        door = input("choose the door, 'blue', 'yellow' or 'red'?")
        if door.lower() == "blue":
            print(f"you chose {door} door. Opps!! that's Lucifer. You died.")
        elif door.lower() == "red":
            print(f"you chose {door} door. Opps!! You are in hell. You died.")
        elif door.lower() == "yellow":
            print(f"you chose {door} door. Lesss fuckin gooo. You've found the treasure. Congratulations!!!")
        else:
            print(f"you chose {door} door. You failed to choose any door. You died.")
    else:
        print(f"you chose {direction}. Unfortunately your mission ends here. Try again.")
else:
    print(f"you chose {direction}. Unfortunately your mission ends here. Try again.")

print("you are alone in a forest...")
print("there are three roads ahead(left, middle, left)... ")
print("which road do you take?(left, right, middle)")
road = input("choose:  ")
if road == 'right':
    print("so you decided to take the dark road ahead, not many choose this path...")

elif road == 'left':
    print("the left path of the world is not for the weary, you have a taste for challenge ")

elif road=='middle':
    print("most people take the middle road, no shame in keeping it safe")

elif road=='back':
    print("you are going back? smart!")

else:
    print("WHAT ARE YOU DOING!!?? MOVE!!")
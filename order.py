#text based story where multiple paths push you towards different roles 
#left, right, middle... and secret outcome if choosing to walk back 
#left - loner, trecking through a dense forest...what would you find at the end 
#right - a single companion, a "pet" or a "tank" to watch your back
#middle -  grouped with others under a leader who hogs the glory, and exp... is it you or someone else...
#walk back - choosing not to play the game, that is the best outcome

print("you are alone in a forest...")
print("there are three roads ahead(left, middle, left)... ")
print("which road do you decide to take?(left, right, middle)")
road = input("choose:  ")
if road == 'right':
    print("so you decided to take the dark road ahead, not many choose this path...")
    print(" futher down the road you find an injured dog, what do you do?")
    choice = input("ignore, heal, feed? ")
    if choice == 'ignore':
        print("i wouldnt have choose that")
    elif choice == 'heal':
        print("not many would have done that...")
    elif choice == 'feed':
        print('hope you know what you are doing... that was your last heal...')


elif road == 'left':
    print("the left path of the world is not for the weary, you have a taste for challenge ")

elif road=='middle':
    print("most people take the middle road, no shame in keeping it safe")

elif road=='walk back':
    print("you are going back? smart!")

else:
    print("WHAT ARE YOU DOING!!?? MOVE!!")
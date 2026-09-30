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
        print("after walking down the cave someone approaches you...")
        person = input("let's walk this road together, we can keep each other safe...(yes or no)")
        if person == 'yes':
            print("can you trust a rando  you met on a dark forest?")
            print("while fighting your way through the forest, the TANK lets you pick between special tea or water")
            hydrate = input("water or tea?....")
            if hydrate == 'tea':
                print("the last thing you see as you close your eyes is the rando approaching you with a knife...")
                print("GAME OVER!!!!")
                print("...")
                print("...")
                last_chance = input("press the button of that mistery bottle you found in a dungeon...(yes/no)")
                if last_chance == 'yes':
                    print("the bottle shoots a laser through the rando.....")
                    print("you survived!!")
                else: 
                    print("you were destined to be ended")

    elif choice == 'heal':
        print("not many would have done that...")
    elif choice == 'feed':
        print('hope you know what you are doing... that was the last of your food...')


elif road == 'left':
    print("the left path of the world is not for the weary, you have a taste for challenge ")

elif road=='middle':
    print("most people take the middle road, no shame in keeping it safe")

elif road=='walk back':
    print("you are going back? smart!")

else:
    print("WHAT ARE YOU DOING!!?? MOVE!!")
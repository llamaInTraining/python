print("Welcome to Byte and Brew Tech Cafe!")

total = 0
items_selected = 0
while items_selected < 3:
    print("Menu")
    print("1. Black Coffee - $2.50")
    print("2. Vanilla Latte - $4.00")
    print("3. Blueberry Muffin - $3.00")
    print("4. Complete Order")
    choice = input("Enter item number (1-4): ")

    if choice == "1":
        total += 2.50
        items_selected += 1
        print("Black Coffee added.")

    elif choice == "2":
        total += 4.00
        items_selected += 1
        print("Vanilla Latte added.")

    elif choice == "3":
        total += 3.00
        items_selected += 1
        print("Blueberry Muffin added.")

    elif choice == "4":
        print("have a lovely day")
    else:
        print("invalid choice")
    print("total cost is:",total )


    










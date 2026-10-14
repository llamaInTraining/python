#create a while a loop that continues, an mutable AND immutable list
#start with two list: mutable and immutable
approve_models = ("MacBook Pro", "Dell XPS", "ThinkPad")
device_inventory= []
while True:
    print("1: Add: ")
    print("2: remove: ") 
    print("3: View: ") 
    print("4: Exit: ")
    choice = input("enter choice: ")
    if choice == "1":
        new_item = input("enter the new item:  ")
        if new_item in approve_models:
            device_inventory.append(new_item)
        else:
            print("device not approved")
    elif choice == "2":
        print(device_inventory)
        delete = input("enter item to remove:  ")
        if delete in approve_models:
            device_inventory.remove(delete)
        else:
            print("device not on the list")
    elif choice == "3":
        print(device_inventory)
    elif choice == "4":
        print("thank you for using our system ")
        break
    else:
        print("not available. ")

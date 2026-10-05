for i in range(4):
    print('hi')


#count = 1
#while count > 0:
    #print("processing")
    #count += 1

    #break

#while True: 
    #cmd = input("Type 'exit' to quit: ") 
    #if cmd == "exit": 
       # print("Shutting down.") 
    #break

for i in range(0,6):
    print("forward...",i)

for i in range(10,0,-1):
    print("backwards...",i)

while True:
    age = input("enter the age: ")
    if age.isdigit():
        age = int(age)
        print("age accepted")
    else:
        print("invalid. numbers only")
    break

secret_pin = "8888"
attempts = 0
while attempts < 3:
    guess = input("ENTER PIN: ")
    if guess == "8888":
        print("you are in")
        break
    elif guess != "8888":
        attempts += 1
        if attempts == 3:
            print("You can try again in 30 minutes")
        
    

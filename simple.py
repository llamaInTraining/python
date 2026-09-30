print("welcome user")
name= input(" please provide your name: ")
#print("Thank You, ",name)
age= int(input("please provide your age: "))
#print("Thank You!")
salary = float(input(" please enter your salary: $"))
print("your name is", name, "your age is", age, "your salary is", salary)
student = input("do you attend LAGCC?(Y/N)")
enrolled= True
not_enrolled= False
if student.lower()== 'y':
    print("that is interesting")
    #major = input("what is your major?  ")
    #print("your major is",major,"AND it is",
          #enrolled, "you are a student")
    print("it's", enrolled)
       
elif student.lower() == 'n':
    print("It's", not_enrolled)

else:
    print("what are you trying to do?")
#Greeting
print("Welcome to my computer quiz")

#"Do you want to play?" Question
playing = input("Do you want to play? ")

if playing != "yes":
    quit() 

print("Okay! Let's Play :)")

#First Question
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

# Secound Question
answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")

#Third Question
answer = input("Whats Linux? ")
if answer == "Linux is an open source Operating System":
    print("Correct!")
else:
    print("Incorrect!")

#Forth Question
answer = input("What does software do? ")
if answer == "Instructions that tell a computer what to do.":
    print("Correct!")
else:
    print("Incorrect!")
    
# The ending thing
print("Thank You for playing!")

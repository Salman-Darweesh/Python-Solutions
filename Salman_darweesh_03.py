    # Welcoming the user, asking if they want to play a game -  SAW Version
choice_1 = input("Hello! Wanna play a game? (yes/no): ")
    # using and using .lowwer conversion to change character to lowercase
if (choice_1.lower() == "yes"):
    print("you cannot go back now")
    print
    
if choice_1 == "no":
    print("you have chosen the safe route of not playing")   

    # creating a counter
counter = 0 
    # answers to the riddles
riddle_1 = "your left hand"
riddle_2 = "a towel"
riddle_3 = "a rubber band"
riddle_4 = "g"
riddle_5 = "when it is ajar"

    # riddles given to the user as an input
rid_ans_1 = input("What can you hold in your right hand, but never in your left hand? ")
if rid_ans_1.lower() == riddle_1:   # making it so that it would make all characters lower case
    print("Correct!")
    counter +=1 # creating a coutner to add to the original value of 0
else:
    print("You got it wrong, L")

rid_ans_2 = input("What gets wet while drying? ")
if rid_ans_2.lower() == riddle_2:   # Relating a specific answer as seen above in the riddles page with the equals operator
    print("Correct!")
    counter +=1
else:
    print("You got it wrong, L")
    
rid_ans_3 = input("What kind of band never plays music? ")
if rid_ans_3.lower() == riddle_3:
    print("Correct!")
    counter +=1
else:
    print("You got it wrong, L")
    
rid_ans_4 = input("What is the end of everything? ")
if rid_ans_4.lower() == riddle_4:
    print("Correct!")
    counter +=1
else:
    print("You got it wrong, L")
    
rid_ans_5 = input("When is a door no longer a door? ")
if rid_ans_5.lower() == riddle_5:
    print("Correct!")
    counter +=1
else:
    print("You got it wrong, L")
    
if counter >= 3:    # refrenced from book, using operator to make a congrats for escaping
    print("Congratulations, you escaped the room of many riddles")
else:   # refrenced from book, using operator to make a failed escape printstmnt
    counter < 2 == print("Unfortunately, you did not escape the room of many riddles.")
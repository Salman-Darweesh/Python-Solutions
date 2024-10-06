# I have refrenced a few youtube videos to get a better understanding on how to use loops.
'''

here are the titles of those videos:
"while true loop until quit - by: TheEduGeek
"While True Loops in Python // Learning Python" by: Tommy's code
"For loops in Python are easy 🔁" by: Bro Code

'''
   
    # Welcoming the user, asking if they want to play a game.
choice_1 = input("Hello! Wanna play a game? (yes/no): ")
    # Using and using .lower conversion to change character to lowercase.
if (choice_1.lower() == "no"):
    print("you hae chosen the safe route of not playing the escape game")
    
if (choice_1.lower() == "yes"):
    print("Welcome!")   
    while True:     # Programmer controlled loop.
            # Creating a counter.
        counter = 0 
        
            # Creating an incorrect answers coutner.
        anticoutner = 0
        
            # Answers to the riddles as variables.
        riddle_1 = "your left hand"
        riddle_2 = "a towel"
        riddle_3 = "a rubber band"
        riddle_4 = "g"
        riddle_5 = "when it is ajar"

            # Questions given to user as variables.
        riddle_q_01 = "What can you hold in your right hand, but never in your left hand? "
        riddle_q_02 = "What gets wet while drying? "
        riddle_q_03 = "What kind of band never plays music? "
        riddle_q_04 = "What is the end of everything? "
        riddle_q_05 = "When is a door no longer a door? "

            # Riddles given to the user as an input.
        rid_ans_1 = input(riddle_q_01)
        if rid_ans_1.lower() == riddle_1:   # Making it so that it would make all characters lower case.
            print("Correct!, W")
            counter +=1 # Creating a coutner to add to the original value of 0 - correct answers.
            print(f"You currently have {anticoutner} Incorrect and {counter} Correct answers")
        else:
            print("You got it wrong, L")    # Response for getting it wrong.
            anticoutner += 1
            print(f"You currently have {anticoutner} Incorrect and {counter} Correct answers")  # Correct/inc preview text.

        rid_ans_2 = input(riddle_q_02)
        if rid_ans_2.lower() == riddle_2:   # Relating a specific answer as seen above in the riddles page with the equals operator.
            print("Correct!, W")   # Response for getting it right.
            counter +=1
        else:
            print("You got it wrong, L")
            anticoutner += 1
            print(f"You currently have {anticoutner} Incorrect and {counter} Correct answers")

        rid_ans_3 = input(riddle_q_03)
        if rid_ans_3.lower() == riddle_3:
            print("Correct!, W")
            counter +=1     # Creating a coutner to add to the original value of 0 - Incorrect answers.
            print(f"You currently have {anticoutner} Incorrect and {counter} Correct answers")
        else:
            print("You got it wrong, L")
            anticoutner += 1
            print(f"You currently have {anticoutner} Incorrect and {counter} Correct answers")

        rid_ans_4 = input(riddle_q_04)
        if rid_ans_4.lower() == riddle_4:
            print("Correct!, W")
            counter +=1
        else:
            print("You got it wrong, L")
            anticoutner += 1
            print(f"You currently have {anticoutner} Incorrect and {counter} Correct answers")

        rid_ans_5 = input(riddle_q_05)
        if rid_ans_5.lower() == riddle_5:
            print("Correct!, W")
            counter +=1
        else:
            print("You got it wrong, L")
            anticoutner += 1
            print(f"You currently have {anticoutner} Incorrect and {counter} Correct answers")

        if counter == 5:    # Refrenced from book, using operator to make a congrats for escaping.
            print(f"Congratulations, you escaped the room of many riddles, you have {counter} Correct answers")
            break   # Loop ends.

        else:   # Refrenced from book, using operator to make a failed escape print statment.
            print(f"Unfortunately, you did not escape the room of many riddles, there were only {counter}/5 Correct answers")
            round_2 = input("Play again, type yes: ")
            continue

# I have refrenced a few youtube videos to get a better understanding on how to use loops - Refer to the top of the program in comments.

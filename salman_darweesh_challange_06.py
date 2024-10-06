import random       # immporting random numbers

def writing_part():     # new def that takes the number transfered from starting()
    user_rand_value = starting()    # calls the starting function 
    with open (r"/Users/salmandarweesh/Desktop/testing.txt", "w") as file:      # while true to make a file, no need for closing line of code
                for i in range(user_rand_value):    
                    rand_number = random.randint(1, 500)    #generates random numbers based on the user given value
                    file.write(str(rand_number) + '\n')     # writes the numbers on different lines. 
    
def starting():     # this creates a def for the code for users to enter a number to generate random numbers
    while True:     # using a while true to make an exception, if true then it will continue.
        try:
            user_rand_value = int(input("Enter a number: "))       # creating a variable and asking user to input an integer
            return user_rand_value      # if its and integer it will be transfered to def writing()
        except ValueError:      # this is when user types a non integer, it would give them an error
            print("Your number is not an integer.")     #tells user its not a number
    

if __name__ == "__main__":      # this is where the program starts
    writing_part()      # calling a specific function, to "start"
    
'''
Refrences: 
Module 4 i in range
Module 5 video
MOdule 5 Lecture code for random number int
Module 6 looking at loops with exceptions
Ch 6 page 383
'''

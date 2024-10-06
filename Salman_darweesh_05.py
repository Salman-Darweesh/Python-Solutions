print("Welcome")    # welcoming the user with a print statement - no input needed.

g = 9.8     # gravity value as a variable in m/s/s.

def falling_ball_time():
    global number_chosen_time   #creating a global term for number chosen
    calculation_distance_formula = 0.5 * g * (number_chosen_time ** 2)      #creating the formula thats used to calculate the time, based on user chosen number.
    # creating a cconversion formula, using the right operators, and making sure its time^2.
    return calculation_distance_formula     #returing the distance that has been calulated

def all_time_shown_as_list():
    global number_chosen_time # usin the global term that was created earlier
    # making it list of each second the ball has fallen up until the chosen value 
    for time in range(1, number_chosen_time +1):   # creating an inc that starts from 1/ends on user choice +1
        calculation_distance_formula = 0.5 * g * (time ** 2)    #calling function to be used for the calculation.
        # showing the user the distance fallen with 1 decimal space, and reitterrating the time they chose to see how far the ball has fallen. 
        print(f"based on the value of {time} the ball has fallen by {calculation_distance_formula:.2f}") #displaying the time and the 


if __name__ == "__main__":  # creating a starting point for where the program starts. 
    #using int(input to ask the user for a value to be used un the formula (applied later). this is used to be the first thing for the program to start 
    number_chosen_time = int(input("Enter a value (seconds) to see how far the ball has fallen: "))
    all_time_shown_as_list()    # calling a function so it would show the resuts that are made from the given vlaue 
    
'''
Refrences: 
Module 5 lecture code for how to use the return part
Module 5 in class lecture specifially for using "global"
Module 5 video attatched on canvas
Module 4 how to use if in range 
'''

'''
i also ran into an issue where g for gravity was not working and 
instead I moved it out of the first def and it worked perfectly. 
'''






    
    
def getting_the_sum(n): # Creating the function to calc user input
    
    # Base case for the recussion: stops it if its 1
    if n == 1: 
        return 1
    else:
        return n + getting_the_sum(n - 1) # Recursive call, meaning the function calls itself.
    
    
if __name__ in "__main__": # where it starts
    user_chosen_value = int(input("What calue would you like to find the complete sum of (between 0 and 100): "))   #asking user for value

    while user_chosen_value not in range(1, 101):  # memory hog or it will eat up lots of memory, making user input within range
        print("you have not entered a valid number, try again.")    #error message
        user_chosen_value = int(input("What calue would you like to find the complete sum of (between 0 and 100): "))
    
    sum_of_number = getting_the_sum(user_chosen_value)  #using recursive function to calculate sum
    
    print(f"The total sum of your value is -- {sum_of_number} -- ") #Display result
    print(f"Based on the given value of -- {user_chosen_value} -- ") #Display result
    
    
'''
Refrences:
Module 10
Chapter 12 Book
'''






    
    
def getting_the_sum(n):
    
    # Base case for the recussion: 
    if n == 1: 
        return 1
    else:
        return n + getting_the_sum(n - 1) # Recursive call, meaning the function calls itself.
    
    
if __name__ in "__main__":
    user_chosen_value = int(input("What calue would you like to find the complete sum of (between 0 and 100): "))

    while user_chosen_value not in range(0, 101):
        print("you have not entered a valid number, try again.")
        user_chosen_value = int(input("What calue would you like to find the complete sum of (between 0 and 100): "))
    
    sum_of_number = getting_the_sum(user_chosen_value)
    
    print(f"The total sum of your value is -- {sum_of_number} -- based on the given value of -- {user_chosen_value} -- " )




import re


def checking_if_valid(password_given):  # Creating afunction with the user input as parameter
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%*!])[A-Z a-z 0-9 @#$%*!]{8,}$" #reating a regex object using the raw string
    
    
    if re.match(pattern, password_given):
        print("Valid.") # if it matches the pattern that it is supposed to be, then it will say valid. 
        
    else:
        print("Invalid.")   # tellin user its not a valid passoword with else
    

if __name__ in "__main__":
    password_given = input("Enter a password to see if its valid: ")    #asking user to input a value
    checking_if_valid(password_given)   #calling the function with parameter 

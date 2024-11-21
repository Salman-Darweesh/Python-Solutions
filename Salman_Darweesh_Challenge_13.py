



import re


def checking_if_valid(password_given):
    pattern = r"^[A-z 0-9 @#$%*!]{8,}$" #reating a regex object using the raw string
    
    if re.match(pattern, password_given):
        print("Valid.")
        
    else:
        print("Invalid.")
    

if __name__ in "__main__":
    password_given = input("Enter a password to see if its valid: ")
    checking_if_valid(password_given)

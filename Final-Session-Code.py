


# --- Final Review --- 
# no recusion, oop, regular expressions
# CH 5 - 6 - 7 - 8
# - for loops (string/ dictionary) 
# - if structures 
# - functions (how to recieve a arguemnt with function call such as parameters)
# - if name - 
# - return types through functions 
# - CH about strings how to determine charactrs in string (alphanumeric ext ext)
# lists append insert pop
# dictionaries - how to create a empty adn store a key value, now to orint a specific value associated with a key
# ---------------------------------------------------------------------------------------------------------------------------------------------
'''

is alpha - only ask for letters and not numbers
'''

"$9//iLovepizza11'OR==1'$" #sql injection protection command

# this function removed the bad characters from the users name and then forwards the actual username to database
def sanitize(unsanitized_string):
    
    san_string = []
    
    # remove characters that are not lowercase letters
    for character in unsanitized_string:
        if character.isalpha() and character.islower():
            san_string.append(character)
            #print(char, end="")
        else:
            print("", end="")
        
    san_string = "".join(san_string)

def function_sanitize(rec_san_string):

    username_dict = {}
    username_dict["iLovepizza"] = rec_san_string
    print(username_dict)

if __name__ in "__main__":
    
    unsanitized_string = input("Enter a string with special characters and numbers: ")
    sanitize(unsanitized_string)
    
    # Return the ductionary and print it to the screen with the new username.
    
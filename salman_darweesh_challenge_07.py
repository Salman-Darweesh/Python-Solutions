# i feel like there are lots of mistakes in this challenge, primarly cause i was more
# focused on other subjects and tried to ge this working even though i feel like its a little messy

def Stored_Passwords(CheckPass):    #using the required def
    global GOOD     # trying to use global to use GOOD in more that one function
    password_tuple = ("123456", "123456789", "12345", "qwerty", "password", "12345678", "111111", "123123", "1234567890", "1234567", "qwerty123", "000000", 
                      "1q2w3e", "aa12345678", "abc123", "password1", "1234", "qwertyuiop", "123321", "password123", "1q2w3e4r5t", "iloveyou", 
                      "654321", "666666", "987654321", "123", "123456a", "qwe123", "1q2w3e4r", "7777777", "1qaz2wsx", "123qwe", "zxcvbnm", "121212" , 
                      "asdasd", "a123456", "555555", "dragon", "112233", "123123123", "monkey", "11111111", "qazwsx", "159753", "asdfghjkl", "222222", 
                      "1234qwer", "qwerty1", "123654", "123abc")    # creating a tuple for all possible common passwords 
    
    if CheckPass in password_tuple:      # I am more thankful that were not using ingrement loops, that is the death of me. :P 
        location = password_tuple.index(CheckPass)  # locating where it is in the tuple 
        womp_womp = input(f"The password you have entered is common, and easily guessable. (it was found in {location}) Please enter your username again: ")
        #   addding a input to show here it was found in the tuple created
        return womp_womp    # sending the info backm and putting the user back in the loop
    
    else:
        GOOD = ("The password you have entered is great.")   # telling user the password woked
        return GOOD     # putting the user back in the loop


def Get_User_Pass():
    global GOOD     # i probably use global wrong, please let me know if I used it correctly or not (im just trying to add things here and there)
    GOOD = ("The password you have entered is great.")
    username = input("Please neter a Username you would like to use: ")     # asking user to give me a username
    
    while True:     # this is where the loop starts, asking them to give me a good password
        password = input("Please enter a Password you would like to use: ")     # asking for a password
    
        output = Stored_Passwords(password)     # checking if common or not
    
        print(output)   #result
        
        if GOOD in output:
            break       # if the global string is correct then it will break the loop and end the program.
    

if __name__ == "__main__":
    Get_User_Pass()     # calling the specific fuction to start
    
    
    '''
    refrences: 
    
    '''
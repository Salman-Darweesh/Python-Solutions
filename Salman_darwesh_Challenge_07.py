
def Stored_Passwords(checking):
    global GOOD
    password_tuple = ("123456", "123456789", "12345", "qwerty", "password", "12345678", "111111", "123123", "1234567890", "1234567", "qwerty123", "000000", 
                      "1q2w3e", "aa12345678", "abc123", "password1", "1234", "qwertyuiop", "123321", "password123", "1q2w3e4r5t", "iloveyou", 
                      "654321", "666666", "987654321", "123", "123456a", "qwe123", "1q2w3e4r", "7777777", "1qaz2wsx", "123qwe", "zxcvbnm", "121212" , 
                      "asdasd", "a123456", "555555", "dragon", "112233", "123123123", "monkey", "11111111", "qazwsx", "159753", "asdfghjkl", "222222", 
                      "1234qwer", "qwerty1", "123654", "123abc")
    
    if checking in password_tuple:      # I am more thankful that were not using ingrement loops, that is the death of me. :P
        womp_womp = ("The password you have entered is common, and easily guessable. Please enter a different password: ")
        location = password_tuple.index(checking)
        
        return womp_womp, location
    
    else:
        GOOD = ("The password you have entered is great.")

        return GOOD



def Get_User_Pass():
    global GOOD
    Username = ("Please neter a Username you would like to use: ")
    Password = ("Please enter a Password you would like to use: ")
    
    Output = Stored_Passwords(Password)
    
    print(Output)
    
    


if __name__ == "main":
    Get_User_Pass()
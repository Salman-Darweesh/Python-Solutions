


def getUser_Pass():
    ask_username = input("Please enter a username you would like to use: ")
    
    print(f"The username you chose was, {ask_username}")
    
    password_question = input("Please enter a password you would like to use: ")
    
    password = stored_Passwords(password_question)
    
    print(password)
    
    
    
def stored_Passwords(Same_Password_Questionmark):
    password_tuple = (123456, 123456789, 12345, "qwerty", "password", 12345678, 111111, 123123, 1234567890, 1234567, "qwerty123", 000000, 
                      "1q2w3e", "aa12345678", "abc123", "password1", 1234, "qwertyuiop", 123321, "password123", "1q2w3e4r5t", "iloveyou", 
                      654321, 666666, 987654321, 123, "123456a", "qwe123", "1q2w3e4r", 7777777, "1qaz2wsx", "123qwe", "zxcvbnm", 121212, 
                      "asdasd", "a123456", 555555, "dragon", 112233, 123123123, "monkey", 11111111, "qazwsx", 159753, "asdfghjkl", 222222, 
                      "1234qwer", "qwerty1", 123654, "123abc")  # immutable
    while True:
            womp_womp = ("The password you have entered is a common password, Try again. ")
            
            location = password_tuple.index(Same_Password_Questionmark)
            
            print(womp_womp)
            
            return location

if __name__ in "__main__":
    getUser_Pass()



class Person():# creating a class for the person
    def __init__(self, customer_name, customer_tele, customer_living_space):#initializing all info for name, tele, and living space
        self.customer_name = customer_name
        self.customer_tele = customer_tele
        self.customer_living_space = customer_living_space
        

    def get_customer_name(self):    # This is where you access the info 
        return self.customer_name
    
    
    def get_customer_tele(self):    # This is where you access the info 
        return self.customer_tele    # returning stat (Getting)
    
    
    def get_customer_living_space(self):    # This is where you access the info 
        return self.customer_living_space    # returning stat (Getting)
    
    
    def set_customer_name(self, customer_name):
        self.customer_name = customer_name      # Setting stat
    
    
    def set_customer_tele(self, customer_tele):     #creating a function for customer tlee
        self.customer_tele = customer_tele      # Setting stat
        
        
    def set_customer_living_space(self, customer_living_space):     #creating a function for living space 
        self.customer_living_space = customer_living_space      # Setting stat
        
        
class Customer(Person):
    customer_number = ""    # attributes, if given an attribute then it would be pointless
    customer_mail = ""
    
    def __init__ (self, customer_name, customer_tele, customer_living_space, customer_number, customer_mail_list):
        super().__init__(customer_name, customer_tele, customer_living_space)#initializing all info 
        self.customer_number = customer_number  # initializing the second part and useing a super() to use the previous info
        self.customer_mail_list = customer_mail_list
        
    def set_customer_number(self, customer_number):   #creating a function for customer number
        self.customer_number    #Setting stat


    def set_customer_mail_list(self, customer_mail_list):   #creating a function for mailing list
        self.customer_mail_list    #Setting stat
            # This is where you access the info 

    def get_customer_number(self):    # This is where you access the info 
        return customer_number    # returning stat info(Getting)
        
    
    def get_customer_mail_list(self):    # This is where you access the info 
        return customer_mail_list    # returning stat info(Getting)


            

if __name__ in "__main__":

    customer_name = input("PLease enter your name: ").upper()   # making all info given into caps
    
    customer_tele = input("Please enter your current telephone number: ").upper()   # asking for user input
    
    customer_living_space = input("Please enter yout current address ").upper()   # asking for user input
    
    customer_number = input("Please enter your customer number: ").upper()   # asking for user input
    
    customer_mail_list = input("Would you like to sign up to a mailing list (yes or no)? ").upper()   # asking for user input
    
    while customer_mail_list != "YES" or customer_mail_list != "NO":    # had to refer to a earlier module for this, seemed like i forgot
        if customer_mail_list == "YES" or customer_mail_list == "NO":   # turned out I was making a mistake by leaving it in the class on accident
            break
        
        else:
            customer_mail_list = input("Try Again, using only yes or no: ").upper()   # asking for user input, error when given anything other than yes or no
        
    
    user = Customer(customer_name, customer_tele, customer_living_space, customer_number, customer_mail_list) #where all info given are taken to consideration for the class
    
    print(f"Hello {customer_name} your tele number is {customer_tele}, living in {customer_living_space} and you chose to {customer_mail_list} ")
        # shows user all details of their details 
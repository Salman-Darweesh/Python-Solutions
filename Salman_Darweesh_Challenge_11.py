


class Person():
    def __init__(self, customer_name, customer_tele, customer_living_space):
        self.customer_name = customer_name
        self.customer_tele = customer_tele
        self.customer_living_space = customer_living_space
        

    def get_customer_name(self):    # This is where you access it 
        return self.customer_name
    
    
    def get_customer_tele(self):
        return self.customer_tele
    
    
    def get_customer_living_space(self):
        return self.customer_living_space
    
    
    def set_customer_name(self, customer_name):
        self.customer_name = customer_name
    
    
    def set_customer_tele(self, customer_tele):
        self.customer_tele = customer_tele
        
        
    def set_customer_living_space(self, customer_living_space):
        self.customer_living_space = customer_living_space
        
        
class Customer(Person):
    customer_number = ""
    customer_mail = ""
    
    def __init__ (self, customer_name, customer_tele, customer_living_space, customer_number, customer_mail_list):
        super().__init__(customer_name, customer_tele, customer_living_space)
        self.customer_number = customer_number
        self.customer_mail_list = customer_mail_list
        
    def set_customer_number(self, customer_number):
        self.customer_number


    def set_customer_mail_list(self, customer_mail_list):
        self.customer_mail_list

    def get_customer_number(self):
        return customer_number
        
    
    def get_customer_mail_list(self):
        return customer_mail_list
    
    
    def printing_results():
        customer_mail_list = input("Would you like to sign up for the mailing list that we have (yes or no): ")
        customer_mail_list.lower()


if __name__ in "__main__":
    
    customer_name = input("PLease enter your name: ")
    
    customer_tele = input("Please enter your current telephone number: ")
    
    customer_living_space = input("Please enter yout current address ")
    
    customer_number = input("Please enter your customer number: ")
    
    customer_mail_list = input("Would you like to sign up to a mailing list (y or n)? ")
    
    user = Customer(customer_name, customer_tele, customer_living_space, customer_number, customer_mail_list)
    
    while True:
        
            print(f"You have chosen to  sign up for the mail list")
            
 
        
    print(f"Hello {customer_name} your tele number is {customer_tele}, living in {customer_living_space} and you chose to {customer_mail_list} ")
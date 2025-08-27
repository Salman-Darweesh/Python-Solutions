


#Instructions:   using the string below, I want you to write a program that extracts the integers from the string 
# in a function called extractIntegers() and then passes the numbers as a list to a function called, listSort().  
# You will then sort the list in the listSort() function and print it to stdout (the console) in reverse order.  
# You need to ensure that you pass the string to extractIntegers() from the main function. In other words, you
# should call extractIntegers() from main and pass the string as an argument to extractIntegers(). 

#final_exam_string = "2 Happy 60 To End 7 This 8 Semester 54."

# Notes:  Your program needs to be able to see that 60 is a single value and not 
# interpret the data as 6  0.  (Notice the space I put between the 6 and the 0). 
# This IS your final exam, so the programming challenge is worth 200 points. 


'''
while string_list:
    highest = string_list.pop() # removed the key value, returns it plage 530 of book - refrenced it even thought it was for dictionaries
    string_list.replace("6", "").replace("0","")
    reversing_numbers.append(highest) # adding the object to the list.
        
    print(reversing_numbers)    # pritning it in reverse
'''
     # i also tried it this way and i could not get the 60 to return as 60. it only seperates it as individual values.
    

def exctractIntegers(final_exam_string):   # creating a function with the user input as the parameter
    string_list = []    # creating a list for the string 
    relacing_info = final_exam_string.replace("Happy", "").replace("To", "").replace("End", "").replace("This", "").replace("Semester", "").replace(".", "")
    # removing  all the words and punctuation that are part of it to make it so its only numbers, page 503 from textbook
    # also refrenced what was written in the final session coding script with .replace the words with essentially nothing = ""
    
    for characters in relacing_info:    # page 446 used to to help with appending the information
        relacing_info.split()   # page 507 in book, refrenced that to remove the trailing and leading white spaces.
        if characters.isdigit():    # finds digits only - page 499
            string_list.append(characters)  # adding the object to the list. - page 453 talks about how tuples are an exception to the rule so i derived it from that
    return string_list  # returns the string to be used in the next function.

def listSort(string_list):  # applies previous list to the function as a parameter.
    string_list.sort()  # sorting the list
    
    reversing_numbers = []  # creating a list for the string 
    
    while string_list:
        highest = string_list.pop() # removed the key value, returns it plage 530 of book - refrenced it even thought it was for dictionaries
        reversing_numbers.append(highest)       # adding the object to the list.
        
        print(reversing_numbers)    # pritning it in reverse

if __name__ in "__main__":  # where the function starts
    final_exam_string = "2 Happy 60 To End 7 This 8 Semester 54."   # provided string that was given
    exctractIntegers(final_exam_string) # running the function
    listSort(exctractIntegers(final_exam_string))      # what was returned is now applies to the sorting function
    
    # i also refrenced the middle section in the review session that we did to help create the "for chaaracters in replaceing_info"
    
    

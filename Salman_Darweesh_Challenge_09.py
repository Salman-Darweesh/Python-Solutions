
    # functon used to start the program
def step_01():
    # using professor given path to access a file, creating a while true loop (for practice)
    while True:
        file_reading = open("/users/burres/desktop/Word_Frequency.txt", "r")
            # now to create a dictionary for the value pair, matcing the word w/ # of times it shows up
        dictonary = {}
            # making the file read line by line
        for line in file_reading:
            
            line = line.replace(".", "")    # removing punctuation
            line = line.replace(",", "")    # removing punctuation
            
            content_in_file = line.lower().strip().split()  # making the program register that for every space,
                # it splits the word and recognizes it as a "word"

            for file_words in content_in_file:  #making it count for eac word
                if file_words in dictonary:
                    dictonary[file_words] = dictonary[file_words] + 1   # if the word exists, then all that happens is that it adds to its value
                else:
                    dictonary[file_words] = 1   # if not that "word," then, it adds to the value
                    
        occurances = dict(sorted(dictonary.items()))    # making it alphabetical
                    
        for key, number in occurances.items():  # priting each word to show occurances
            print(f"{key}; Appeared: {number}")
            
        break   # going out of the loop
        

# where the program starts
if __name__ == "__main__":
    step_01()     # calling the specific fuction to start
    
'''
Refrences: 
Class Lecture, and question asked after class
Module 7 
Module 5 
Module 6 
'''
    
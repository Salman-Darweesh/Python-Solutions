
def step_01(): # creating a function that runs the code
    asking101 = input("Please enter something into the Morse Code Translator: ")    # Variable created to ask user for what they want to translate
    makingAllLettersCapital = asking101.lower()     # forcing all input to be in lowercase
    
    alphabet = [" ", ",", ".", "?", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
                "g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        # creating a list for what is directly translated from the regular alphabet
    
    morseCode = [" ", "--..--", ".-.-.-","..--..", "-----", ".----", "..---", "...--", "....-", ".....",
                           "-....","--...", "---..", "----.", ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                           "..", ".---", "-.-", ".-..", "--","-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", 
                           "...-", ".--", "-..-", "-.-", "--.."]
        # creating list for morse code that matches with "alphabet"

    whereTheTranslationHappens = []     # storing locations of Morse code index
    
    lastStepTranslation = []    # This holds the translated version of whatever was the users input
    
    for i in makingAllLettersCapital:   # creating a loop to get every single location of the characters for their index
        if i in alphabet:   #checking to see if its in the alphabet. if not it will just ignore it 
            location = alphabet.index(i)    # finds the location in index
            whereTheTranslationHappens.append(location)     #saves it for later 

    for k in whereTheTranslationHappens:    # this is where the actual translation happens. 
        lastStepTranslation.append(morseCode[k]) # morse code translated by index
        
    print(" ".join(lastStepTranslation))      # based on how we covered it in class, im just applying it here to get rid of the commas and brackets to look pretty\
            # and prints the result.

    
if __name__ == "__main__": # this where the program starts
    step_01() #calling the specific function

'''
I used a part of something that we went over in class for the .join 
module 7 
module 6 
modulet 5 
'''
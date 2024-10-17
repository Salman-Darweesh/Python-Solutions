


def step_01():
    user = input("Please enter something into the Morse Code Translator: ")
    makingAllLettersCapital = user.upper()
    
    alphabet = [" ", ",", ".", "?", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
                "g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "x"]
    
    morseCodeTranslated = [" ", "--..--", ".-.-.-","..--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....",
                           "--...", "---..", "----.", ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....","..", ".---",
                           "-.-", ".-..", "--","-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                           "-.-", "--.."]

    whereTheTranslationHappens = []
    
    lastStepTranslation = []
    
    for i in makingAllLettersCapital:


if __name__ == "__main__":
    step_01()
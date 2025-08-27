    
'''
class firstGUI():
    def __init__(self):
        
        # set the dimentions of the window
        self.main_window = tkinter.Tk()
        
        self.label = tkinter.Label(self.main_window, text="Hellow World!")
        
        self.label.pack()
        
        tkinter.mainloop()

if main :
    my_gui = firstGUI()
'''
import tkinter 
import tkinter.font # used to create custom fonts (times new roman is the only good one)

class HollywoodStar_Challenge:
    
    def __init__(self):
        
        self.main_window = tkinter.Tk()     #init the main window
        
        self.main_window.title("Hollywood WAlk of Fame Star")   #giving the window a title 
        
        self.main_window.geometry("1000x1000")      # the space used for the window
        
        
        self.canvas = tkinter.Canvas(self.main_window, width=1000, height=1000,
                                     bg="pink")     # creating a custom font that would apply to the text that woul be centered in the star.
        
        times_new_roman_is_the_best = tkinter.font.Font(family="Times New Roman",   # creating a custom font function that would use a specific text size and font.
                                                        size=30, weight="bold")
        
        
        self.canvas.create_text(520, 520, text="Salman Darweesh",
                                font=times_new_roman_is_the_best, fill="black")     # took me a while to figure out how to move texts around in the way i wanted but this also applies the custom font
        self.canvas.pack()
        
        
        # to do this i heavily relied on desmos to plot points on the plane for the star
        self.canvas.create_line(520, 52, 620, 416, fill="black", width=2)
        self.canvas.create_line(620, 416, 988, 416, fill="black", width=2)   # creating the points for the star, it takes the form of (x1,y1) for the start and end to plot
        self.canvas.create_line(988, 416, 680, 650, fill="black", width=2)
        self.canvas.create_line(680, 650, 780, 988, fill="black", width=2)    # creating the points for the star, it takes the form of (x1,y1) for the start and end to plot
        self.canvas.create_line(780, 988, 520, 780, fill="black", width=2)
        self.canvas.create_line(520, 780, 260, 988, fill="black", width=2)   # creating the points for the star, it takes the form of (x1,y1) for the start and end to plot
        self.canvas.create_line(260, 988, 360, 650, fill="black", width=2)
        self.canvas.create_line(360, 650, 52, 416, fill="black", width=2)   # creating the points for the star, it takes the form of (x1,y1) for the start and end to plot
        self.canvas.create_line(52, 416, 420, 416, fill="black", width=2)
        self.canvas.create_line(420, 416, 520, 52, fill="black", width=2)   # creating the points for the star, it takes the form of (x1,y1) for the start and end to plot

        
        tkinter.mainloop()  # start

if __name__ == "__main__":
    HollywoodStar_Challenge()# calling the function used to execute the code.
    
    # Refrences used was te chapter and some of the lecture code that was provided.

'''
failed attepmts

        self.canvas.create_line(520, 52, 780, 988, fill="black")    # creating a line to make the shape of the star.
        self.canvas.create_line(780, 988, 52, 416, fill="black")
        self.canvas.create_line(52, 416, 988, 416, fill="black")
        self.canvas.create_line(988, 416, 260, 988, fill="black")
        self.canvas.create_line(260, 988, 520, 52, fill="black")
        
        
# self.canvas.create_polygon()


    def invert(self):   # creating a function to invert colors of star and text
        times_new_roman_is_the_best = tkinter.font.Font(family="Times New Roman",
                                                        size=30, weight="bold")     # creating a custom font that would apply to the text that woul be centered in the star.
        
        self.canvas.create_text(520, 520, text="Salman Darweesh",
                                font=times_new_roman_is_the_best, fill="black")     # took me a while to figure out how to move texts around in the way i wanted but this also applies the custom font
        
        self.canvas.create_line(520, 52, 780, 988, fill="black")
        self.canvas.create_line(780, 988, 52, 416, fill="black")
        self.canvas.create_line(52, 416, 988, 416, fill="black")  
        self.canvas.create_line(988, 416, 260, 988, fill="black")
        self.canvas.create_line(260, 988, 520, 52, fill="black")
'''
        

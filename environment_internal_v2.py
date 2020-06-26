#environment_internal_v2
#Ethan Montgomery

"""
#### CHANGE LOG ####
V.10 - App Jar
V.20 - Created base of the game
###################
"""

# import the library
from appJar import gui

### VARIABLES ###
userName = ""
questions = []
quizProgress = 0
score = 0

### CLASS DEFINITITIONS ###
class Question:
    def __init__(self, questionText, options, answer):
        self.questionText = questionText
        self.options = options
        self.answer = answer

    def displayQuestion(self):
        pass
    
    def getAnswer(self, button):
        pass
    
### FUNCTIONS ###

# handle button events
def press(button):
    pass

def buttonFunctions(button):
    pass

def start():
    pass   

def endScreen():
    pass

# create a GUI variable called app
app = gui("Environment Quiz", "800x400")
app.setResizable=False
app.setBg("black")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome To The Quiz", row=0, column=0)
app.setLabelBg("title", "black")
app.setLabelFg("title", "white")

# link the buttons to the function called press
app.addMessage("welcome", "Hello, who would you like to be refered as?", 1, 0)
app.setMessageFg("welcome", "white")
app.setMessageWidth("welcome", 400)
app.addLabelEntry("Name: ", 2,0)
app.setLabelFg("Name: ", "white")
app.addButtons(["Submit", "Cancel"], press)

### QUESTIONS ###

# start the GUI
app.go()

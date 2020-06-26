#environment_internal_v5
#Ethan Montgomery

"""
#### CHANGE LOG ####
V.10 - App Jar
V.20 - Created base of the game
V.30 - Created end screen
V.40 - Made end screen show how many answers you got correct out of how many
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
        buttons = ["A","B","C","D","E"]
        app.removeAllWidgets()
        app.addLabel("questionText",self.questionText)
        app.setLabelFg("questionText", "white")
        app.addButton("Next",buttonFunctions)
        app.hideButton("Next")
        i=0
       
        for option in self.options:
            app.addButton(buttons[i],self.getAnswer)
            app.setButton(buttons[i],option)
            i += 1
           
   
    def getAnswer(self, button):
        global score
        buttons = ["A","B","C","D","E"]
        i = 0
        for option in self.options:
            app.hideButton(buttons[i])
            i += 1
        if button == self.answer:
            app.setLabel("questionText", "Correct")
            score +=1
        else:
            app.setLabel("questionText", "Incorrect")
        app.showButton("Next")




### FUNCTIONS ###

# handle button events
def press(button):
    global userName
    if button == "Cancel":
        app.stop()
    else:
        userName = app.getEntry("Name: ").capitalize()
        start()
   
def buttonFunctions(button):
    global quizProgress
    if button == "Start":
        questions[0].displayQuestion()
    if button == "Next":
        if quizProgress < len(questions)-1:
            quizProgress += 1
            questions[quizProgress].displayQuestion()
        else:
            endScreen()
    #print(button)

def start():
    global userName
    app.removeAllWidgets()
    welcomeString = "Welcome "+str(userName)
    app.addLabel("test", welcomeString, 0, 0)
    app.setLabelFg("test", "white")
    app.addButton("Start",buttonFunctions)
   

def endScreen():
    app.removeAllWidgets()
    app.addLabel("finish","The quiz is over, your score has been printed below")
    app.setLabelFg("finish", "white")
    scoreString = str(score) +" / " +str(len(questions))
    app.addLabel("score",scoreString)
    app.setLabelFg("score", "white")
 
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
questions.append(Question("Who am I?",["Ethan","Ollie","Jed", "Nik"],"A"))
questions.append(Question("Who am I (2) ?",["Ethan","Ollie","Jed", "Nik"],"A"))


# start the GUI
app.go()

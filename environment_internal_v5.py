#environment_internal_v5
#Ethan Montgomery

"""
#### CHANGE LOG ####
V.10 - App Jar
V.20 - Created base of the game
V.30 - Created end screen
V.40 - Made end screen show how many answers you got correct out of how many
V.50 - Replaced questions with new ones
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
questions.append(Question("How much plastic enters the ocean every year?",["6 metric tonnes","7 metric tonnes","8 metric tonnes", "9 metric tonnes"],"C"))
questions.append(Question("How many Turtles die from plastic per year?",["1","10","100","1000"],"D"))
questions.append(Question("What percentage of plastic is recycled",["8.4%","20.3%","29.6%","46.7%"],"A"))
questions.append(Question("How much waste goes to landfill in NZ per year",["250 thousand tonnes","750 thousand tonnes","2.5 million tonnes","3.75 million tonnes"],"C"))
questions.append(Question("How many differing marine species are harmed by plastic?",["693","942","1371","1965"],"A"))
questions.append(Question("How many marine mammals die every year from plastic polution?",["50,000","100,000","150,000","200,000"],"B"))
questions.append(Question("How long does it take plastic to decompose",["100 years","1000 years","10,000 years","1 million years"],"B"))
questions.append(Question("What country puts the most plastic in the ocean?",["China","Russia","United States","Australia"],"A"))
questions.append(Question("What is the most common debris that litters our ocean",["Plastic bottles","Bags","Food packaging","Ciggarettes"],"D"))
questions.append(Question("What day is Earth day?",["February 12","April 22","June 9","October 17"],"B"))
questions.append(Question("Where does the majority of plastic waste end up?",["Recycled","Landfilled","Burned","Oceans"],"D"))
questions.append(Question("How many drinking straws worldwide do we use per day?",["5 milion","50 million","500 million","5 billion"],"C"))

# start the GUI
app.go()

#environmentInternal_V6
#Ethan Montgomery

"""
#### CHANGE LOG ####
V.10 - App Jar
V.20 - Creaded the base of the game
V.30 - Created end screen
V.40 - Made end screen show how many answers you got correct out of how many
V.50 - Replaced questions with new ones
V.60 - Commented
###################
"""

# import the library
from appJar import gui

### VARIABLES ###
userName = ""
questions = []
quizProgress = 0
score = 0

### CLASSES ###
class Question:
    """
    This function sets up the title information
    """
    def __init__(self, questionText, options, answer):
        self.questionText = questionText
        self.options = options
        self.answer = answer

    """
    This function displays the questions
    """
    def displayQuestion(self):
        buttons = ["A","B","C","D"] #ABCD because there is 4 possible answers avaliable
        app.removeAllWidgets() #Removes all widgets currently on the screen
        app.addLabel("questionText",self.questionText)
        app.setLabelFg("questionText", "white")
        app.addButton("Next",buttonFunctions)
        app.hideButton("Next")
        i=0
        
        #goes to next question
        for option in self.options:
            app.addButton(buttons[i],self.getAnswer)
            app.setButton(buttons[i],option)
            i += 1
           
    """
    This function checks the answers
    """
    def getAnswer(self, button):
        global score
        buttons = ["A","B","C","D"]
        i = 0
        for option in self.options:
            app.hideButton(buttons[i]) #hides buttons after button has been clicked
            i += 1
        #adds one point to the score
        if button == self.answer:
            app.setLabel("questionText", "Correct")
            score +=1
        #lets the user go to next question
        else:
            app.setLabel("questionText", "Incorrect")
        app.showButton("Next")




### FUNCTIONS ###
"""
This function asks for the name
"""
def press(button):
    global userName
    if button == "Cancel": #the person can cancel the quiz
        app.stop()
    else:
        userName = app.getEntry("Name: ").capitalize() #makes the username have a capital
        start()
        
"""
This function is what the buttons do to proceed in the quiz
"""
def buttonFunctions(button):
    global quizProgress
    if button == "Start":
        questions[0].displayQuestion()
    if button == "Next":
        if quizProgress < len(questions)-1: #-1 because python stats at 0 and not 1
            quizProgress += 1 #adds 1 to the quiz progress so then we dont run out of questions
            questions[quizProgress].displayQuestion()
        else:
            endScreen() #game is over
    #print(button)

"""
The function which welcomes the user with their username
"""
def start():
    global userName
    app.removeAllWidgets()
    welcomeString = "Welcome "+str(userName) #makes the username a string
    app.addLabel("welcome", welcomeString, 0, 0) #coardinates on the grid
    app.setLabelFg("welcome", "white")
    app.addButton("Start",buttonFunctions)
   
"""
The end screen is the screen shown at the end of the game
"""
def endScreen():
    app.removeAllWidgets() 
    app.addLabel("finish","The quiz is over, your score has been printed below")
    app.setLabelFg("finish", "white")
    scoreString = str(score) +" / " +str(len(questions)) #score out of how many questions
    app.addLabel("score",scoreString) 
    app.setLabelFg("score", "white")
 
# create a GUI variable called Environment Quiz
app = gui("Environment Quiz", "800x400") #gives the tab a title and the size its limited to
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
questions.append(Question("What percentage of plastic is recycled?",["8.4%","20.3%","29.6%","46.7%"],"A"))
questions.append(Question("How much waste goes to landfill in NZ per year?",["250 thousand tonnes","750 thousand tonnes","2.5 million tonnes","3.75 million tonnes"],"C"))
questions.append(Question("How many differing marine species are harmed by plastic?",["693","942","1371","1965"],"A"))
questions.append(Question("How many marine mammals die every year from plastic polution?",["50,000","100,000","150,000","200,000"],"B"))
questions.append(Question("How long does it take plastic to decompose?",["100 years","1000 years","10,000 years","1 million years"],"B"))
questions.append(Question("What country puts the most plastic in the ocean?",["China","Russia","United States","Australia"],"A"))
questions.append(Question("What is the most common debris that litters our ocean?",["Plastic bottles","Plastic bags","Food packaging","Ciggarettes"],"D"))
questions.append(Question("What day is Earth day?",["February 12","April 22","June 9","October 17"],"B"))
questions.append(Question("Where does the majority of plastic waste end up?",["Recycled","Landfilled","Burned","Oceans"],"D"))
questions.append(Question("How many drinking straws worldwide do we use per day?",["5 milion","50 million","500 million","5 billion"],"C"))

# start the GUI
app.go()

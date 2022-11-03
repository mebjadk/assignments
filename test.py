import random
import tkinter
from tkinter import *
import time
#Creating window for GUI using tkinter python package
#cutomize property related to root window
root = tkinter.Tk()
root.title("Charles Darwin Quiz App")
root.geometry("500x800")
root.configure(bg='blue')
##################################################
#global variable
<<<<<<< HEAD
global nextQuestion,scoreCounter
#nextQuestion is counter to track which question to display next form the listofQueston list
#scoreCounter is also  a counter to track the correct answer of the user
scoreCounter=0
=======
global nextQuestion
>>>>>>> refs/remotes/origin/quizlogic
nextQuestion =0
print(type(nextQuestion))
##########################################

#section for class 
#Using class to store quiz question. This class store question and its four option and the correct answer as its property.
class quizquestion:
    def __init__(self,question,option1,option2,option3,option4,answer):
        self.question=question
        self.option1=option1
        self.option2=option2
        self.option3=option3
        self.option4=option4
        self.answer=answer


#Each object has a question and its options and correct answer
<<<<<<< HEAD
question0= quizquestion("Which constellation is depicted on the Australian flag?",'Virgo','libra','leo','cancer','leo')
question1= quizquestion("What two animals are featured on the Australian coat of arms?",'kangaaro','squirrel','coe','snake','kangaaro')
question2= quizquestion("Who is Australia head of state?",'President','Prime Minister','Head of attorney','vice-president','prime minister')
question3= quizquestion("When is bilateral relation between Nepal and australia established?",'19 august','ram','shyam','raju','raju')
question4= quizquestion("How many Australia States and Territories are there?",'15','8','13','7','7')
question5= quizquestion("How many  States are there in Nepal?",'4','8','6','7','6')
question6= quizquestion("Who is Nepal head of state?",'President','Prime Minister','Head of attorney','vice-president','prime minister')
=======
question0= quizquestion("Which constellation is depicted on the Australian flag?",'hari','ram','shyam','raju','raju')
question1= quizquestion("What two animals are featured on the Australian coat of arms?",'hari','ram','shyam','raju','raju')
question2= quizquestion("Who is Australia head of state?",'hari','ram','shyam','raju','raju')
question3= quizquestion("When is bilateral relation between Nepal and australia established?",'hari','ram','shyam','raju','raju')
question4= quizquestion("How many Australia States and Territories are there?",'hari','ram','shyam','raju','raju')
question5= quizquestion("How many  States are there in Nepal?",'hari','ram','shyam','raju','raju')
question6= quizquestion("Who is Nepal head of state?",'hari','ram','shyam','raju','raju')
>>>>>>> refs/remotes/origin/quizlogic
question7= quizquestion("what is your name2",'hari','ram','shyam','raju','raju')
question8= quizquestion("what is your name1",'hari','ram','shyam','raju','raju')
question9= quizquestion("what is your name3",'hari','ram','shyam','raju','raju')
question10= quizquestion("what is your name4",'hari','ram','shyam','raju','raju')

#########preparing for Question Bank#################
listOfQuestionsBank=[]
listOfQuestionsBank.append(question0)
listOfQuestionsBank.append(question1)
listOfQuestionsBank.append(question2)
listOfQuestionsBank.append(question3)
listOfQuestionsBank.append(question4)
listOfQuestionsBank.append(question5)
listOfQuestionsBank.append(question6)
listOfQuestionsBank.append(question7)
listOfQuestionsBank.append(question8)
listOfQuestionsBank.append(question9)
listOfQuestionsBank.append(question10)
######################


###############################

#randomly generation 5 question from list of question bank
#random question selection from question bank.
listOfQuestions=[]
listOfQuestions=random.sample(listOfQuestionsBank,5)

###########################



#Section for functions
<<<<<<< HEAD
#finalpage functon for displaying the score and other graphics for the final page in this quiz application 
def finalpage():
    greeting = Label(
    root,
    text =listOfQuestions[nextQuestion].question,
    font=("",10,"bold"),
    )
    score = Label(
    root,
    text =scoreCounter,
    font=("",10,"bold"),
    )
    score.pack(pady=(20))
    greeting.pack(pady=(20))

#changeQuestion function is use to change the text of label(questions and options) and increase the counter if correct answer is passed
def changeQuestion(answer,label):
    global questionlabel,option1,option2,option3,option4,nextQuestion,scoreCounter
    label["state"]=ACTIVE
    time.sleep(1)
#this if blocks checks wheather the answer selected by user is correct or not
    if(listOfQuestions[nextQuestion].answer==answer):
        scoreCounter+=1
        print(scoreCounter)

#this if block is used to change the question 
    if(nextQuestion<len(listOfQuestions)-1):
        nextQuestion+=1
=======
def changeQuestion():
    global questionlabel,option1,option2,option3,option4,nextQuestion
    if(nextQuestion<len(listOfQuestions)-1):
        nextQuestion+=1
        print(nextQuestion)
>>>>>>> refs/remotes/origin/quizlogic
        questionlabel.config(text=listOfQuestions[nextQuestion].question)
        option1.config(text=listOfQuestions[nextQuestion].option1)
        option2.config(text=listOfQuestions[nextQuestion].option2)
        option3.config(text=listOfQuestions[nextQuestion].option3)
        option4.config(text=listOfQuestions[nextQuestion].option4)
<<<<<<< HEAD
    else:
        questionlabel.destroy()
        option1.destroy()
        option2.destroy()
        option3.destroy()
        option4.destroy()
        finalpage()

#function consist all the labels that is required to show the question and options for quiz question.
def displayQuestion():
    global questionlabel,option1,option2,option3,option4#questionlabel for queston option1 ,option2,option3,option4 holds options for quiz
=======
    
def displayQuestion():
    global questionlabel,option1,option2,option3,option4
>>>>>>> refs/remotes/origin/quizlogic
    questionlabel = Label(
    root,
    text =listOfQuestions[nextQuestion].question,
    font=("",10,"bold"),
    )
    questionlabel.pack(pady=(180,20))
    
    option1 = Button(
    root,
    text=listOfQuestions[nextQuestion].option1,
    height=1,
    width=16,
<<<<<<< HEAD
    activebackground='#00ff00',
    fg='blue',
    command=lambda:changeQuestion(listOfQuestions[nextQuestion].option1,option1),
=======
    command=changeQuestion,
>>>>>>> refs/remotes/origin/quizlogic
    )
    option2 = Button(
    root,
    text=listOfQuestions[nextQuestion].option2,
    height=1,
    width=16,
    activebackground='#00ff00',
    fg='blue',
    command=lambda:changeQuestion(listOfQuestions[nextQuestion].option2,option2),

    )
    option3 = Button(
    root,
    text=listOfQuestions[nextQuestion].option3,
    height=1,
    width=16,
    activebackground='#00ff00',
    fg='blue',
    command=lambda:changeQuestion(listOfQuestions[nextQuestion].option3,option3),
    )
    option4 = Button(
    root,
    text=listOfQuestions[nextQuestion].option4,
    height=1,
    width=16,
    activebackground='#00ff00',
    fg='blue',
    command=lambda:changeQuestion(listOfQuestions[nextQuestion].option4,option4))
    option1.pack(pady=(20,30))
    option2.pack(pady=(0,30))
    option3.pack(pady=(0,30))
    option4.pack()

##Function to clear the landing page 
def startGame():
    global questionlabel,option1,option2,option3,option4,nextQuestion
    inputtxt.destroy()
    labeltext.destroy()
    labelimage.destroy()
    userName.destroy()
    btnStart.destroy()
    root.configure(bg='grey')
    displayQuestion()
charlesDarwinImage=PhotoImage(file="charlesDarwin.png")

global labelimage
global labeltext
global inputtxt
global userName
global btnStart
labelimage = Label(
root,
image=charlesDarwinImage,
)
labelimage.pack()

#Label for Quiz Application Name:

labeltext = Label(
root,
text ="Charles Darwin Quiz App",
font=("",20,"bold"),
)

labeltext.pack(pady=(20,0))

startGameLogo= PhotoImage(file="logo.png")

userName = Label(
    root,
    text ="Your Name",
    font=("",15,"bold"),
)
userName.pack(pady=(20,0))

inputtxt=Text(
    root,
    height=2,
    width=18
)
inputtxt.pack()

btnStart = Button(
    root,
    image=startGameLogo,
    # text="Start",
    height=40,
    width=180,
    command=startGame,
)
btnStart.pack(pady=20)

root.mainloop()
<<<<<<< HEAD
=======
# #creating a list of objects of question so it can easily accessed when necessary


# #scoreCounter is to measure the score of the students.
# scoreCounter=0

# #randomly generation 5 question from list of question bank
# listOfQuestions=[]
# listOfQuestions=random.sample(listOfQuestionsBank,5)
# #this part will display the question to the user
# for i in listOfQuestions:
#     print(i.question)
#     print(i.option1)
#     print(i.option2)
#     print(i.option3)
#     print(i.option4)


# #user answer for the question
#     usesInput=input("Enter Correct Answer:")


# #this if condition checks the answer of the user.
#     if(usesInput==i.answer):
#         scoreCounter=scoreCounter+1
#         print("correct answers")
#     print(scoreCounter)
>>>>>>> refs/remotes/origin/quizlogic




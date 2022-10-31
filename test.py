import random
import tkinter
from tkinter import *
#Creating window for GUI using tkinter python package
#cutomize property related to root window
root = tkinter.Tk()
root.title("Charles Darwin Quiz App")
root.geometry("500x800")
root.configure(bg='blue')
##################################################
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
question0= quizquestion("Which constellation is depicted on the Australian flag?",'hari','ram','shyam','raju','raju')
question1= quizquestion("What two animals are featured on the Australian coat of arms?",'hari','ram','shyam','raju','raju')
question2= quizquestion("Who is Australia head of state?",'hari','ram','shyam','raju','raju')
question3= quizquestion("When is bilateral relation between Nepal and australia established?",'hari','ram','shyam','raju','raju')
question4= quizquestion("How many Australia States and Territories are there?",'hari','ram','shyam','raju','raju')
question5= quizquestion("How many  States are there in Nepal?",'hari','ram','shyam','raju','raju')
question6= quizquestion("Who is Nepal head of state?",'hari','ram','shyam','raju','raju')
question7= quizquestion("what is your name",'hari','ram','shyam','raju','raju')
question8= quizquestion("what is your name",'hari','ram','shyam','raju','raju')
question9= quizquestion("what is your name",'hari','ram','shyam','raju','raju')
question10= quizquestion("what is your name",'hari','ram','shyam','raju','raju')


#Section for functions
def displayQuestion():
    questionlabel = Label(
    root,
    text =question0.question,
    font=("",10,"bold"),
    )
    questionlabel.pack(pady=(180,20))
    
    option1 = Button(
    root,
    text=question0.option1,
    height=1,
    width=16,
    )
    option2 = Button(
    root,
    text=question0.option2,
    height=1,
    width=16,
    )
    option3 = Button(
    root,
    text=question0.option3,
    height=1,
    width=16,
    )
    option4 = Button(
    root,
    text=question0.option4,
    height=1,
    width=16,
    )
    option1.pack(pady=(20,30))
    option2.pack(pady=(0,30))
    option3.pack(pady=(0,30))
    option4.pack()

def startGame():
    inputtxt.destroy()
    labeltext.destroy()
    labelimage.destroy()
    userName.destroy()
    btnStart.destroy()
    displayQuestion()
    root.configure(bg='grey')

#Logo  charlesDarwin university for attractive front end
#Disclaimer Logo are used form following site
#www.pngtree.com
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
# #creating a list of objects of question so it can easily accessed when necessary
# listOfQuestionsBank=[]
# listOfQuestionsBank.append(question0)
# listOfQuestionsBank.append(question1)
# listOfQuestionsBank.append(question2)
# listOfQuestionsBank.append(question3)
# listOfQuestionsBank.append(question4)
# listOfQuestionsBank.append(question5)
# listOfQuestionsBank.append(question6)
# listOfQuestionsBank.append(question7)
# listOfQuestionsBank.append(question8)
# listOfQuestionsBank.append(question9)
# listOfQuestionsBank.append(question10)


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




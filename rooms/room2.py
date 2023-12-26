#ROOM 2
import random
import sys
sys.path.append('../Projekt')
import access_data as ad
from main import health



def pinfindNum1(health, set1):
    print("In order to get the 1st number of the PIN, you must answer a set of questions.")      
    questions = ad.loadData("data\\room2")["SET1"]["questions"]
    answers = ad.loadData("data\\room2")["SET1"]["answers"]
    for index,q in enumerate(questions):
        correct_answer = answers[index]
        print(q)
        user_answer = input("Please enter in your answer: ").lower() 
        if user_answer == correct_answer: 
            print("Correct!") 
        else:
            print("Wrong!")
            health -= 5
            print("Your current health is", health)
    menu()
  

def pinfindNum2(health, pinNum):
     print("In order to get the 2nd number of the PIN, you must answer a set of questions.")


def pinfindNum3(health, pinNum):
    print("In order to get the 3rd number of the PIN, you must answer a set of questions.")


def pinfindNum4(health, pinNum):
    print("In order to get the 4th number of the PIN, you must answer a set of questions.")



def menu():
    pinNumMap = {
        1:pinfindNum1,
        2:pinfindNum2,
        3:pinfindNum3,
        4:pinfindNum4
    }
    pinNum = ['?','?','?','?']
    print(f"To get out of this room, you must find the missing numbers for this PIN number: {''.join(pinNum)}")
    pinSelector = random.randint(1,4)
    pinNumMap[pinSelector](health,pinNum)

    
#no i already tested it it shows the question marks and 2 , but the menu displays the old list


menu()
#theere is no error its by mistake
#bro what ru doing

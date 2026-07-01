import mysql.connector
db =mysql.connector.connect(host='localhost',user='root',password='1234',database='project1')

cr = db.cursor()

totalmarks = 0
correct = 0
incorrect = 0

def grade():
    if totalmarks >= 17:
        print("Grade A")
    elif 13 <= totalmarks < 17:
        print("Grade B")
    elif 9 <= totalmarks < 13:
        print("Grade C")
    elif totalmarks < 9:
        print("Grade D")
    else:
        print("Fail")
        #print()
                
def percentage():
    print("Percentage of marks obtained:", (totalmarks / 20) * 100)

def invigilator():
    print("Exam starts now....")
    cr.execute("SELECT * FROM exam")
    result = cr.fetchall()
    for i in result:
        print("Question:", i[1])
        print("OptionA:", i[2])
        print("OptionB:", i[3])
        print("OptionC:", i[4])
        print("OptionD:", i[5])
        answer = input("Enter your answer (A/B/C/D): ").capitalize()
        
        if answer == i[6]:
            global totalmarks
            totalmarks += 2
            global correct
            correct += 1
            percentage()  
            #grade()   

        elif answer != i[6]:
            global incorrect
            incorrect += 1
            print("Incorrect answer.")
    print("Total marks obtained:", totalmarks)
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
#____________________________________________________________________________________

username = input("Enter your username: ")
password = input("Enter your password: ")
adminid = input("Enter your admin ID: ") 

choice = input("Enter your choice y/n : ")
if choice == 'y' or choice == 'Y':
    #print("Exam starts now....")
    #print("select * from exam")
    #cr.execute("SELECT * FROM exam")
    #result = cr.fetchall()
    invigilator() 
    
elif choice == 'n' or choice == 'N':
    print("Exiting the exam")
    exit()
else:
    print("Invalid choice. Please enter 'y' or 'n'.")    
                  
         
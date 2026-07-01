import mysql.connector
db = mysql.connector.connect( host='localhost',user='root',password='1234',database='project1')

cr = db.cursor()

totalmarks = 0
correct = 0
incorrect = 0
#admin_username = "admin"
#admin_password = "admin123"

def studentlist():
    cr.execute("select * from studentids")
    allstudent = cr.fetchall()
    for i in allstudent:
        print("Username", i[0])
        print("Password", i[1])
        print("Student ID", i[2])

def info():
    #cr.execute("select * from studentids")
    #biodata =cr.fetchall()
    #for i in biodata:
        #print("Name:", i[2])
    print("Enter your details here")    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    studentid = input("Enter your student ID: ")
    cr.execute("insert into studentids (username, password, studentid) values (%s, %s, %s)", (username, password, studentid))
    db.commit()
    print("Student Info added successfully")

def grade():
    if totalmarks >= 17:
        print("Grade A")
    elif 13 <= totalmarks < 17:
        print("Grade B")
    elif 9 <= totalmarks < 13:
        print("Grade C")
    elif 5<= totalmarks < 9:
        print("Grade D")
    else:
        print("Fail")

def percentage():
    print("Percentage of marks obtained:", (totalmarks / 20) * 100)

def invigilator():
    #print("Exam starts now....")
    cr.execute("SELECT * FROM exam")
    result = cr.fetchall()
    for i in result:
        print("Question:", i[1])
        print("OptionA:", i[2])
        print("OptionB:", i[3])
        print("OptionC:", i[4])
        print("OptionD:", i[5])
        answer = input("Enter your answer (A/B/C/D): ").capitalize()

        global totalmarks, correct, incorrect
        if answer == i[6]:
            totalmarks += 2
            correct += 1
        else:
            incorrect += 1
            #print("Incorrect answer.")
    print("Exam finished")
    print("Total Marks:", totalmarks)
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    grade()
    percentage()

def admin_access():
    while True:
        print("Admin Access Granted")
        print("1 View All Questions")
        print("2 Add New Question")
        print("3 Delete a Question")
        print("4 Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            cr.execute("SELECT * FROM exam")
            for i in cr.fetchall():
                print(i)

        elif choice == '2':
            question = input("Enter question: ")
            optA = input("Option A: ")
            optB = input("Option B: ")
            optC = input("Option C: ")
            optD = input("Option D: ")
            correct_ans = input("Correct answer (A/B/C/D): ").capitalize()

            cr.execute("INSERT INTO exam (question, optionA, optionB, optionC, optionD, answer) VALUES (%s, %s, %s, %s, %s, %s)",
                       (question, optA, optB, optC, optD, correct_ans))
            db.commit()
            print("Question added successfully")

        elif choice == '3':
            qid = input("Enter question ID to delete: ")
            cr.execute("DELETE FROM exam WHERE id = %s", (qid,))
            db.commit()
            print("Question deleted")

        elif choice == '4':
            print("Exiting Admin Panel")
            break

        else:
            print("Invalid choice")
#===================================================================================            
print("press 1 for student login : ")
print("press 2 for admin login : ")
print("press 3 for adding student information / viewing student list")
print("press 4 to exit")

n= int(input("Enter your choice: "))
if n == 1 :
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    cr.execute("SELECT * FROM studentids WHERE username = %s AND password = %s", (username, password))
    result = cr.fetchall()
    #print(result)
    for i in result:
        report = print("Student ID:",i[2])
        if i[1] == username and i[3] == password:
            print("Your Student ID is:", i[2])
            #print("Now you can give the exam")
        invigilator()
    #print("Invalid username or password")

elif n == 2 : 
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")
    cr.execute("SELECT * FROM adminids WHERE username = %s AND password = %s", (admin_username, admin_password))
    cr.fetchall()
    admin_access()

elif n == 3:
    options = input("choose appropiate option (studentlist/info): ").lower()
    if options == "studentlist":
        studentlist()
    elif options == "info":
        info()

elif n == 4:
    print("Exiting the exam")
    exit()

else:
    print("Invalid input")

"""student1  st01  ashwinee  //   admin1  ad01  admin"""    
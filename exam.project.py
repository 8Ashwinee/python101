import mysql.connector
import hashlib
import time
import sys

# Database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='project1'
)
cr = db.cursor()

# Global variables
totalmarks = 0
correct = 0
incorrect = 0

# ------------------ Utility Functions ------------------

def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def pause():
    input("\nPress Enter to continue...")

# ------------------ User Management ------------------

def register_student():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    hashed = hash_password(password)
    cr.execute("INSERT INTO students (username, password) VALUES (%s, %s)", (username, hashed))
    db.commit()
    print("Student registered successfully!")

def login_student():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed = hash_password(password)
    cr.execute("SELECT * FROM students WHERE username=%s AND password=%s", (username, hashed))
    result = cr.fetchone()
    if result:
        print("Login successful! Welcome,", username)
        return True
    else:
        print("Invalid credentials.")
        return False

def login_admin():
    adminid = input("Enter admin ID: ")
    password = input("Enter admin password: ")
    hashed = hash_password(password)
    cr.execute("SELECT * FROM admin WHERE adminid=%s AND password=%s", (adminid, hashed))
    result = cr.fetchone()
    if result:
        print("Admin login successful!")
        return True
    else:
        print("Invalid admin credentials.")
        return False

# ------------------ Exam Functions ------------------

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

def percentage():
    print("Percentage of marks obtained:", (totalmarks / 20) * 100)

def invigilator():
    global totalmarks, correct, incorrect
    print("Exam starts now....")
    cr.execute("SELECT * FROM exam ORDER BY RAND()")  # randomize questions
    result = cr.fetchall()
    start_time = time.time()

    for i in result:
        print("\nQuestion:", i[1])
        print("A:", i[2], " B:", i[3], " C:", i[4], " D:", i[5])
        answer = input("Enter your answer (A/B/C/D): ").capitalize()

        if answer == i[6]:
            totalmarks += 2
            correct += 1
            print("Correct!")
        else:
            incorrect += 1
            print("Incorrect.")

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    print("\nExam Finished!")
    print("Total marks obtained:", totalmarks)
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Time taken:", duration, "seconds")
    percentage()
    grade()

    # Save results
    cr.execute("INSERT INTO results (marks, correct, incorrect, duration) VALUES (%s,%s,%s,%s)",
               (totalmarks, correct, incorrect, duration))
    db.commit()

# ------------------ Admin Functions ------------------

def add_question():
    q = input("Enter question: ")
    a = input("Option A: ")
    b = input("Option B: ")
    c = input("Option C: ")
    d = input("Option D: ")
    ans = input("Correct answer (A/B/C/D): ").capitalize()
    cr.execute("INSERT INTO exam (question, optionA, optionB, optionC, optionD, answer) VALUES (%s,%s,%s,%s,%s,%s)",
               (q, a, b, c, d, ans))
    db.commit()
    print("Question added successfully!")

def delete_question():
    qid = input("Enter question ID to delete: ")
    cr.execute("DELETE FROM exam WHERE id=%s", (qid,))
    db.commit()
    print("Question deleted successfully!")

def view_results():
    cr.execute("SELECT * FROM results ORDER BY marks DESC")
    rows = cr.fetchall()
    print("\nLeaderboard:")
    for r in rows:
        print("Marks:", r[1], "| Correct:", r[2], "| Incorrect:", r[3], "| Time:", r[4])

# ------------------ Main Menu ------------------

def main_menu():
    while True:
        print("\n--- Exam Management System ---")
        print("1. Student Login")
        print("2. Student Registration")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            if login_student():
                invigilator()
        elif choice == '2':
            register_student()
        elif choice == '3':
            if login_admin():
                while True:
                    print("\n--- Admin Menu ---")
                    print("1. Add Question")
                    print("2. Delete Question")
                    print("3. View Results")
                    print("4. Logout")
                    ch = input("Enter choice: ")
                    if ch == '1':
                        add_question()
                    elif ch == '2':
                        delete_question()
                    elif ch == '3':
                        view_results()
                    elif ch == '4':
                        break
        elif choice == '4':
            print("Exiting system...")
            sys.exit()
        else:
            print("Invalid choice.")

# Run program
main_menu()

# 📝 Exam Management System (Python + MySQL)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Status](https://img.shields.io/badge/Status-Active-success)

A **Python-based Exam Management System** integrated with **MySQL**.  
This project provides a complete workflow for student login, exam invigilation, grading, and admin-level question management.

---

##  Features

###  Student Module
- Secure login using stored credentials.
- Add new student information (`info()`).
- View all registered students (`studentlist()`).
- Attempt exams with multiple-choice questions fetched from the database.
- Automatic evaluation of answers with:
  - **Total Marks**
  - **Correct/Incorrect Answers**
  - **Grade Assignment (A–Fail)**
  - **Percentage Calculation**

###  Admin Module
- Secure admin login.
- Manage exam questions:
  - View all questions.
  - Add new questions.
  - Delete existing questions.
- Full control over the exam database.

---

##  Project Structure

- **Database Connection:**  
  Uses `mysql.connector` to connect with `project1` database.

- **Functions:**  
  - `studentlist()` → Displays all registered students.  
  - `info()` → Inserts new student details into the database.  
  - `invigilator()` → Conducts exam, tracks answers, calculates marks.  
  - `grade()` → Assigns grade based on marks.  
  - `percentage()` → Calculates percentage.  
  - `admin_access()` → Admin panel for managing questions.  

- **Main Menu Options:**  
  - Student login  
  - Admin login  
  - Add/view student information  
  - Exit  

---

##  Grading System

| Marks Range | Grade |
|-------------|-------|
| ≥ 17        | A     |
| 13–16       | B     |
| 9–12        | C     |
| 5–8         | D     |
| < 5         | Fail  |

---

##  Tech Stack
- **Language:** Python  
- **Database:** MySQL  
- **Connector:** `mysql.connector`  

---

##  Example Workflow
1. Student/Admin selects login option.  
2. Credentials validated against database (`studentids` / `adminids`).  
3. Students attempt exam questions stored in `exam` table.  
4. System auto-calculates marks, grade, and percentage.  
5. Admins can add, view, or delete questions.  

---

##  ER Diagram

```mermaid
erDiagram
    STUDENTIDS {
        string username
        string password
        int studentid
    }

    ADMINIDS {
        string username
        string password
    }

    EXAM {
        int id
        string question
        string optionA
        string optionB
        string optionC
        string optionD
        string answer
    }

    STUDENTIDS ||--o{ EXAM : "attempts"
    ADMINIDS ||--o{ EXAM : "manages"

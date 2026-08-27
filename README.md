# 🎓 Student Placement Tracker

A **Python Object-Oriented Programming (OOP)** project that manages student profiles, mock scores, placement readiness, and platform information through a simple menu-driven application.

This project demonstrates important Python OOP concepts such as **classes, objects, constructors, instance variables, class variables, instance methods, static methods, class methods, properties, getters, setters, inheritance-free encapsulation, and input validation**.

## 🚀 Features

* Add new student profiles
* Prevent duplicate student IDs
* Display all registered students
* Update student mock scores
* Validate scores between `0` and `100`
* Automatically determine placement readiness
* Normalize student names
* Change the platform name
* Track the total number of students
* Create student objects directly from comma-separated strings
* Menu-driven command-line interface

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* Classes & Objects
* `@property`
* Getter & Setter
* `@staticmethod`
* `@classmethod`
* Lists
* Loops
* Conditional Statements
* String Manipulation
* Input Validation

## 📂 Project Structure

```text
Student-Placement-Tracker/
│
├── main.py
└── README.md
```

## 🧠 OOP Concepts Demonstrated

### 1. Class

The main class used in the project is:

```python
class StudentProfile:
```

It represents a student's profile.

### 2. Constructor

The `__init__()` method initializes student information:

```python
def __init__(self, student_id, name, branch, score):
    self.student_id = student_id
    self.name = name
    self.branch = branch
    self._score = score
```

### 3. Class Variables

The application uses class variables to store common information:

```python
platform = "KodNest"
total_students = 0
```

`total_students` is automatically increased whenever a new student is created.

### 4. Property, Getter & Setter

The score is accessed using a property:

```python
@property
def score(self):
    return self._score
```

The setter validates the new score before updating it:

```python
@score.setter
def score(self, new_score):
    if StudentProfile.is_valid_score(new_score):
        self._score = new_score
```

This demonstrates **encapsulation** and controlled access to data.

### 5. Static Method

The project uses a static method to validate scores:

```python
@staticmethod
def is_valid_score(score):
    return 0 <= score <= 100
```

Another static method normalizes names:

```python
@staticmethod
def normalize_name(name):
    return name.strip().title()
```

### 6. Instance Method

The `get_placement_status()` method determines whether a student is ready for placement:

| Score  | Status              |
| ------ | ------------------- |
| 80–100 | Placement Ready     |
| 60–79  | Needs More Practice |
| 0–59   | Not Ready           |

### 7. Class Method

The `from_string()` class method creates a student object from comma-separated input:

```text
101, subham nayak, Computer Science, 85
```

It converts the input into a `StudentProfile` object.

The `change_platform()` method allows the platform name to be changed for all students.

## 📋 Menu Options

When the program starts, the following menu is displayed:

```text
===== Student Placement Tracker =====
1. Add Student
2. Display All Students
3. Update Student Score
4. Change Platform
5. Show Total Students
6. Exit
```

### Option 1 – Add Student

Enter student details in this format:

```text
101, subham nayak, Computer Science, 85
```

The program checks whether the student ID already exists.

### Option 2 – Display All Students

Displays information such as:

```text
Student ID: 101
Name: Subham Nayak
Branch: Computer Science
Mock Score: 85
Placement Status: Placement Ready
Platform: KodNest
```

### Option 3 – Update Student Score

The user can update a student's mock score.

Only scores between `0` and `100` are accepted.

Example:

```text
Student ID: 101
New Score: 92
```

Output:

```text
Score updated successfully.
Updated Score: 92
Updated Status: Placement Ready
```

### Option 4 – Change Platform

The platform name can be changed:

```text
Enter the new platform name: CodeNest
```

### Option 5 – Show Total Students

Displays the total number of students created:

```text
Total Students: 3
```

### Option 6 – Exit

Terminates the application.

## ▶️ How to Run

### Step 1: Clone the repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the project directory

```bash
cd Student-Placement-Tracker
```

### Step 3: Run the Python program

```bash
python student_placement_tracker.py
```

If your system uses `python3`:

```bash
python3 student_placement_tracker.py
```

## 💡 Example

### Input

```text
1
101, subham nayak, Computer Science, 85
2
5
6
```

### Output

```text
Student added successfully.

Student ID: 101
Name: Subham Nayak
Branch: Computer Science
Mock Score: 85
Placement Status: Placement Ready
Platform: KodNest

Total Students: 1

Thank you for using the Student Placement Tracker.
```

## 🔒 Validation

The project includes several validations:

* Student IDs must be unique.
* Scores must be between `0` and `100`.
* Invalid scores are rejected.
* Previous scores remain unchanged when an invalid score is entered.
* Student names are automatically cleaned and formatted.
* Empty student lists are handled with a message.

## 📚 Learning Outcomes

Through this project, you can practice:

* Understanding Python classes and objects
* Using constructors with `__init__()`
* Understanding instance vs. class variables
* Implementing getters and setters
* Using properties for encapsulation
* Understanding static methods
* Understanding class methods
* Creating objects from formatted strings
* Working with lists of objects
* Implementing validation
* Building menu-driven Python applications

## 🔮 Future Improvements

Possible improvements include:

* Search students by ID
* Delete a student profile
* Update student branch
* Store data permanently using a file or database
* Add login/authentication
* Add placement company information
* Generate placement reports
* Add a graphical user interface
* Connect the application to MySQL

## 👨‍💻 Author

**Subham Nayak**

This project was created as part of Python and Object-Oriented Programming practice.

## ⭐ Conclusion

The **Student Placement Tracker** is a beginner-friendly Python OOP project designed to demonstrate how different OOP concepts can work together in a practical application.

It provides a foundation for building larger **student management, placement management, and career-tracking applications** using Python.

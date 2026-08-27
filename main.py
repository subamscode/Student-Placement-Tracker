class StudentProfile:
    # Class variables
    platform = "KodNest"
    total_students = 0

    # Constructor
    def __init__(self, student_id, name, branch, score):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self._score = score

        StudentProfile.total_students += 1

    # Score getter
    @property
    def score(self):
        return self._score

    # Score setter
    @score.setter
    def score(self, new_score):
        if StudentProfile.is_valid_score(new_score):
            self._score = new_score
        else:
            print("Invalid score. Score must be between 0 and 100.")

    # Static method: Validate score
    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

    # Static method: Normalize name
    @staticmethod
    def normalize_name(name):
        return name.strip().title()

    # Instance method: Placement status
    def get_placement_status(self):
        if 80 <= self.score <= 100:
            return "Placement Ready"
        elif 60 <= self.score <= 79:
            return "Needs More Practice"
        else:
            return "Not Ready"

    # Instance method: Display profile
    def display_profile(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Mock Score:", self.score)
        print("Placement Status:", self.get_placement_status())
        print("Platform:", self.platform)

    # Class method: Create object from string
    @classmethod
    def from_string(cls, data):
        student_id, name, branch, score = data.split(",")

        student_id = student_id.strip()
        name = cls.normalize_name(name)
        branch = branch.strip()
        score = int(score.strip())

        return cls(student_id, name, branch, score)

    # Class method: Change platform
    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform.strip()

    # Class method: Show total students
    @classmethod
    def show_total_students(cls):
        print("Total Students:", cls.total_students)


#  Main Program Management


students = []

while True:
    print("\n===== Student Placement Tracker =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Score")
    print("4. Change Platform")
    print("5. Show Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    
    # Option 1: Add Student
    
    if choice == "1":
        student_data = input("Enter student details: ")

        # Extract student ID
        student_id = student_data.split(",")[0].strip()

        # Check duplicate ID
        id_exists = False

        for student in students:
            if student.student_id == student_id:
                id_exists = True
                break

        if id_exists:
            print("Student ID already exists.")
        else:
            # Create object using from_string()
            student = StudentProfile.from_string(student_data)

            # Add object to list
            students.append(student)

            print("Student added successfully.")

    # Option 2: Display All Students
    
    elif choice == "2":
        if students:
            for student in students:
                student.display_profile()
                print()
        else:
            print("No students found.")

    
    # Option 3: Update Student Score

    elif choice == "3":
        student_id = input("Student ID: ").strip()
        new_score = int(input("New Score: "))

        student_found = False

        for student in students:
            if student.student_id == student_id:
                student_found = True

                # Validate before updating
                if StudentProfile.is_valid_score(new_score):
                    # Update using property
                    student.score = new_score

                    print("Score updated successfully.")
                    print("Updated Score:", student.score)
                    print("Updated Status:", student.get_placement_status())
                else:
                    # Previous score remains unchanged
                    print("Invalid score. Score must be between 0 and 100.")

                break

        if not student_found:
            print("Student not found.")


    # Option 4: Change Platform

    elif choice == "4":
        new_platform = input("Enter the new platform name: ")

        StudentProfile.change_platform(new_platform)

        print("Platform changed successfully.")

    # Option 5: Show Total Students
    elif choice == "5":
        StudentProfile.show_total_students()


    # Option 6: Exit
    
    elif choice == "6":
        print("Thank you for using the Student Placement Tracker.")
        break

 
    # Invalid Choice

    else:
        print("Invalid choice. Please select an option from 1 to 6.")

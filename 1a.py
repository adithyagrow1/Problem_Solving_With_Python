name = input("Enter students name :")
usn = input ("enter student USN:")
marks1 = float (input ("enter marks in subject 1 (out of 100):"))
marks2 = float (input ("enter marks in subject 2 (out of 100):"))
marks3 = float (input ("enter marks in subject 3 (out of 100):"))

def calculate_total():
    return marks1 + marks2 + marks3
def calculated_percentage():
        total_marks = 300
        return (calculate_total()/total_marks)*100
def display_student_details():
    print(f"\nstudent Details:")
    print(f"Name:{name}")
    print(f"USN:{usn}")

    print(f"")



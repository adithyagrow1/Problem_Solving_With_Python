class Student:

    def init(self,name,usn):
        self.name = name
        self.usn = usn
        self.marks = []
        self.total_marks = 0

    def getMarks(self):
        """Reads marks for three subjects and calculates total."""
        for i in range(3):
            mark = float(input(f"Enter marks for subject {i+1}:"))
            self.marks.append(mark)
        self.total_marks = sum(self.marks)

    def calculatePercentage(selfself):
        """Calculates percentage based on total marks."""
        return(self.total_marks / 300)*100

    def display(selfself):
        """Displays student details, marks, total, and percentage."""
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"USN: {self.usn}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.total_marks}")
        print(f"Percentage: {self.calculatePercentage():.2f}%")
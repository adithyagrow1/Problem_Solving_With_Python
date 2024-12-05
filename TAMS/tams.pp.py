import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    contact TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER,
    date TEXT NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Leave')),
    FOREIGN KEY (teacher_id) REFERENCES Teachers (id)
)
""")

conn.commit()
print("Database setup complete.")

'add a teacher'
def add_teacher(name, department, contact):
    cursor.execute("""
    INSERT INTO Teachers (name, department, contact) 
    VALUES (?, ?, ?)
    """, (name, department, contact))
    conn.commit()
    print("Teacher added successfully.")

'mark attendance'
def mark_attendance(teacher_id, date, status):
    cursor.execute("""
    INSERT INTO Attendance (teacher_id, date, status) 
    VALUES (?, ?, ?)
    """, (teacher_id, date, status))
    conn.commit()
    print("Attendance marked successfully.")

'view attendance'
def view_attendance(teacher_id):
    cursor.execute("""
    SELECT date, status FROM Attendance 
    WHERE teacher_id = ? 
    ORDER BY date
    """, (teacher_id,))
    records = cursor.fetchall()
    for record in records:
        print(f"Date: {record[0]}, Status: {record[1]}")

'generate report'
def generate_report():
    cursor.execute("""
    SELECT T.name, T.department, A.date, A.status 
    FROM Teachers T 
    JOIN Attendance A ON T.id = A.teacher_id
    """)
    records = cursor.fetchall()
    for record in records:
        print(f"Name: {record[0]}, Department: {record[1]}, Date: {record[2]}, Status: {record[3]}")

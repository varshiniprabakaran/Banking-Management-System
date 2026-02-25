#------------STUDENT MANAGEMENT SYSTEM------------------#

students = {}

# ---------------- ADD STUDENT ----------------
def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")

    marks = []
    subjects = ["Tamil", "English", "Maths", "Science", "Social"]

    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    attendance = int(input("Enter Attendance Percentage: "))

    students[roll_no] = {
        "name": name,
        "marks": marks,
        "attendance": attendance
    }

    print("Student added successfully!")


# ---------------- UPDATE MARKS ----------------
def update_marks():
    print("\n--- Update Marks ---")
    roll_no = input("Enter Roll Number: ")

    if roll_no not in students:
        print("Student not found!")
        return

    marks = []
    subjects = ["Tamil", "English", "Maths", "Science", "Social"]

    for subject in subjects:
        mark = int(input(f"Enter new marks for {subject}: "))
        marks.append(mark)

    students[roll_no]["marks"] = marks
    print("Marks updated successfully!")


# ---------------- UPDATE ATTENDANCE ----------------
def update_attendance():
    print("\n--- Update Attendance ---")
    roll_no = input("Enter Roll Number: ")

    if roll_no not in students:
        print("Student not found!")
        return

    attendance = int(input("Enter new attendance percentage: "))
    students[roll_no]["attendance"] = attendance

    print("Attendance updated successfully!")


# ---------------- CALCULATIONS ----------------
def calculate_result(marks):
    total = sum(marks)
    average = total / 5

    if min(marks) < 40:
        result = "Fail"
    else:
        result = "Pass"

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    return total, average, grade, result


# ---------------- STUDENT REPORT ----------------
def view_report():
    print("\n--- Student Report ---")
    roll_no = input("Enter Roll Number: ")

    if roll_no not in students:
        print("Student not found!")
        return

    student = students[roll_no]
    marks = student["marks"]

    total, average, grade, result = calculate_result(marks)

    print("\n------ REPORT ------")
    print("Roll No :", roll_no)
    print("Name    :", student["name"])
    print("Marks   :", marks)
    print("Total   :", total)
    print("Average :", average)
    print("Grade   :", grade)
    print("Result  :", result)

    if student["attendance"] >= 75:
        print("Attendance : Eligible")
    else:
        print("Attendance : Not Eligible")

    print("--------------------")


# ---------------- VIEW ALL STUDENTS ----------------
def view_all_students():
    print("\n--- All Students ---")

    if not students:
        print("No students available!")
        return

    for roll_no, student in students.items():
        print(roll_no, "-", student["name"])


# ---------------- RANK LIST ----------------
def rank_list():
    print("\n--- Rank List ---")

    if not students:
        print("No students available!")
        return

    totals = []

    for roll_no, student in students.items():
        total = sum(student["marks"])
        totals.append((roll_no, student["name"], total))

    totals.sort(key=lambda x: x[2], reverse=True)

    rank = 1
    for data in totals:
        print(f"Rank {rank}: {data[1]} (Roll No: {data[0]}) - Total: {data[2]}")
        rank += 1


# ---------------- DELETE STUDENT ----------------
def delete_student():
    print("\n--- Delete Student ---")
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


# ---------------- MAIN MENU ----------------
def main_menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Update Attendance")
        print("4. View Student Report")
        print("5. View All Students")
        print("6. Rank List")
        print("7. Delete Student")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_marks()
        elif choice == "3":
            update_attendance()
        elif choice == "4":
            view_report()
        elif choice == "5":
            view_all_students()
        elif choice == "6":
            rank_list()
        elif choice == "7":
            delete_student()
        elif choice == "8":
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid choice! Try again.")


main_menu()

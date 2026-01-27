import os

DATA_FILE = "students.txt"
LOG_FILE = "log.txt"


def write_log(message):
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")


def add_student():
    stu_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")

    with open(DATA_FILE, "a") as f:
        f.write(f"{stu_id},{name},{course}\n")

    write_log(f"ADD : Student ID {stu_id} added")
    print("Student added successfully!")


def view_students():
    if not os.path.exists(DATA_FILE):
        print("No student records found!")
        write_log("VIEW : No student records found")
        return

    with open(DATA_FILE, "r") as f:
        data = f.read()

    print("\n=== All Students ===")
    print(data)
    write_log("VIEW : Viewed all student records")


def search_student():
    stu_id = input("Enter Student ID to search: ")

    if not os.path.exists(DATA_FILE):
        print("No data found!")
        write_log("SEARCH : File not found")
        return

    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.startswith(stu_id + ","):
                print("Record Found:", line)
                write_log(f"SEARCH : Student ID {stu_id} found")
                return

    print("Student not found!")
    write_log(f"SEARCH : Student ID {stu_id} not found")


def delete_student():
    stu_id = input("Enter Student ID to delete: ")

    if not os.path.exists(DATA_FILE):
        print("No data found!")
        write_log("DELETE : File not found")
        return

    with open(DATA_FILE, "r") as f:
        lines = f.readlines()

    found = False

    with open(DATA_FILE, "w") as f:
        for line in lines:
            if line.startswith(stu_id + ","):
                found = True
                continue
            f.write(line)

    if found:
        print("Student deleted successfully!")
        write_log(f"DELETE : Student ID {stu_id} deleted")
    else:
        print("Student ID not found. No records deleted.")
        write_log(f"DELETE : Student ID {stu_id} not found")


def menu():
    write_log("SYSTEM STARTED")

    while True:
        print("\n-=-== Student Registration System ==-=-")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        else:
            write_log("SYSTEM EXITED")
            break


menu()

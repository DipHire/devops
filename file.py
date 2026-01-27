filename = "hello.txt"

def create_file():
    f = open(filename, "w")
    f.close()


def write_file():
    f = open(filename, "w")
    data = input("Enter data to write: ")
    f.write(data)
    f.close()


def read_file():
    f = open(filename, "r")
    print("\nFile Content:\n")
    print(f.read())
    f.close()


def append_file():
    f = open(filename, "a")
    data = input("Enter data to append: ")
    f.write("\n" + data)
    f.close()


def read_lines():
    f = open(filename, "r")
    lines = f.readlines()
    for i in range(len(lines)):
        print(i, ":", lines[i])
    f.close()


while True:
    print("\n===== FILE HANDLING MENU =====")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Append File")
    print("5. Read File Line by Line")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_file()
    elif choice == 2:
        write_file()
    elif choice == 3:
        read_file()
    elif choice == 4:
        append_file()
    elif choice == 5:
        read_lines()
    elif choice == 6:
        print("Exited from the code :)")
        break
    else:
        print("Enter correct choice")

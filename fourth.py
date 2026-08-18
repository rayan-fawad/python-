filename = "students.txt"


# ================= ADD STUDENT =================
def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    behaviour = input("Enter Behaviour: ")
    skill = input("Enter skill:")

    # check duplicate roll
    with open(filename, "r") as file:
        data = file.read()
        if f"Roll: {roll}" in data:
            print("Student already exists with this roll number!")
            return

    with open(filename, "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Roll: {roll}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Marks: {marks}\n")
        file.write(f"Behaviour: {behaviour}\n")
        file.write(f"skill: {skill}\n")
        file.write("----------------\n")

    print("Student Added Successfully!")


# ================= VIEW STUDENTS =================
def view_students():
    try:
        with open(filename, "r") as file:
            data = file.read()

        if data == "":
            print("No students found!")
        else:
            print("\n===== ALL STUDENTS =====\n")
            print(data)

    except FileNotFoundError:
        print("No file found!")


# ================= SEARCH STUDENT =================
def search_student():
    roll = input("Enter Roll No to Search: ")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        found = False

        for i in range(len(lines)):
            if lines[i].startswith("Roll:") and lines[i].split(":")[1].strip() == roll:
                print("\nStudent Found:\n")

                print(lines[i-1].strip())
                print(lines[i].strip())
                print(lines[i+1].strip())
                print(lines[i+2].strip())
                print(lines[i+3].strip())

                found = True
                break

        if not found:
            print("Student not found!")

    except FileNotFoundError:
        print("File not found!")


# ================= REMOVE STUDENT =================
def remove_student():
    roll = input("Enter Roll No to Remove: ")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        new_data = []
        skip = False

        for line in lines:
            if line.startswith("Roll:") and line.split(":")[1].strip() == roll:
                 new_data.pop() if new_data else None
                 skip = True
                 continue

            if skip and line.strip() == "----------------":
                skip = False
                continue

            if not skip:
                new_data.append(line)
       
        with open(filename, "w") as file:
            file.writelines(new_data)

        print("Student Removed Successfully!")

    except FileNotFoundError:
        print("File not found!")


# ================= UPDATE STUDENT =================
def update_student():
    roll = input("Enter Roll No to Update: ")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        updated_lines = []
        i = 0

        while i < len(lines):
            if lines[i].startswith("Roll:") and lines[i].split(":")[1].strip() == roll:
                print("Enter new details (leave blank to keep old value):")

                name = input("New Name: ")
                new_roll = input("New Roll: ")
                age = input("New Age: ")
                marks = input("New Marks: ")
                behaviour = input("New Behaviour: ")

                updated_lines.append(f"Name: {name if name else lines[i-1].split(':')[1].strip()}\n")
                updated_lines.append(f"Roll: {new_roll if new_roll else roll}\n")
                updated_lines.append(f"Age: {age if age else lines[i+1].split(':')[1].strip()}\n")
                updated_lines.append(f"Marks: {marks if marks else lines[i+2].split(':')[1].strip()}\n")
                updated_lines.append(f"Behaviour: {behaviour if behaviour else lines[i+3].split(':')[1].strip()}\n")

                i += 5  # skip old record
                continue

            updated_lines.append(lines[i])
            i += 1

        with open(filename, "w") as file:
            file.writelines(updated_lines)

        print("Student Updated Successfully!")

    except FileNotFoundError:
        print("File not found!")


# ================= MAIN MENU =================
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        remove_student()

    elif choice == "6":
        print("Program Ended.")
        break

    else:
        print("Invalid choice!")
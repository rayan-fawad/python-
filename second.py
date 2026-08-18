show_history = "history.txt"

def history():
    with open(show_history , "r") as file:
        data = file.read()


    if not data:
        print("no history found")

    else:
        print(data)

         


def clear():
    with open(show_history , "w") as file:
        pass

    print("History deleted successfully")    



def save_history(text):
    with open(show_history, "a") as file:
        file.write(text + "\n")    



def calculate():
    while True:
        try:
            num1 = input("Enter first number: ")

            if num1.lower() == "clear":
                clear()
                print("History cleared")
                break

            op = input("Enter operator (+, -, *, /, %): ")
            num2 = input("Enter second number: ")
            
            

            num1 = int(num1)
            num2 = int(num2)

            if op == "+":
                result = num1 + num2

            elif op == "-":
                result = num1 - num2

            elif op == "*":
                result = num1 * num2

            elif op == "/":
                if num2 == 0:
                    print("Cannot divide by zero")
                    return
                result = num1 / num2

            elif op == "%":
                result = num1 % num2

            else:
                print("Invalid operator")
                return

            print("Result =", result)

        # save history
            save_history(f"{num1} {op} {num2} = {result}")

        # ask user after saving
            ask = input("Do you want to delete history? (yes/no): ").lower()

            if ask == "yes":
                clear()

        except ValueError:
            print("Invalid input")



calculate()
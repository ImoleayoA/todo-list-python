# Simple Calculator

while True:
    try:
        firstNum = float(input("Enter first number: ").strip())
        operator = input("Enter operator from the following (+, -, *, /): ")

        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            secondNum = float(input("Enter second number: ").strip())

            if operator == "+":
                print(firstNum + secondNum)

            elif operator == "-":
                print(firstNum - secondNum)

            elif operator == "*":
                print(firstNum * secondNum)

            elif operator == "/":
                if 0 == secondNum:
                    print("Cannot divide by zero")
                else:
                    print(firstNum / secondNum)
        else:
            print("Invalid operator. Please enter an operator from the following (+, -, *, /)")

        while True:
            choice = input("Do you want to continue? (y/n) or (yes/no): ").strip().lower()
            if choice in ("y", "yes"):
                break
            elif choice in ("n", "no"):
                print("Exiting the calculator...")
                break
            else:
                print("Please enter y/n or yes/no")
        if choice in ("n", "no"):
            break

    except ValueError:
        print("Please enter a valid number")

    except(KeyboardInterrupt, EOFError):
        print("Exiting the calculator...")
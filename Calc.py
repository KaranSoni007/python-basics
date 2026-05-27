def smart_calculator():
    while True:
        print("\nSmart Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Exit")

        choice = input("\nEnter choice (1-7): ")
        if choice == "7":
            print("Exit")
            break
        if choice in ["1", "2", "3", "4", "5", "6"]:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            match int(choice):
                case 1:
                    print("Addition: ", num1 + num2)
                case 2:
                    print("Subtraction: ", num1 - num2)
                case 3:
                    print("Multiplication: ", num1 * num2)
                case 4:
                    if num2 != 0:
                        print("Division:", num1 / num2)
                    else:
                        print("Error: Division by zero is not allowed.")
                case 5:
                    print("Power:", num1**num2)
                case 6:
                    print("Modulus:", num1 % num2)
                case 7:
                    print("Exit")

        else:
            print("Invalid selection! Please choose a number between 1 and 7.")


smart_calculator()

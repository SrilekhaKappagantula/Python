print("Welcome to Arithmetic Calculator:\n")

while True:
    print("\nChoose your required Arithmetic operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Modulo")
    print("6: Exit")

    try:
        op = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if op == 6:
        print("Exiting the calculator!")
        break

    if op < 1 or op > 6:
        print("Invalid choice. Please choose a valid operation.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if op == 1:
        sum = num1 + num2
        print(num1,'+',num2,'=',sum)

    elif op == 2:
        diff = num1 - num2
        print(num1,'-',num2,'=',diff)

    elif op == 3:
        prod = num1 * num2
        print(num1,'*',num2,'=',prod)

    elif op == 4:
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            div = num1 / num2
            print(num1,'/',num2,'=',div)

    elif op == 5:
        if num2 == 0:
            print("Error! Modulo by zero is not allowed.")
        else:
            mod = num1 % num2
            print(num1,'%',num2,'=',mod)

print("Thank you for using Arithmetic Calculator!")

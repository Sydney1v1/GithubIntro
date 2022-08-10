while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("\n")
    print("\nEnter q or Q to exi program\n")

    choice = input("Enter your choice: ")

    if choice  == 'q' or choice == 'Q':
        num3 = input(print("Are you sure you want to end program?(y/n): "))
        if num3 == 'y' or num3 == 'Y':
            print("Goodbye :)")
            break
        else:
            continue
    else:
        continue
        

    num1 = float(input("Enter your first digit: "))
    num2 = float(input("Enter your second digit: "))

    if choice == "1":
            (print(num1,"+",num2,"=",(num1+num2)))
    elif choice == "2":
            (print(num1,"-",num2,"=",(num1-num2)))
    elif choice == "3":
            (print(num1,"x",num2,"=",(num1*num2)))
    elif choice == "4":
        if num2 == 0:
            print("\nMathematical error! Can't divide by 0\n")
        else:
            (print(num1,"/",num2,"=",(num1/num2)))
    elif choice == "5":
            x= pow(num1, num2)
            (print(num1,"^",num2,"=",(x)))
    else:
        print("Enter correct digits")
    

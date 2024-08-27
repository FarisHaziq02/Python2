def divide_numbers():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        result = a / b
        print(f"the division of {a} and {b} is {result}")
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("You must enter a number!")

    finally:
        print("Operation complete!")

divide_numbers()
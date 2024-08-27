def check_positive_number(num):
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("The number must be positive!")
    return num

try:
    num = check_positive_number(int)
    print("The number is valid")

except ValueError as ve:
    print(ve)
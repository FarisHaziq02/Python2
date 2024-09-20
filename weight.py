# Python weight converter

weight = float(input("What is your weight: "))
unit = input("Kilogram or Pounds? (K or P): ")

if unit == "K":
    weight = round(weight * 2.205, 1)
    print(f"Your weight is {weight} Pounds")
elif unit == "P":
    weight = round(weight / 2.205, 1)
    print(f"Your weight is {weight} Kilograms")
else:
    print("Invalid input")
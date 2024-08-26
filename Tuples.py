#Creating tuples
fruits = ("apple", "banana", "cherry", "date")
print(fruits[0], fruits[3])
print(fruits)

#Tuples operations
numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers

print("a:",a)
print("b:",b)
print("rest:",rest)

fruits[1] = "blueberry"
print(fruits)
#It show an error because tuples are immutable


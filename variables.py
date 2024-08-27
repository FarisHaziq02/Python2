x = 0

def print_global():
    print(x)

def increment_counter():
    global x
    x += 1
    print(x)


def reset_counter():
    x = 0
    print(x)

increment_counter()
increment_counter()
increment_counter()
reset_counter()



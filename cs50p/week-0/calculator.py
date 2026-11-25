# nesting the function input() into the function int() to avoid writing too many lines of code
x = float(input("What's x? "))
y = float(input("What's y? "))

# int is not only a type of data in python but also a function
print(x + y)


# we could also make it a single line of code print(int(input("What's x? ")) + int(input("What's y? ")))
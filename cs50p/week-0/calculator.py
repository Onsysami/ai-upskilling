# nesting the function input() into the function int() to avoid writing too many lines of code
# round() function - note that the [] usually mean these conditions are optional - in this case you can specify to what number digits you want to round

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

# int is not only a type of data in python but also a function
print(z)


# we could also make it a single line of code print(int(input("What's x? ")) + int(input("What's y? ")))
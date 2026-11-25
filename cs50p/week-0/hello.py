# Ask user for their name
# name = input("What's your name? ").strip().title()


# Remove whitespace from str
# name = name.strip().title() simplified it even further and added the functions to
# the first line

# Capitalize user's name - unlike .capitalize() the .title() function capitalizes like
# in a title - not just the first word that is typed
# name = name.title() I now chained it to the previous function

# Split user's name into first name and last name
# first, last = name.split(" ")

"""
Say hello to user - used the f-string is short for formatted string literal to
allow me to add the variable directly in the string and avoid joining 2 strings with +
NOTE: print is a positional parameter what ever is printed first will appear first
sep and end are named parameters because they're optional and they can also be used
by name
"""
# print(f"hello, {first}")

# Python documentation => end = "\n" and sep = " " by default


# starting over completely - we're working to define (def) create our own function - added a parameter "to" - notice how by default it says hello, world before asking me for my name
# defining own function is to avoid having to repeat again and again if you just wanted to say hello
# def hello(to="world"):
#    print("hello,", to)

# hello()
# name = input("What's your name? ")
# hello(name)


# Now we're redefining the how the function is declared -  this now works - this can cause scope issues if it's defined in one function but not in the other
# def main():
#    name = input("What's your name? ")
#    hello()

# def hello():
#    print("hello,", name)

# main()

# Back to what we had before
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

    main()
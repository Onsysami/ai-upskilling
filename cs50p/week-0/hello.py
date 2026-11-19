# Ask user for their name
name = input("What's your name? ")


# Remove whitespace from str
name = name.strip()

"""
Say hello to user - used the f-string is short for formatted string literal to
allow me to add the variable directly in the string and avoid joining 2 strings with +
NOTE: print is a positional parameter what ever is printed first will appear first
sep and end are named parameters because they're optional and they can also be used
by name
"""
print(f"hello, {name}")

# Python documentation => end = "\n" and sep = " " by default
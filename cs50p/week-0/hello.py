# Ask user for their name
name = input("What's your name? ").strip().title()


# Remove whitespace from str
# name = name.strip().title() simplified it even further and added the functions to
# the first line

# Capitalize user's name - unlike .capitalize() the .title() function capitalizes like
# in a title - not just the first word that is typed
# name = name.title() I now chained it to the previous function

# Split user's name into first name and last name
first, last = name.split(" ")

"""
Say hello to user - used the f-string is short for formatted string literal to
allow me to add the variable directly in the string and avoid joining 2 strings with +
NOTE: print is a positional parameter what ever is printed first will appear first
sep and end are named parameters because they're optional and they can also be used
by name
"""
print(f"hello, {first}")

# Python documentation => end = "\n" and sep = " " by default
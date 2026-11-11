from datetime import date
name = input("What's your name? ")
colour = input("What's your favourite colour? ")
city = input("What city do you line in? ")

try:
    age = int(input("How old are you? "))
    print(f"Hello, {name}! {colour} is a great colour.")
    birth_year = date.today().year - age
    print(f"You were born around {birth_year}.")
    print(f"Summary: {name}, {age}, from {city} - favourite colour {colour}, born around {birth_year}.")
except ValueError:
    print(f"Hello, {name}! I need your age as a number — words don't count.")
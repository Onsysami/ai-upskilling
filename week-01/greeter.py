name = input("What's your name? ")
colour = input("What's your favourite colour? ")

try:
    age = int(input("How old are you? "))
    print(f"Hello, {name}! {colour} is a great colour.")
    print(f"Next year you'll be {age + 1}.")
except ValueError:
    print(f"Hello, {name}! I need your age as a number — words don't count.")
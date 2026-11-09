name = input("What's your name? ")

try:
    age = int(input("How old are you? "))
    print(f"Hello, {name}!")
    print(f"Next year you'll be {age + 1}.")
except ValueError:
    print(f"Hello, {name}! I need your age as a number — words don't count.")

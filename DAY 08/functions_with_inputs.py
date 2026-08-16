def greet():
    print(f"Hello!")
    print(f"Welcome to the world of functions.")
    print(f"I hope you enjoy learning Python.")

greet()

# Function that allows for inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Billie")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Billie", "New York")
greet_with(location="Los Angeles", name="Sam")
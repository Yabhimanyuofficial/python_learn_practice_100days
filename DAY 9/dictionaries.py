# create dictionaries 
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
    
    }

# Retrieving a value from a dictionary
print(programming_dictionary["Bug"])

#Adding more items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary
empty_dictionary = {}   

# Wipe an existing dictionary
programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
for key in programming_dictionary:
    print(key) # prints the key
    print(programming_dictionary[key])  # prints the value associated with the key   


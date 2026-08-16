def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

#formated_name = format_name(input("What is your first name? "), input("What is your last name? "))
#print(formated_name)
print(format_name(input("What is your first name? "), input("What is your last name? ")))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

print(function_2(function_1("hello")))
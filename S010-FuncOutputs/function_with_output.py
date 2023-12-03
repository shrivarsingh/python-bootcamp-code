# Function with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        #return # empty return -> terminate program early
        #better to return something rather than nothing
        return "You didn't provide valid result"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
# OR
def format_namev2(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(format_name(f_name=first_name,l_name=last_name))

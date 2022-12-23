from datetime import datetime
 
# This is a comment. It is used to display useful
# information to people who read our code
 
def print_message(prefix, first_name):
    print(prefix + " " + first_name)
 
# Get user input
first_name = input("Enter a name: ")
 
# Check if the first_name variable is equal to 'Q'
# If so we will skip the next greeting
while first_name != "Q":
 
    # Display the joined message to our user
    print_message("Hello", first_name)
     
    # Display the current time using the datetime library
    # and chaining method calls to .now() and .strftime()
    print("The current time is ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
     
    print_message("Goodbye", first_name)
 
    first_name = input("Enter another name or 'Q' to quit: ").title()
 
print("Quitting greeter")

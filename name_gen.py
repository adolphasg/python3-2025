import random  # Import the random module for generating random values
import string  # Import the string module for generating random characters

# Prompt the user to enter the number of EC2 instances they want
number_of_ec2 = int(input("Enter the number of EC2 instances you want created: "))

# Prompt the user to enter the name of their department
departments = input("What is the name of your department? ")

# Define a tuple of valid department names
valid_departments = ("Marketing", "Accounting", "FinOps")

# Check if the entered department is in the list of valid departments
if departments in valid_departments:
    # Loop to generate and print names for the number of EC2 instances specified
    for i in range(number_of_ec2):
        # Generate a random two-letter string
        random_char = "".join(random.choices(string.ascii_letters, k=2))
        # Create a generated name by combining department, random characters, and a random number
        generated_names = departments + "-" + random_char + str(random.randrange(0, 200))
        # Print the generated name
        print(generated_names)
else:
    # Print an error message if the department is not valid
    print("Sorry, you do not have permissions to use the name generator.")
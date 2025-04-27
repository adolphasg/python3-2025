import random
import string

# Allowed departments
allowed_departments = ["Marketing", "Accounting", "FinOps"]

def generate_random_string(length=6):
    """Generate a random string of letters and digits."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the EC2 Name Wizard!")
    
    department = input("Enter your department (Marketing, Accounting, FinOps): ").strip().capitalize()

    if department not in allowed_departments:
        print(f"Access Denied: '{department}' department is not allowed to use this Name Generator.")
        return

    try:
        number_of_instances = int(input("How many EC2 instance names do you need?: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print("\nHere are your unique EC2 instance names:")
    for _ in range(number_of_instances):
        random_part = generate_random_string()
        ec2_name = f"{department}-{random_part}"
        print(ec2_name)

if __name__ == "__main__":
    main()

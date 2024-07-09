import string
import random

def generate_password(length=12):
    """Generate a random password of a specified length."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character sets
    characters = {
        '1': string.digits,
        '2': string.ascii_letters,
        '3': string.punctuation,
        '4': string.ascii_letters + string.digits + string.punctuation
    }

    # Prompt user to choose character sets
    print("Choose character sets for your password:")
    print("1. Digits")
    print("2. Letters")
    print("3. Special characters")
    print("4. Mix of all")
    print("5. Exit")

    choice = input("Enter your choices (e.g., '1 3' for digits and special characters): ").split()

    if '5' in choice:
        raise ValueError("Exiting program.")

    # Validate user input and build character list
    selected_chars = [characters[key] for key in choice if key in characters]

    if not selected_chars:
        raise ValueError("Please select at least one valid character set.")

    # Generate password
    password = []
    for _ in range(length):
        chosen_set = random.choice(selected_chars)
        password.append(random.choice(chosen_set))

    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter desired password length (default is 12): ").strip() or 12)
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

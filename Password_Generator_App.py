import random
import string

def generate_password(length=12):
    """Generate a random password with uppercase, lowercase, digits, and special characters."""
    if length < 6:
        print("Password length should be at least 6 characters for better security.")
        return None

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password includes at least one character from each pool
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters from all pools
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)

def main():
    print("\n--- Password Generator ---")
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        password = generate_password(length)
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()

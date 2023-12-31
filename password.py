import secrets
import string

#function to generate password as per required complexity
def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.punctuation
    else:
        print("Invalid complexity choice. Using default (easy).")
        characters = string.ascii_letters + string.digits

    generated_password = ''.join(secrets.choice(characters) for _ in range(length))
    return generated_password

print("===== Password Generator =====")
length = int(input("Enter the desired length of the password: "))
complexity = input("Choose complexity (easy/medium/hard): ").lower()

password = generate_password(length, complexity)

print("\nGenerated Password:")
print(password)

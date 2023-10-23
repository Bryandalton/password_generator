import random
import string

def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

num_passwords = 100000
passwords = [generate_password() for _ in range(num_passwords)]

# Saving the passwords to a file (optional)
with open('passwords.txt', 'w') as file:
    for password in passwords:
        file.write(password + '\n')

print("Passwords generated and saved to 'passwords.txt'!")
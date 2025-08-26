"""
The following function generates a random password with the following criteria:
# 1 special char at least
# 1 uppercase char at least
# 1 number at least
# lengh of password = 12 at least
"""

import random

def generate_password(length=12):
    password = []

    if length < 12:
        print("Password length should be at least 12 characters.")
        return None

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "!@#$%^&*()-+"

    all_characters = lowercase + uppercase + numbers + special_characters

    password = [random.choice(lowercase), random.choice(uppercase), random.choice(numbers), random.choice(special_characters)]

    remaining_length = length - len(password)

    password += random.choices(all_characters, k=remaining_length)

    return ''.join(password)


if __name__ == "__main__":
    print(generate_password(12))
    print(generate_password(9))
    print(generate_password(12))
    print(generate_password(12))

import random
import string
def generate_password():
    user_input = input("pick password strength: weak, strong, very strong ")
    strength_dict = {"weak":5,"strong":8,"very strong":12}
    if strength_dict.get(user_input) == None:
        return "Invalid input"
    else:
        pw_strength = strength_dict.get(user_input)
        password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
        ]
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password += [random.choice(all_characters) for ch in range(pw_strength-4)]
        return "".join(password)
print(generate_password())
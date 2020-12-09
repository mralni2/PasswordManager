import secrets
import string


def check_password(password):
    complexity = 0
    if len(password) < 8:
        return complexity
    for i in string.ascii_lowercase:
        if i in password:
            complexity += 1
            break
    for i in string.ascii_uppercase:
        if i in password:
            complexity += 1
            break
    for i in string.digits:
        if i in password:
            complexity += 1
            break
    for i in string.punctuation:
        if i in password:
            complexity += 1
            break
    return complexity


def start_password_generator(length, spec):
    if spec <= 0:
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    else:
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''
    while check_password(password) < 3:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def count_spec(password):
    count = 0
    for i in string.punctuation:
        for j in password:
            if i == j:
                count += 1
    return count

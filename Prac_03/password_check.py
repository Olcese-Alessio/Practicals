""" Set minimum length of password"""
minimum_length = 4


def main():
    """Get a password and print using functions."""
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    """ Prints same number of asterisks as there are characters in password"""
    print('*' * len(password))


def get_password(minimum_length):
    """ Gets password and ensures it is valid """
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password


main()


def main():
    """ Create dictionary """
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = determine_name(email)
        email = confirmation(email, email_to_name, name)
    print_list_of_email(email_to_name)


def confirmation(email, email_to_name, name):
    """ Confirm that auto generated name is correct """
    confirm_name = input("Is your name {}? (Y/N) ".format(name))
    if confirm_name.upper() != "Y" and confirm_name != '':
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email :")
    return email


def print_list_of_email(email_to_name):
    """Print out list of all names and emails"""
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def determine_name(email):
    """Attempt name generation from email"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()



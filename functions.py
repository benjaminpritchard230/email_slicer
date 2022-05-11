def enter_email():
    """Gets user's desired email."""
    while True:
        while True: 
            try: 
                email = input('Please enter an email address:\n')
            except ValueError:
                print('Please enter an email address:')
                continue
            break
        if '@' not in email:
            print('Email address must contain @.')
        else:
            return email


def get_domain(email):
    """Gets the domain name from an email address."""
    email_as_list = list(email)
    reversed_domain = []
    domain = []
    for i in reversed(email_as_list):
        if i == '@':
            break
        else:
            reversed_domain.append(i)
    for i in reversed(reversed_domain):
        domain.append(i)
    domain = ''.join(domain)
    return domain

def get_username(email):
    email_as_list = list(email)
    username = []
    for i in email_as_list:
        if i == '@':
            break
        else:
            username.append(i)
    username = ''.join(username)
    return username

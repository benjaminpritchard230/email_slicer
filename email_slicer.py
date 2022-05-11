from functions import *

email = enter_email()
username = get_username(email)
domain = get_domain(email)

print(f'Email: {email}')
print(f'Username: {username}')
print(f'Domain: {domain}')

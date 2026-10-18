def check_lgin(password):
    if password == 'NullPointer2026':
        return True
    else:
        return False

user_pass = input('Enter your login password: ')
check = check_lgin(user_pass)
if check:
    print('Login successful!, you can enter')
else:
    print('Login failed.')


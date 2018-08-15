PASSWORD = 'admin'

for i in range(3):
    user_password = input('pass:')
    if user_password == PASSWORD:
        print('HELLO')
        break
    print(f'Wrong password! Attempts: {3 - i - 1}')

    
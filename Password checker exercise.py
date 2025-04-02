## user name

username = input("Input your username")

## Password

password = input("Input your password")

lenpassword = len(password)

passwordhash= "*" * lenpassword

print(f'Dear {username}, your password {passwordhash} is {lenpassword} characters long')
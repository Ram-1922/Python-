
username = ""
password = ""
spl="!@#$%^&*_"
p=0

print("Condition:\n 1. password must be at least 8 characters\n 2. must include one uppercase, one lowercase, one digit, and one special character (!@#$%^&*)\n 3. must not contain spaces\n 4. must not include your username")

while not username:
    username=input("Enter Username: ")
while p==0:
    password=input("Enter Password:")
    if not password:
        print("Password can\'t be empty...")
    elif len(password)<8:
        print("Password must contain more than 8 characters...")
    elif ' ' in password:
        print("Must not contain spaces...")
    elif not any(i.islower() for i in password) or not any(i.isupper() for i in password) or not any(i.isdigit()  for i in password) or not any(i in spl for i in password):
        print("Must satisfy the condition...")
    elif sum(i.isdigit() for i in password)<4:
        print("Must contain 4 digits")
    elif username.lower() in password.lower():
        print("Username shouldn\'t be in Password")
    else:
        print("Password Updated...")
        p=1

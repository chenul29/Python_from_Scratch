from cryptography.fernet import Fernet

#creating key for encryption
def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def loadkey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = loadkey()
fer = Fernet(key)

def add():
    name = input("Enter Name: ")
    pwd = input("Enter Passwords: ")

    with open ('password.txt', 'a') as file:
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open ('password.txt', 'r') as file:
        for passwords in file.readlines():
            data = passwords.rstrip()
            username, pswd = data.split("|")
            print("username:", username, "Password", fer.decrypt(pswd.encode()).decode())

while True:
    answer = input("Do you want to create or view passwords? q for quit: ")

    if answer == "q":
        break
    elif answer == "add":
        add()
    elif answer == "view":
        view()
    else:
        print("Invalid Input")
        continue

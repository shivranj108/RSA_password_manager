#Password manager using RSA encryption

import rsa
import os

os.system('clear')

def gen_keys():
    (pub_key, priv_key) = rsa.newkeys(2048)
    with open('password_rsa/keys/pubkey.pem', 'wb') as f:
        f.write(pub_key.save_pkcs1('PEM'))
    with open('password_rsa/keys/privkey.pem', 'wb') as f:
        f.write(priv_key.save_pkcs1('PEM'))

def load_keys():
    with open('password_rsa/keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())
    
    with open('password_rsa/keys/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey

def encrypt(message, pubkey):
    cipher = rsa.encrypt(message.encode("ascii"), pubkey)
    with open('password.txt', 'wb') as f:
        f.write(cipher)

def decrypt(privkey):
    try:
        with open('password.txt', 'rb') as f:
            ct = f.read()
        clearText =  rsa.decrypt(ct, privkey).decode('ascii')

        return clearText

    except:
        return False
    
gen_keys()
pubKey, privKey = load_keys()

while True:
    print("|   Welcome to SPM#1   |")
    choice = int(input("| 1 - Encrypt password | \n| 2 - Decrypt password | \n| 3 - Break            |\n: "))
    if type(choice) != int:
        print("Enter an integer within given range")
    elif choice == 1:
        password = input("Enter your password | ")
        encrypt(password, pubKey)
    elif choice == 2:
        clearText = decrypt(privKey)
        print(clearText)
    elif choice == 3:
        break

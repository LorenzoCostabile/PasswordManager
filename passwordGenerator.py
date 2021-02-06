import sys
from random import choice, randint
from string import ascii_letters, digits, punctuation
from cryptography.fernet import Fernet, InvalidToken
import psycopg2
import createDB
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from datetime import date

def encryptPass(password,key):
    encoded = password.encode()
    #Encrypt the password
    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    return encrypted

def decryptPass(encrypted,key):
    #Decrypt the password
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    password = decrypted.decode()
    return password

def createKeyFromPassAndSalt(password,salt):
    password = password.encode() # Convert to type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # can only use kdf once
    return key

def generateNewPassword(min=14,max=20,method=3):
    if method == 1:
        string_format = ascii_letters
    elif method == 2:
        string_format = ascii_letters + digits
    elif method == 3:
        string_format = ascii_letters + digits + punctuation
    else:
        raise ValueError("Error el metodo de generar una contraseña no existe. Debe ser 1, 2, o 3.")

    generated_string = "".join(choice(string_format) for x in range(randint(min, max)))
    return generated_string

def insertNewPasswordInDB(values):
    pass


if __name__ == '__main__':
    #you need to generate a salt code with the command os.urandom(arg) and as an argument the length in of the salt.
    salt = b''
    selectedOPT = ''
    try:
        print('Please insert the master password to acces the EgongoIsSafe database: ')
        masterPassword = input()
        key = createKeyFromPassAndSalt(masterPassword,salt)
        print('Okay you now will decrypt the passwords with that key. If you want to try another masterPassword press R, if you want to exit the script press E, if you want to search for a password press S, if you want to create a password press C.')
        while(selectedOPT != 'E'):
            
            print('Select option:\n')
            selectedOPT = input()
            if selectedOPT == 'S':
                print('Write the web to acces: \n')
                web = input()
                password = createDB.filterForWeb(web,'egongoIsSafe.db')[0][0]
                try:
                    password = decryptPass(password,key)
                except InvalidToken:
                    print('MasterPassword incorrect, try another.')
                print(password)
            elif selectedOPT == 'R':
                print('Please insert the master password to acces the EgongoIsSafe database: ')
                masterPassword = input()
                key = createKeyFromPassAndSalt(masterPassword,salt)
            elif selectedOPT == 'E':
                selectedOPT = 'E'
                pass
            elif selectedOPT == 'C':
                print('Write the website name for this password:')
                website_name = input()
                print('Write the username for this password:')
                username = input()
                print('Copy the link for this website:')
                link = input()
                print('Write the email for this password:')
                email = input()
                print('Select the mode: 1 (only characters), 2 (characters and digits) or 3 (characters, digits and punctuation simbols):')
                mode = input()
                password = generateNewPassword(method=int(mode))
                password = encryptPass(password,key)
                values = [website_name,link,password,username,email,str(date.today())]
                createDB.insertValues(values,'egongoIsSafe.db')
                                
                

            else:
                print('Opcion incorrecta.')

    except KeyboardInterrupt:
        sys.exit("Keyboard Interrupt")

    except ValueError:
        sys.exit("Error de Valor erroneo.")
from cryptography.fernet import Fernet

file = open('key.key','rb')
key = file.read()
file.close()

message = "es un espia ruso"
encoded = message.encode()

#Encrypt the message
f = Fernet(key)
encrypted = f.encrypt(encoded)
print(encrypted)

file = open('MensajeEncriptado','w+b')
file.write(encrypted)
file.close()
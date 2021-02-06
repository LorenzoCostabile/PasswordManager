from cryptography.fernet import Fernet

file = open('MensajeEncriptado','rb')
mensajeEncryptado = file.read()
file.close()

file = open('key.key','rb')
key = file.read()
file.close()

f = Fernet(key)
decrypted = f.decrypt(mensajeEncryptado)

mensaje = decrypted.decode()
print(mensaje)
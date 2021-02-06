import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "FBpZCELJiJtFdD2FSa7J"
password = password_provided.encode() # Convert to type bytes
salt = b'\x8d\x17\xee\r}%\xdf74M\x07\xf1A\x13[\xe4'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # can only use kdf once
print(key)
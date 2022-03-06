import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

TEMPORAL_MASTER_DECRYPT_PWD = bytes("caca_culo_pedo_pis", 'utf-8')  # TODO: Get from User
SALT = b'\x00s\x12X\x18\x04\xb7\xab\x89\x1a4u\xbe\x96\xbe\xa4'  # TODO: Store in a better way


def show_password(password_token):
    """
        Method that decrypts the token into plain text password.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(TEMPORAL_MASTER_DECRYPT_PWD))
    f = Fernet(key)
    decrypt = ""
    if password_token:
        decrypt = f.decrypt(bytes(password_token, "utf-8")).decode("utf-8")
    return decrypt


def generate_password_token(password):
    """
        Method that encrypts a plain text password using SHA256 hash.
    """
    # salt = os.urandom(16) # Became a Constant after first generation
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(TEMPORAL_MASTER_DECRYPT_PWD))
    f = Fernet(key)
    token = ""
    if password:
        token = f.encrypt(bytes(password, "utf-8")).decode("utf-8")
    return token

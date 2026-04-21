import hashlib

def login(password):
    return hashlib.md5(password.encode())

def check(data):
    return hashlib.sha1(data.encode())

print("RSA encryption test")
import maskpass
from cryptography.fernet import Fernet

pwd = input("Enter Password:  ")
print(pwd)
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(pwd.encode())

print("original string: ", pwd)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
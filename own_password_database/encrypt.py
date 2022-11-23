from cryptography.fernet import Fernet

with open(r'C:\Users\benja\OneDrive\Pulpit\Studia_AGH\git_repos\Python_repo\own_password_database\filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)
with open(r'C:\Users\benja\OneDrive\Pulpit\Studia_AGH\git_repos\Python_repo\own_password_database\add_to_database.txt', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open(r'C:\Users\benja\OneDrive\Pulpit\Studia_AGH\git_repos\Python_repo\own_password_database\add_to_database.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
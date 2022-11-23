from cryptography.fernet import Fernet
key = Fernet.generate_key()
 
# string the key in a file
with open(r'C:\Users\benja\OneDrive\Pulpit\Studia_AGH\git_repos\Python_repo\own_password_database\filekey.key', 'wb') as file:
    file.write(key)

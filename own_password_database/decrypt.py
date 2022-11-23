from cryptography.fernet import Fernet
with open(r'C:\Users\benja\OneDrive\Pulpit\Studia_AGH\git_repos\Python_repo\own_password_database\filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)
 
with open(r'C:\Users\benja\OneDrive\Pulpit\Studia_AGH\git_repos\Python_repo\own_password_database\add_to_database.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open(r'C:\Users\benja\OneDrive\Pulpit\Studia_AGH\git_repos\Python_repo\own_password_database\add_to_database.txt', 'wb') as dec_file:
    dec_file.write(decrypted)
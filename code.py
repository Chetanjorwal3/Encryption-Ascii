import string
from encrypt_func import encrypt
from decrypt_func import decrypt

text = str(input('Enter Message :- '))
encrypt(text,key = 5)
print(encrypt(text,key = 5))
text = encrypt(text,key = 5)
print(decrypt(text,key = 5))
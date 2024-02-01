'''
Este modulo es el que contiene los metodos para
generar y guardar las contraseñas

'''

import secrets
import string

def password_generator(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

def save_passwords(contraseñas, archivo):
    with open(archivo, 'w') as file:
        for contraseña in contraseñas:
            file.write(contraseña + "\n")
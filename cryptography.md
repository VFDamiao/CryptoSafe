# CryptoSafe

## Instalação da Biblioteca

pip install cryptography

## Importe a biblioteca e defina uma chave de criptografia:

from cryptography.fernet import Fernet

# Gere uma chave de criptografia

key = Fernet.generate_key()

# Crie um objeto Fernet usando a chave

fernet = Fernet(key)

# Defina funções para criptografar e descriptografar strings:

def encrypt(text): # Codifique a string como bytes
encoded_text = text.encode()

    # Use o objeto Fernet para criptografar os bytes
    encrypted_text = fernet.encrypt(encoded_text)

    # Retorne a string criptografada como uma string codificada em base64
    return encrypted_text.decode("utf-8")

def decrypt(encrypted_text): # Decodifique a string criptografada de volta em bytes
decoded_text = encrypted_text.encode("utf-8")

    # Use o objeto Fernet para descriptografar os bytes
    decrypted_text = fernet.decrypt(decoded_text)

    # Retorne a string descriptografada como uma string
    return decrypted_text.decode()

# Use as funções para criptografar e descriptografar dados em seu aplicativo Django:

from django.shortcuts import render
from django.http import HttpResponse

def my_view(request): # Dados a serem criptografados
my_data = "dados sensíveis"

    # Criptografe os dados
    encrypted_data = encrypt(my_data)

    # Exiba a string criptografada na resposta HTTP
    return HttpResponse(encrypted_data)

def my_other_view(request): # String criptografada recebida de algum lugar
encrypted_data = request.GET.get("data")

    # Descriptografe os dados
    decrypted_data = decrypt(encrypted_data)

    # Exiba a string descriptografada na resposta HTTP
    return HttpResponse(decrypted_data)

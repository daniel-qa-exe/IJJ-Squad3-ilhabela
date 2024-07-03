import requests

cep = input("digite seu cep: ")
response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
data = response.json()
print("o logradouro do seu cep é ", data['logradouro'])
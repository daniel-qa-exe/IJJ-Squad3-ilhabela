import requests

squad = {
    "daniel":"11630340",
    "yehudi":"11630001",
    "viviane":"11630003",
    "christopher":"11630115"
}
for nome, cep in squad.items():
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    cidade = data['localidade']
    print(f"O nome do integrante do squad é {nome} e sua cidade é {cidade}")
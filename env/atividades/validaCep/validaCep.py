import requests

uf_frete_gratis = ["AM","PA","AC","RR","RO","AP","TO","AL","BA","CE","MA","PB","PE","PI","RN","SE"]
cep = input("Digite um CEP para verificar o frete: ")

# Verifica se o CEP tem exatamente 8 dígitos
if len(cep) != 8:
    print("Digite um CEP válido, com 8 dígitos") 
else:
    # Faz a requisição à API do ViaCEP
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()

    # Verifica se a resposta contém a chave 'uf'
    if 'uf' in data:
        uf = data['uf']
        # Verifica se a UF está na lista de frete grátis
        if uf in uf_frete_gratis:
            print("Está na lista de frete grátis")
        else:
            print("Não está na lista de frete grátis")
    else:
        print("CEP inválido ou não encontrado")


"""
import requests

# Lista de UFs com frete grátis
uf_frete_gratis = ["AM", "PA", "AC", "RR", "RO", "AP", "TO", "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]

# Função para obter a UF a partir de um CEP usando a API do ViaCEP
def obter_uf_por_cep(cep):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        data = response.json()
        if 'uf' in data:
            return data['uf']
        else:
            return None
    except Exception as e:
        print(f"Erro ao consultar o CEP: {e}")
        return None

# Função principal
def verificar_frete_gratis():
    cep = input("Digite um CEP para verificar o frete: ")

    # Verifica se o CEP tem exatamente 8 dígitos
    if len(cep) != 8:
        print("Digite um CEP válido, com 8 dígitos") 
    else:
        uf = obter_uf_por_cep(cep)
        if uf:
            if uf in uf_frete_gratis:
                print("Está na lista de frete grátis")
            else:
                print("Não está na lista de frete grátis")
        else:
            print("CEP inválido ou não encontrado")

# Chama a função principal
verificar_frete_gratis()


"""
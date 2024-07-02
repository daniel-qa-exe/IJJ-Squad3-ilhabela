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










#import requests

#uf_frete_gratis = ["AM","PA","AC","RR","RO","AP","TO","AL","BA","CE","MA","PB","PN","PI","RN","SE"]
#cep = input("digite um cep para verificar o frete: ")
#valida_cep = len(cep)

#print(data['uf'])
#if valida_cep <8 or valida_cep > 8:
#    print("digite um ceo valido, com 8 digitos") 
#else:
#    for uf in uf_frete_gratis.items(): 
#        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
#        data = response.json()
#        if data['uf'] in uf_frete_gratis:
#            print("esta na lista")
#        else:
#            print("nao esta na lista")
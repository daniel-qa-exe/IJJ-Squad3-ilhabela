#tupla de nomes
nomes =("daniel","viviane","yehudi","christopher","matheus")
#alterar tupla para lista 
nomes_list = list(nomes)
#adicionando mais dados na lista
nomes_list.append("ryan")
nomes_list.append("vini")
#removendo o primeiro dado da lista 
nomes_list.pop(0)
#removendo o ultimo dado da lista 
nomes_list.pop()
#print com o primeiro dado da lista
print(nomes_list[0])
#função para contar a quntidade de dados na lista e depois um print desse valor 
tamanho_lista = len(nomes_list)
print(tamanho_lista)
#criação de dicionario 
dicionario = {
    "nome":"Daniel",
    "idade":24,
    "profissao":"Dev python junior & QA junior"
}
#print da informação do dicionario no campo nome 
print(dicionario["nome"])
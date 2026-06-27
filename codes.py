

'''
Lista em python
- Estrutura de dado ordenada de valores
- Cada valor é chamado de elemento e é identificado por um índice
- Possui tamanho dinâmico
- representadas por colchetes []
- Semelhantes a uma string, sequência de caracteres, no entanto, uma lista pode ter tipos diferentes de dados.


print('##############################################################################################')
print('################################## Exemplo de lista vazia ####################################')
print('')

lista_vazia = []
print(f'Impressão de lista vazia: {lista_vazia}')
print(f'Impressão do tipo do objeto da variável listaVazia: {type(lista_vazia)}')

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

print('##############################################################################################')
print('###################################### Exemplo de listas #####################################')
print(' ')

# Exemplos de Listas
listaNumerica = [-1, 22, 35, 52, 90, 54, 30]
print(listaNumerica)

listaCaracter = ['U', 'P', 'E', '-', 'G', 'U', 'S']
print(listaCaracter)

lista_mista = ['UPE', '2021', 10 + 10]
print(lista_mista)

# Convertendo uma string em uma lista
nomeIES = list('Universidade de Pernambuco')

# exemplos de acesso a elementos de uma lista
print(nomeIES)
print(nomeIES[0])
print(nomeIES[1])
print(nomeIES[2])

listaAninhada = [200, [220, 320], [1, 2, [20,50]]]
print(listaAninhada)
print(listaAninhada[0])
print(listaAninhada[1])
print(listaAninhada[1][0])
print(listaAninhada[1][1])
print(listaAninhada[2])

listaTodoTipo = [True, 10 + 10, [1, 2], "string qualquer"]
print(listaTodoTipo)

variavel01 = 9
variavel02 = 'oi'
variavel03 = "Olá"

listaVariaveis = [variavel01, variavel02, variavel03]
print(listaVariaveis)

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

print('##############################################################################################')
print('########################### Exemplo conversão de Range para List #############################')
print(' ')

# Criação de uma variável chama 'intervalo' e uma atribuição de uma chamada a função range a esta variável
intervalo = range(20)
print(f'Impressão do resultado da chamada a função range(): {intervalo} \n')
print(f'Impressão do tipo de objeto retornado após a chamada a função range(): {type(intervalo)} \n')

# Exemplo de lista com objetos do tipo range
novo_intervalo = [range(10), range(15)]
print(f'Lista criada com dois objetos do tipo range: {novo_intervalo} \n')

# conversão do range em lista
intervalo = list(intervalo)
print(f'Impressão da conversão do objeto do tipo range em lista: {intervalo} \n')
print(f'Impressão do tipo após a conversão do objeto do tipo range em lista: {type(intervalo)}')


print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

# Siga para aula do comando condicional IF

print('##############################################################################################')
print('############################# Checagem se existe um elemento  ################################')
print(' ')

# Exemplo de checagem de existência de um elemento em uma lista

lista_mista = ['UPE', '2000', 10 + 10]
print('')
print('Resultados da checagem, através do condicional IF,')
print('se existe um determinado elemento na lista listaMista.')
print(f'Impressão listaMista: {lista_mista}\n')

print('Existe a string UPE na listaMista?')
if 'UPE' in lista_mista:
    print('Sim, encontramos o item na Lista.')
else:
    print('Não encontramos o item na lista.')

print('Existe o número 20 na listaMista?')
if 20 in lista_mista:
    print('Sim, encontramos o item na Lista.')
else:
    print('Não encontramos o item na lista.')

print('Existe o número 2000 na listaMista?')
if 2000 in lista_mista:
    print('Sim, encontramos o item na Lista.')
else:
    print('Não encontramos o item na lista.')

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

print('')
print('##############################################################################################')
print('############################## Exemplo de ordenação de lista #################################')

listaNumerica = [1, 22, 35, 52, 90, 54, 30]
print(f'Impressão lista original: {listaNumerica}')

cloneListaNumerica = listaNumerica.copy()

print(f'Impressão do clone da lista original: {cloneListaNumerica}')

cloneListaNumerica.sort()

print(f'Impressão de clone ordenado: {cloneListaNumerica}')
print(f'Impressão da lista original: {listaNumerica}')

lista_caracter = ['a', 'e', 'h', 'j', 'b', 'c']
print(lista_caracter)
lista_caracter.sort()
print(lista_caracter)

lista_caracter = ['a', 'e', 'h', 'j', 'b', 'c']
lista_ordenada = sorted(lista_caracter)
print(lista_ordenada)
print(lista_caracter)

print('')
print('#############################################################')
print('############## Exemplo de ordenação de lista 2 ##############')
# Cuidado com as referências a objetos
# Neste caso não há uma cópia da lista e sim é criada outra referência a mesma lista.
# Alterações usando qualquer referência afetará a mesma lista.

listaNumerica = [1, 22, 35, 52, 90, 54, 30]
print(f'Lista original: {listaNumerica}')


pareceCloneListaNumerica = listaNumerica
print(f'Lista "clonada": {pareceCloneListaNumerica}')

pareceCloneListaNumerica.sort()
print(f'Impressão lista "clonada" ordenada: {pareceCloneListaNumerica}')
print(f'Impressão lista original (observe se há modificações): {listaNumerica}')


print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')


print('##############################################################################################')
print('#################################### Fatiamento de  lista ####################################')
print('')

listaNumerica = [1, 22, 35, 52, 90, 54, 30]
item_lista = listaNumerica[6]
print(item_lista)
# Descomente o código abaixo para ver um erro de acesso ao índice inexistente
# item_lista = listaNumerica[7]
# print(item_lista)
fatia_01 = listaNumerica[0:2]
print(fatia_01)
fatia_02 = listaNumerica[3:5:2]
print(fatia_02)
fatia_03 = listaNumerica[5:7]
print(fatia_03)
fatia_04 = listaNumerica[:7]
print(fatia_04)
fatia_05 = listaNumerica[2:]
print(fatia_05)
fatia_06 = listaNumerica[:]
print(fatia_06)

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

print('')
print('##############################################################################################')
print('################################# Exemplo de clone de lista ##################################')

listaNumerica = [1, 22, 35, 52, 90, 54, 30]
print(f'Impressão lista original: {listaNumerica}')
print('Impressão do clone da lista original:')
cloneListaNumerica = listaNumerica[:]
cloneListaNumerica2 = listaNumerica.copy()
print(f'Clone 01: {cloneListaNumerica}')
print(f'Clone 02: {cloneListaNumerica2}')

cloneListaNumerica.sort()
cloneListaNumerica2.reverse()
print('Impressão de clone ordenado:')
print(cloneListaNumerica)
print('Impressão de clone invertido:')
print(cloneListaNumerica2)
print('Impressão da lista original:')
print(listaNumerica)

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

# Comprimento de uma lista
print('')
print('##############################################################################################')
print('################################## Exemplo tamanho lista #####################################')

listaNumerica = [1, 22, 35, 52, 90, 54, 30]
lista_mista = ['UPE', '2021', 10 + 10]
listaAninhada = [200, [220, 320], [1, 2, [20,50]]]

print(f'Impressão listaNumerica: {listaNumerica}')
print(f'Tamanho listaNumerica: {len(listaNumerica)}')

print(f'Impressão listaMista: {lista_mista}')
print(f'Tamanho listaMista: {len(lista_mista)}')

print(f'Impressão listaAninhada: {listaAninhada}')
print(f'Tamanho listaMista: {len(listaAninhada)}')

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')
# Seguir para aula referente ao comando FOR e depois para parte 2'''








# Quantidade de ocorrências de um elemento em uma lista
print('##############################################################################################')
print('############################ Exemplo de contagem de ocorrências ##############################')
print('')

listaNumerica = [1, 22, 35, 52, 90, 54, 30]
listaCaracter = ['U', 'P', 'E', '-', 'G', 'U', 'S', 'EE']
lista_mista = ['UPE', '2021', 10 + 10]

print(f'Lista Caracter: {listaCaracter}')
print(f'Quantidade de caracteres "E" que são elementos da Lista Caracter: {listaCaracter.count("E")}')
print(f'Lista Numerica: {listaNumerica}')
print(f'Quantidade números "1000" que são elementos da Lista Numérica: {listaNumerica.count(1000)}')
print(f'Lista Mista: {lista_mista}')
print(f'Quantidade números "20" que são elementos da Lista Mista: {lista_mista.count(20)}')

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

print('##############################################################################################')
print('############################# Pertinência e enumerate() ######################################')
print('')

# Pertinência em uma lista
listaBolos = ['bolo de leite', 'bolo de milho', 'bolo de chocolate']

if 'bolo de leite' in listaBolos:
    print('Bolo de leite está diponível.')
else:
    print('Tem, mas está faltando.')

# Geração de índices com enumerate()
# Uma forma de percorrer uma lista acessando o conteúdo de cada elemento, bem como o índice dele.
# O enumarete pode ser aplicado a qualquer coisa que seja iterable.

listaBolos = ['bolo de leite', 'bolo de milho', 'bolo de chocolate', 'bolo de banana', 'bolo de mandioca',
              'bolo inglês', 'bolo de nutella', 'bolo de milho', 'bolo de laranja', 'bolo souza leão']

enumarate_bolos = enumerate(listaBolos)
print(enumarate_bolos)
print(type(enumarate_bolos))

for indice, tipoBolo in enumarate_bolos:
    print(indice, tipoBolo)

# Index retorna o índice do primeiro elemento encontrado.
print('index() retornará o índice do primeiro elemento encontrado da lista, no caso "bolo de milho"')
print('Lista Bolos: -', listaBolos)
print(f'índice do "bolo de milho": {listaBolos.index("bolo de milho")}')

# É possível determinar o índice que o método index() usará para iniciar a busca
print('é possível passar um parâmetro para index() informando a partir de qual índica procurar, no caso índica 2')
print('Lista Bolos: -', listaBolos)
print(f'índice do "bolo de milho": {listaBolos.index("bolo de milho", 2)}')


# Se o valor não for encontrado será retornado ValueError
print('Lista Bolos: -', listaBolos)
# Para ver o ValueError, modificar o índice abaixo para 8 ou maior
print(f'índice do "bolo de milho": {listaBolos.index("bolo de milho", 6)}')

# É possível fazer a busca do índice de um elemento dentro de um intervalo de busca
print(listaBolos.index('bolo de chocolate', 2, 6))

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

# Adição de elementos a lista.
# Método append(), um elemento por vez será adicionado em uma lista
# Método extend(), mais de elementos por vez (valores iteráveis) por vez será adicionado em uma lista
# Método insert(),

print('')
print('########################################################')
print('############ Exemplo de adição de elementos ############')

listaNumerica = [1, 22, 35, 52, 90, 54, 30]

print(listaNumerica)
listaNumerica.append(1000)
print(listaNumerica)
listaNumerica.append([101, 102, 103]) # Adiciona uma sublista a lista, criando uma lista aninhada.
print(listaNumerica)

if [101, 102, 103] in listaNumerica:
    print('O item foi encontrado')
else:
    print('O item não foi encontrado')

if [22, 35] in listaNumerica:
    print('O item foi encontrado')
else:
    print('O item não foi encontrado')

listaNumerica.extend([1001, 1002, 1003]) # Adiciona vários elementos individualmente a uma lista
print(listaNumerica)

lista_mista = ['UPE', '2021', 10 + 10]

print('Inserção da string "Pernambuco" na listaMista através do extend().')
print(f'Lista original: {lista_mista}')
lista_mista.extend('Pernambuco')
print(f'listaMista modificada: {lista_mista}')

print('Adicionaremos o elemento "frevo" na lista com o método insert:')
lista_mista.insert(2, "frevo")
print(f'Impressão listaMista modificada: {lista_mista}')

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

# Remoção de elementos a lista.
# Método pop(), remove e retorna o último elemento de uma lista. Também pode remover um índice específico.
# Método clear(), apaga os valores da lista
# Método del[], apaga um item específico
# Método remove(), busca o item pelo valor e remove a primeira aparição do item.

print('##############################################################################################')
print('########### Exemplo de remoção de elementos ############')
print('')

listaCaracter = ['U', 'P', 'E', '-', 'G', 'U', 'S']

print(f'Impressão listaCaracter: {listaCaracter}')

ultimo_elemento_lista = listaCaracter.pop()
print(f'Impressão do retorno do método pop(): {ultimo_elemento_lista}')

print(f'Impressão da lista após método pop(): {listaCaracter}')

print("Remoção do caracter índice 2 da lista acima, com uso de pop(2)")
# Além de remover o caracter, o pop() também retorna o valor.

print(f'O caracter removido foi o: {listaCaracter.pop(2)}')
print(listaCaracter)

# A função del não retorna valor
del listaCaracter[-1]
print(listaCaracter)

# o método remove(), tal qual a função del, não retorna valor.
a = listaCaracter.remove('-')
print(listaCaracter)
print(a)

print('Resultado da aplicação do método clear()')
listaCaracter.clear()
print(listaCaracter)

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')


print('##############################################################################################')
print('######################### Exemplo de uso do método split() e join() ##########################')
print('')

exemploString = "Universidade de Pernambuco"
print(f'Impressão da String Exemplo: {exemploString}')

lista_a_partir_string = exemploString.split()
print(f'Impressão da lista gerada a partir da aplicação do método split(): {lista_a_partir_string}')


exemploString = "Universidade-de-Pernambuco"
print(f'Impressão da String Exemplo: {exemploString}')
lista_a_partir_string = exemploString.split('-')
print(f'Impressão da lista gerada a partir da aplicação do método split() com parâmetro: {lista_a_partir_string}')

print('Junção de elementos de uma lista com join() para formar uma String:')
print(f'Lista Original: {lista_a_partir_string}')
print(type(lista_a_partir_string))

string_a_partir_lista = ' '.join(lista_a_partir_string)
print(f'String gerada: {string_a_partir_lista}')
print(type(string_a_partir_lista))

print(' ')
print('##############################################################################################')
print('##############################################################################################')
print(' ')

# Concatenação de listas
# Operado +
# Método extend()

print('##################################################################')
print('############### Exemplo de concatenação de listas ################')
print('')

listaCaracter = ['U', 'P', 'E', '-', 'G', 'U', 'S']
listaNumerica = [1, 22, 35, 52, 90, 54, 30]

print(f'Impressão listaNumerica: {listaNumerica}')
print(f'Impressão listaCaracter: {listaCaracter}')

print('Impressão da concatenação de listaNumerica com lista Caracter com o operador +')
listaConcat = listaNumerica + listaCaracter
print(f'listaNumerica original: {listaNumerica}')
print(f'listaCaracter original: {listaCaracter}')
print(f'lista concatenatada: {listaConcat}')

print('Impressão da concatenação de listaNumerica com lista Caracter com o método extend()')
print(f'listaNumerica original: {listaNumerica}')
print(f'listaCaracter original: {listaCaracter}')
listaNumerica.extend(listaCaracter)
listaCaracter.extend(listaNumerica)
print(f'listaNumerica modificada: {listaNumerica}')
print(f'listaCaracter modificada: {listaCaracter}')

# Inversão de listas
# Fatiamento [:]
# Método reverse()
print('')
print('##################################################################')
print('###################### Inversão de listas ########################')

# Forma não recomendada
listaNomes = ['Garanhuns', 'Arcoverde', 'Pedra']
print(listaNomes)
listaNomes[0], listaNomes[1], listaNomes[2] = listaNomes[2], listaNomes[1], listaNomes[0]
print(listaNomes)

listaCaracter = ['U', 'P', 'E', '-', 'G', 'U', 'S']
# Usando fatiamento
print(f'impressão listaCaracter original: {listaCaracter}')
print('É possível imprimir os elementos acessando pelos índices.')
print(f'Índice 0: {listaCaracter[0]}')
print(f'Índice 1: {listaCaracter[1]}')
print(f'Índice 2: {listaCaracter[2]}')
print('...')
print('Também é possível acessar índices negativos -1, -2, -3')
print(f'Índice -1:{listaCaracter[-1]}')
print(f'Índice -2:{listaCaracter[-2]}')
print(f'Índice -3:{listaCaracter[-3]}')
print('...')

print(f'É possivel imprimir fatias: {listaCaracter[:6]}')
print(f'É possível imprimir fatias com passo: {listaCaracter[:6:2]}')
print(f'É possível imprimir fatias com passo negativo {listaCaracter[::-1]}')

# Usando o método reverse()
print(f'impressão listaCaracter original: {listaCaracter}')
print(f'impressão listaCaracter invertida: {listaCaracter.reverse()}')

######################################################################################
print('')
print('##################################################################')
print('###################### Iterando em listas ########################')

listaCaracter = ['U', 'P', 'E', '-', 'G', 'U', 'S']
listaNumerica = [1, 22, 35, 52, 90, 54, 30]

for elementoLista in listaCaracter:
    print(elementoLista, end=' ')
print('')

for elementoLista in listaNumerica:
    print(elementoLista, end=' ')
print('')

concatElementos = ''

for elementoLista in listaCaracter:
    print(elementoLista)
    concatElementos = concatElementos + elementoLista
print(concatElementos)
print(type(concatElementos))

somaElementos = 0
for elementoLista in listaNumerica:
    print(elementoLista)
    somaElementos = somaElementos + elementoLista
print(somaElementos)
print(type(somaElementos))

listaDesejos = []
desejo = ''
while desejo != 'sair':
    desejo = input('O que você deseja? (digite "sair" para finalizar) -> ')
    if desejo.lower() != 'sair':
        listaDesejos.append(desejo)

# print('Sua lista de desejos é: ', end="")
# print(listaDesejos)

print(f'Sua lista de desejos é: {listaDesejos}')

######################################################################################
print('')
print('##################################################################')
print('################### Outras funções em listas #####################')
# Outras funções úteis
listaNumerica = [1, 22, 35, 52, 90, 54, 30]
# Soma dos valores de uma lista (listas com valores do tipo int ou float)
print(sum(listaNumerica))
# Valor mais alto de uma lista (listas com valores do tipo int ou float)
print(max(listaNumerica))
# Valor mais baixo de uma lista (listas com valores do tipo int ou float)
print(min(listaNumerica))

######################################################################################

print('')
print('##################################################################')
print('################## Desempacotamento de listas ####################')

# Desempacotamento de lista
# Se a quantidade de elementos da lista for diferente do número de variáveis o resultado é um Value Error
listaNumerica = [100, 200, 300]
variavel01, variavel02, variavel03 = listaNumerica
print(variavel01)
print(variavel02)
print(variavel03)

print('')
print('##################################################################')
print('################## Revertendo Lista com Sort() ###################')

listaNumerica = [1, 22, 35, 52, 90, 54, 30]
listaNumerica.sort(reverse=True)
print(listaNumerica)

listaNumerica = [1, 22, 35, 52, 90, 54, 30]
listaNumerica.sort()
print(listaNumerica)

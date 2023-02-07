#oque são lists em python?são usadas com variaveis homogêneas
lista= ['limite','derivada','integral']
print(type(lista))
#metodos com listas

lista.sort()# o metodo sort reorganiza uma lista em ordem crescente ou alfabetica
print(lista)

lista.sort(reverse=True)#usando sor com reverse podemos ordenar de forma decrescente
print(lista)

lista.append('series')#usando as listas podemos adicionar elementos com append

lista.remove('series')#remove apaga o item da lista

segundalista=lista.copy()#copia todos os elementos de uma lista

lista.pop(1)#remove um item atrelado ao indice da lista
print(lista)

lista.insert(1,'series')#insere em um indice da lista o elemento especificado
print(lista)

lista.extend(segundalista)#insere elementos de uma segunda lista a primeira 
print(lista)


#tupla são coleçoes imutaveis
tup=('area','base','altura')
print(type(tup))
#para adicionar elementos em uma tupla devemos converter em lista
y= list(tup)
y.append('triangulo')
print(y)

Novatup=(1,2,3,4,5,6,7,7,8,9,10)
print(Novatup.index(3))#retorna a posição de um elemento em uma tupla
print(Novatup.count(7))#retorna a quantidade de vezes que um elemento aparece

#sets em python

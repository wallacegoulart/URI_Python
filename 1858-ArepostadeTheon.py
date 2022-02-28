#1858 A Resposta de Theon

n = int(input())
lista = [int(x) for x in input().split(' ')]

print(lista.index(min(lista))+1)

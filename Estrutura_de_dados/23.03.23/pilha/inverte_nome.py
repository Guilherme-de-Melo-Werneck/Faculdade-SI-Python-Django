#inverta o nome joaquim usando pilha
from transformar_número import Pilha
pilha = Pilha()
x = input('Digite um nome: ')

for i in x:
    pilha.push(i)

while not pilha.pilhaVazia():
    print(pilha.pop(), end='')

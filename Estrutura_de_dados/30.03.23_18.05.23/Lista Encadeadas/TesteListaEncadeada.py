from Elemento import Elemento
from No import No
from ListaEncadeadas import ListaEncadeadas

e = Elemento()
e.setChave(1)
e.setNome('Guilherme')
n = No(e)
print(e.getChave(), e.getNome())
print(n.getDados().getNome(), n.getProximo())

l = ListaEncadeadas()
chave = int(input('Digite uma chave (-1 para encerrar): '))

while chave != -1:
    nome = input('Digite um nome: ')
    e = Elemento()
    e.setChave(chave)
    e.setNome(nome)
    n = No(e)
    l.insereNoInicio(n)
    l.mostraLista()

    chave = int(input('Digite uma chave (-1 pra encerrar): '))

chave = int(input('Digite uma chave (-1 pra encerrar): '))
while chave != -1 and not l.listaVazia():
    ret = l.retiraElemento(chave)
    if ret != None:
        print(f'Elemento retirado: {ret.getDados().getValores()}')
    else:
        print('Chave não encontrada!')

    chave = int(input('Digite uma chave (-1 pra encerrar): '))
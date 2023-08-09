'''
8.	Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
'''

class Monkey:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.pop()

nome = str(input('Digite o nome do macaco: '))
Monkey = Monkey(nome)

while True:
    opcoes = int(input('''
O que deseja fazer?
1 - Comer
2 - Ver Bucho
3 - Digerir
4 - Sair
> '''))

    if opcoes == 1:
        comida = input('Digite a comida: ')
        print(f'O macaco comeu a {comida}')
        Monkey.comer(comida = comida)

    elif opcoes == 2:
        Monkey.verBucho()

    elif opcoes == 3:
        Monkey.digerir()
        Monkey.verBucho()

    else:
        break

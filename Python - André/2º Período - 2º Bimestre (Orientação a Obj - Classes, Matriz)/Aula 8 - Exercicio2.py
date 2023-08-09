'''
2.	Classe Quadrado: Crie uma classe que modele um quadrado:
a.	Atributos: Tamanho do lado
b.	Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:
    def __init__(self, lado):
        self.tamanhoLado = lado
    
    def mudarValorLado(self, lado):
        self.tamanhoLado = lado

    def retornarValorLado(self):
        return self.tamanhoLado

    def calculoArea(self):
        return self.tamanhoLado * self.tamanhoLado

print('> Programa para calcular a área do quadrado')

valor = float(input('Digite o valor do lado do quadrado: '))
quadrado = Quadrado(valor)
q = quadrado.calculoArea()
print(q)

novoValor = float(input('Digite o novo valor do quadrado: '))
quadrado.mudarValorLado(novoValor)
q = quadrado.calculoArea()
print(q)


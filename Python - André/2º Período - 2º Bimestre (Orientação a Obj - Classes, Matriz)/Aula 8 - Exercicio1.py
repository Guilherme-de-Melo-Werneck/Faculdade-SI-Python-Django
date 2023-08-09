'''
1.	Classe Bola: Crie uma classe que modele uma bola:
a.	Atributos: Cor, circunferência, material
b.	Métodos: trocaCor e mostraCor
'''

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novaCor):
        self.cor = novaCor
        return self.cor

    def mostraCor(self):
        print(self.cor)

    #def retornarCor(self):
        #return self.cor

bola = Bola()
print(bola.circunferencia)
print(bola.cor)
bola.trocaCor('Azul')
bola.mostraCor()
#print(bola.retornarCor())
print(bola.cor)
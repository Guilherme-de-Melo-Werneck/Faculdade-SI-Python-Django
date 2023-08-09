'''
3.	Classe Retangulo: Crie uma classe que modele um retangulo:
a.	Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b.	Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c.	Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo:
    def __init__(self, base, altura):
        self.tamanhoBase = base
        self.tamanhoAltura = altura

    def mudarValorLados(self, base, altura):
        self.tamanhoLados = base, altura
    
    def retornarValorLados(self):
        return self.tamanhoLados

    def calculoArea(self):
        return self.tamanhoBase * self.tamanhoAltura

    def calculoPerimetro(self):
        return 2 * (self.tamanhoBase + self.tamanhoAltura)

    


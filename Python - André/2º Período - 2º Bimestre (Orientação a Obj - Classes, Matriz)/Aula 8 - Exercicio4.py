'''
4.	Classe Pessoa: Crie uma classe que modele uma pessoa:
a.	Atributos: nome, idade, peso e altura
b.	Métodos: Envelhecer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def emagrecer(self, peso):
        self.peso = self.peso - peso
        return self.peso
    
    def engordar(self, peso):
        self.peso = self.peso + peso
        return self.peso

    def crescer(self, altura):
        self.altura = self.altura + altura
        return self.altura
    
    def envelhecer(self):
        self.idade = self.idade + 1

        if self.idade < 21:
            self.crescer(0.05)
            return self.idade

        return self.idade

while True:
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    peso = input('Digite o seu peso: ')
    altura = input('Digite a sua altura: ')

    pessoa = Pessoa(nome, idade, peso, altura)
    pessoa.envelhecer()
    
    print('-'*35)

    print(f'''
Nome: {pessoa.nome} 
Idade: {pessoa.idade}
Peso: {pessoa.peso} 
Altura: {pessoa.altura}
''')

    print('-'*35)



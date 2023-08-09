'''
7.	Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a.	Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos 
levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde,
ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''

class Tamagushi:
    def __init__(self, nome, idade, fome = 100, saude = 100):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def AlterarNome(self, alterarNome):
        self.nome = alterarNome
        return self.nome

    def Fome(self, novaFome):
        self.fome = novaFome
        return self.fome

    def Saude(self, vida):
        self.saude = vida
        return self.saude

    def Humor(self):
        if self.fome >= 70 and self.saude >= 70:
            return 'Estou feliz :D!'

        elif self.fome >= 50 and self.saude >= 50:
            return 'Não estou tão feliz :/'

        elif self.fome >= 30 and self.saude >= 30:
            return 'Estou muito bravo :('
        
        else:
            return 'ESTOU COM MUITA FOME E MUITO FRACO!'


nome = input('Digite o nome do seu Tamagushi: ')
idade = input('Digite a idade do seu Tamagushi: ')
Tamagoshi = Tamagushi(nome, idade)

while True:
    print(f'Tamagoshi - Nome: {Tamagoshi.nome}, Idade: {Tamagoshi.idade}')

    opcoes = input('''
O que você deseja fazer?
1 - Alterar Nome
2 - Ver Humor
3 - Alterar Saúde
4 - Alterar Fome
5 - Sair
> ''')

    if opcoes == '1':
        novoNome = input('Digite o novo nome do seu Tamagushi: ')
        Tamagoshi.AlterarNome(novoNome)

        print(f'Nome alterado! Novo nome: {Tamagoshi.nome}')
    
    elif opcoes == '2':
        print(f'{Tamagoshi.Humor()}')
    
    elif opcoes == '3':
        novaSaude = int(input('Digite a vida do Tamagushi: '))
        Tamagoshi.Saude(novaSaude)

        print('Saúde alterada com sucesso!')

    elif opcoes == '4':
        novaFome = int(input('Digite o nível de fome do Tamagushi: '))
        Tamagoshi.Fome(novaFome)

        print('Fome alterada com sucesso!')

    else:
        break




    

    
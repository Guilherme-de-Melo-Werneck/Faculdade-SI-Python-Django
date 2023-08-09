'''
10.	Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
a.	Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i.	tipoCombustivel.
ii.	valorLitro
iii. quantidadeCombustivel

b.	Possua no mínimo esses métodos:
i.	abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
ii.	abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
iii.	alterarValor( ) – altera o valor do litro do combustível.
iv.	alterarCombustivel( ) – altera o tipo do combustível.
v.	alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, qtdCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.qtdCombustivel = qtdCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor/self.valorLitro
        self.qtdCombustivel = self.qtdCombustivel - litros_abastecidos
        print(f'\nForam abastecidos {litros_abastecidos:.2f} litros pelo valor de R$ {valor:.2f}.')
        print(f'Sobrou na bomba {self.qtdCombustivel:.2f} litros de {self.tipoCombustivel}.')

    def abastecerPorLitro(self, litrosAbastecidos):
        valor = litrosAbastecidos * self.valorLitro
        self.qtdCombustivel = self.qtdCombustivel - litrosAbastecidos
        print(f'\nForam abastecidos {litrosAbastecidos:.2f} litros pelo valor de R$ {valor:.2f}.')
        print(f'Sobrou na bomba {self.qtdCombustivel:.2f} litros de {self.tipoCombustivel}.')
        
    def alterarValorLitro(self, alterarValor):
        self.valorLitro = alterarValor
        return self.valorLitro

    def alterarCombustivel(self, alterarCombustivel):
        self.tipoCombustivel = alterarCombustivel
        return self.tipoCombustivel
    
    def alterarQuantidadeCombustivel(self, alterarQtd):
        self.qtdCombustivel = alterarQtd
        return self.qtdCombustivel

print('-' * 18)
print('Posto Santa Cruz')
print('-' * 18)

combustivel = str(input('Digite o tipo de combustível desejado: '))
valorL = float(input('Digite o valor do litro: '))
qtdC = int(input('Digite a quantidade de combustível disponível na bomba: '))

Bomba = BombaCombustivel(tipoCombustivel = combustivel, valorLitro = valorL, qtdCombustivel = qtdC)

while True:
    opcao = input('''
O que você deseja fazer?
1 - Abastecer por Valor
2 - Abastecer por Litro
3 - Alterar Valor do Litro
4 - Alterar tipo de Combustível
5 - Alterar Quantidade de Combustível na Bomba
6 - Sair
> ''')

    if opcao == '1':
        valor = int(input('\nDigite o valor a ser abastecido: ')) 
        Bomba.abastecerPorValor(valor)

    elif opcao == '2':
        litros = int(input('\nDigite a quantidade em litros a ser abastecido: '))
        Bomba.abastecerPorLitro(litros)

    elif opcao == '3':
        alterar = int(input('\nDigite o novo valor: '))
        Bomba.alterarValorLitro(alterar)

    elif opcao == '4':
        alterarTCombustivel = str(input('\nDigite o tipo de combustível: '))
        Bomba.alterarCombustivel(alterarTCombustivel)

    elif opcao == '5':
        alterarQtd = int(input('\n> Digite a quantidade que deseja alterar: '))
        Bomba.alterarQuantidadeCombustivel(alterarQtd)

    else:
        break

    


    




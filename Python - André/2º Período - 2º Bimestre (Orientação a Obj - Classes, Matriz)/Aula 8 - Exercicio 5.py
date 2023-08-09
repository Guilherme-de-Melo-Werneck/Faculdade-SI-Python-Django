'''
5.	Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''

class ContaCorrente:
    #É possível também colocar saldo = 0 nos parâmetros (atributos) do __init__
    def __init__(self, numConta, nome, saldo = 0):
        self.numConta = numConta
        self.nome = nome
        self.saldo = saldo

    def alterarNome (self, novoNome):
        self.nome = novoNome
        return self.nome
    
    def deposito (self, valorDeposito):
        self.saldo = self.saldo + valorDeposito
        return self.saldo

    def saque (self, valorSaque):
        self.saldo = self.saldo - valorSaque
        return self.saldo

conta = ContaCorrente(777, 'Flávio Novaes')
conta.alterarNome('Guerri')
print(conta.__dict__)

conta.deposito(250)
print(conta.__dict__)

conta.saque(50)
print(conta.__dict__)
    
class Pessoa:
    def __init__(self,nome,idade,peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1

        if self.idade < 21:
            self.crescer(0.5)
            return self.idade

        return self.idade
    
    def engordar(self, peso):
        self.peso = self.peso + peso
        return self.peso
    
    def emagrecer(self, peso):
        self.peso = self.peso - peso
        return self.peso

    def crescer(self, altura):
        self.altura = self.altura + altura
        return self.altura

Yann = Pessoa('Yann', 19, 68, 1.76)
print(Yann.__list__)
print(f'seu nome é {Yann.nome}, você tem {Yann.idade} anos, pesa {Yann.peso} kgs e tem uma altura de {Yann.altura}')
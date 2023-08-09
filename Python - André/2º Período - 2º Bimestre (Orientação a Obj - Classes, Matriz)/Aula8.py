class Cachorro:
  def __init__(self, raca, cor, peso, idade, nome):
    self.raca = raca
    self.cor = cor
    self.peso = peso
    self.idade = idade
    self.nome = nome

#Abaixo temos uma instância (transforma a classe em obj)
dog = Cachorro('Golden Retriever', 'Bronze', '60', '5', 'Moira')

print(dog.raca, dog.cor, dog.peso, dog.idade, dog.nome)
'''
6.Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e 
aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''

class TV:
    def __init__(self, canal, volume = 50):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, novoCanal):
        self.canal = novoCanal
        return self.canal
    
    def aumentarVolume (self, aVolume):
        self.volume = self.volume + aVolume
        return self.volume
    
    def abaixarVolume (self, abVolume):
        self.volume = self.volume - abVolume
        return self.volume

televisao = TV(2)
televisao.mudarCanal(3)
televisao.aumentarVolume(5)

print(televisao.__dict__)


    


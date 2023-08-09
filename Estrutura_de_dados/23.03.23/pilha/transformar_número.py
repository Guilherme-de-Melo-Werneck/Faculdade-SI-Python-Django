#transformar número decimal em binário usando pilha

class Pilha:
  def __init__(self):
    self.__info = []
  
  def pilhaVazia(self):
    return len(self.__info) == 0

  def push(self, dado):
    self.__info.append(dado)

  def pop(self):
    if not self.pilhaVazia():
      return self.__info.pop()
    else:
      return None 


p = Pilha()
x = int(input('Digite um número: '))
while x > 0:
    p.push(x%2)
    x=x//2
s=''
while not p.pilhaVazia():
   s = s + str(p.pop())

print(s)
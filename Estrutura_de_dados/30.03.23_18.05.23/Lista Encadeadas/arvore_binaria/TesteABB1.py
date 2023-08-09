from ArvoreBB import ArvoreBuscaBinaria

arv = ArvoreBuscaBinaria()
# x = int(input("Digite o valor da Chave (-1 para sair): "))
# while x != -1:
#   arv.insereNo(x)
#   print("Arvore: ")
#   arv.emOrdem(arv.getRaiz())
#   x = int(input("Digite o valor da Chave (-1 para sair): "))
# k=[10,11,15,17,13,4,7,5,2]
# k = [8,12,14,15,13,10,11,9,4,6,7,5,2,3,1]
k = [7,8,9,3,5,4,0]
for i in k:
    arv.insereNo(i)
    

print("Em Ordem")
arv.emOrdem(arv.getRaiz())

print("Pre Ordem")
arv.preOrdem(arv.getRaiz())

print("Pos Ordem")
arv.posOrdem(arv.getRaiz())

# print("Ordem Decrescente")
# arv.emOrdemDecrescente(arv.getRaiz())

# print("Buscar Valor")
# print(arv.BuscarValor(arv.getRaiz(), 15))

# print("ContarElementos")
# print(arv.ContarElementos(arv.getRaiz()))

# print("SomarElementos")
# print(arv.SomarElementos(arv.getRaiz()))

# print("Menor Valor")
# print(arv.EncontrarMenorValor(arv.getRaiz()))

# print("Maior valor")
# print (arv.EncontrarMaiorValor(arv.getRaiz()))


# arv = ArvoreBuscaBinaria()
# k = [8,3,12,1,5,9,17,4,11,14,19,13,15]
# for i in k:
#     arv.insereNo(i)                                  #7
# f = []
# f.append (arv.getRaiz())
# while len(f)>0:
#     atual = f.pop(0)
#     print(atual.getDados().getChave())
#     if atual.getFilhoEsquerda() !=None:
#         f.append(atual.getFilhoEsquerda())
#     if atual.getFilhoDireita() !=None:
#         f.append(atual.getFilhoDireita()) 

 
# arv = ArvoreBuscaBinaria()
# k = [8, 3, 12, 1, 5, 9, 17,4,11,14,19,13,15]
# f = []
# nivel = []

# for i in k:
#   arv.insereNo(i)
# nivel.append(0)
# f.append(arv.getRaiz())

# while len(f) > 0:
#   atual = f.pop(0)
#   nAtual = nivel.pop(0)                                  #7 mostrando os nível
#   print(nAtual, '-', atual.getDados().getChave())
#   if atual.getFilhoEsquerda()!=None:
#     f.append(atual.getFilhoEsquerda())
#     nivel.append(nAtual + 1)
#   if atual.getFilhoDireita()!=None:
#     f.append(atual.getFilhoDireita())
#     nivel.append(nAtual + 1)


# arv = ArvoreBuscaBinaria()
# k = [8,3, 12, 1, 5, 9, 17,4,11,14,19,13,15]
# f = []
# fn = []
# for i in k:
#   arv.insereNo(i)
# #arv.decrescente(arv.getRaiz())
# arv.Espelho(arv.getRaiz())
# f.append(arv.getRaiz())
# fn.append(0)                          #inversa
# while len(f) > 0:
#   atual = f.pop(0)
#   nAtual = fn.pop(0)
#   print(nAtual, "-", atual.getDados().getChave())
#   if atual.getFilhoEsquerda()!=None:
#     f.append(atual.getFilhoEsquerda())
#     fn.append(nAtual+1)
#   if atual.getFilhoDireita()!=None:
#     f.append(atual.getFilhoDireita())
#     fn.append(nAtual+1)
# arv.emOrdem(arv.getRaiz())

# print("prova")
# arv.q3(arv.getRaiz())


            
        






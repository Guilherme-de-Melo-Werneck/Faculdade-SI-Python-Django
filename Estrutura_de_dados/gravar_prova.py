#folha
# def q6(self,n):
#     if n.folha():
#         return 1
#     else:
#         return self.q6(n.FE() + n.FD())

def Folha(self,n):
    if n.folha():
        return 1
    else:
        return self.Folha(n.FE()) + self.Folha(n.FD())

    

# def insere(self, pai, atual, v):
#         if atual != None:
#             if v < atual.getDados().getChave(): # Alteração do elemento
#                 self.insere(atual, atual.getFilhoEsquerda(), v)
#             else:
#                 self.insere(atual, atual.getFilhoDireita(), v)
#         else:
#             x = self.criaNo(v)
#             if v < pai.getDados().getChave():
#                 pai.setFilhoEsquerda(x)
#             else:
#                 pai.setFilhoDireita(x)


#     def emOrdem(self, n):
#         if n != None:                                      #print o filho a esquerda, print o pai e o filho a direita
#             self.emOrdem(n.getFilhoEsquerda())
#             print(n.getDados().getChave())
#             self.emOrdem(n.getFilhoDireita())


def eo(self,n):
    if n!=None:
        self.eo(n.getFD())
        print(n.getdados().getchave())
        self.eo9(n.getFD())


    
#     def preOrdem(self, n):
#         if n != None:
#             print(n.getDados().getChave())              # print a raiz e vai printando pra esquerda
#             self.preOrdem(n.getFilhoEsquerda())             
#             self.preOrdem(n.getFilhoDireita())

def preo(self,n):
    print(n.getdados().getchave())
    self.preo(n.getFE())
    self.preo(n.getFD())




#     def posOrdem(self, n):
#         if n != None:
#             self.posOrdem(n.getFilhoEsquerda())
#             self.posOrdem(n.getFilhoDireita())          
#             print(n.getDados().getChave())

def poso(self,n):
    self.poso(n.getdados().getchave())
    self.poso(n.getchave().getchave())
    print(n.getdados().getchave())




#     def emOrdemDecrescente(self, n):                              #1
#         if n != None:
#             self.emOrdemDecrescente(n.getFilhoDireita())
#             print(n.getDados().getChave())
#             self.emOrdemDecrescente(n.getFilhoEsquerda())

def eod(self,n):
    self.eod(n.getFD())
    print(n.getdados().getchave())
    self.eod(n.getFE())


#     def BuscarValor(self, n, v):                                   #2
#         if n != None:
#             if v == n.getDados().getChave():
#                 return True
#             elif v < n.getDados().getChave():
#                 return self.BuscarValor(n.getFilhoEsquerda(),v)
#             else:
#                 return self.BuscarValor(n.getFilhoDireita(), v)
#         return False

def bcv(self,n,v):
    if n!=None:
        if v==n.getdados().getchave():
            return True
        elif v<n.getdados().getchave():
            return self.bcv(n.getFE())
        else:
            return self.bcv(n.getFD())
    return False


        
            
#     def ContarElementos(self,n):                                 #3
#         if n is None:
#             return 0
#         else:
#             return 1 + self.ContarElementos(n.getFilhoEsquerda()) + self.ContarElementos(n.getFilhoDireita())

def ce(self,n):
    if n!=None:
        return 0
    else:
        return 1+self.ce(n.getFE())+ self.ce(n.FD())



        
        
#     def SomarElementos(self,n):                                  #4
#         if n is None:
#             return 0 
#         return n.getDados().getChave() + self.SomarElementos(n.getFilhoEsquerda()) + self.SomarElementos(n.getFilhoDireita())

def se(self,n):
    if n!=None:
        return 0
    else:
        return n.getdados().getchave()+self.se(n.getFE())+self.se(n.getFD())



    
#     def EncontrarMenorValor(self, n):                           #5
#         if n.getFilhoEsquerda() != None:
#             return self.EncontrarMenorValor(n.getFilhoEsquerda())
#         elif n != None:
#             return n.getDados().getChave()
#         else:
#             return None

def emev(self,n):
    if n.get(n.FE())!=None:
        return self.emev(n.getFE())
    elif n!=None:
        return n.getdados().getchave()
    else:
        None


    
#     def EncontrarMaiorValor(self, n):                           #6
#         if n.getFilhoDireita() != None:
#             return self.EncontrarMaiorValor(n.getFilhoDireita())
#         elif n != None:
#             return n.getDados().getChave()
#         else:
#             return None

def emav(self,n):
    if n.get(n.getFD())!=None:
        return self.emav(n.getFD())
    elif n!=None:
        return n.getdados().getchave()
    else:
        None

   
#     def Espelho(self, n):
#         if n != None:
#             self.Espelho(n.getFilhoEsquerda())
#             self.Espelho(n.getFilhoDireita())            #inverter
#             fe = n.getFilhoEsquerda()
#             fd = n.getFilhoDireita()
#             n.setFilhoEsquerda(fd)
#             n.setFilhoDireita(fe)

def espelho(self,n):
    if n!=None:
        self.espelho(n.getFE())
        self.espelho(n.FD())
        fe = n.get(n.FE())
        fd = n.get(n.getFD())
        n.set(n.FE(fd))
        n.set(n.FD(fe))



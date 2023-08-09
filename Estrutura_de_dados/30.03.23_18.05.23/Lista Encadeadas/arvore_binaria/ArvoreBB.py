from NoABB import No
class ArvoreBuscaBinaria:
    def __init__(self):
        self.__raiz = None
    def getRaiz(self):
        return self.__raiz
    def setRaiz(self, n):
        self.__raiz = n
    def arvoreVazia(self):
        return self.__raiz == None
    def criaNo(self, v):
        no = No()
        no.getDados().setChave(v)
        return no
    def insereNo(self, v):
        if self.arvoreVazia():
            self.setRaiz(self.criaNo(v))
        else:
            self.insere(None, self.getRaiz(), v)
    def insere(self, pai, atual, v):
        if atual != None:
            if v < atual.getDados().getChave(): # Alteração do elemento
                self.insere(atual, atual.getFilhoEsquerda(), v)
            else:
                self.insere(atual, atual.getFilhoDireita(), v)
        else:
            x = self.criaNo(v)
            if v < pai.getDados().getChave():
                pai.setFilhoEsquerda(x)
            else:
                pai.setFilhoDireita(x)
    def emOrdem(self, n):
        if n != None:                                      #print o filho a esquerda, print o pai e o filho a direita
            self.emOrdem(n.getFilhoEsquerda())
            print(n.getDados().getChave())
            self.emOrdem(n.getFilhoDireita())
    
    def preOrdem(self, n):
        if n != None:
            print(n.getDados().getChave())              # print a raiz e vai printando pra esquerda
            self.preOrdem(n.getFilhoEsquerda())             
            self.preOrdem(n.getFilhoDireita())

    def posOrdem(self, n):
        if n != None:
            self.posOrdem(n.getFilhoEsquerda())
            self.posOrdem(n.getFilhoDireita())          
            print(n.getDados().getChave())

    def emOrdemDecrescente(self, n):                              #1
        if n != None:
            self.emOrdemDecrescente(n.getFilhoDireita())
            print(n.getDados().getChave())
            self.emOrdemDecrescente(n.getFilhoEsquerda())

    def BuscarValor(self, n, v):                                   #2
        if n != None:
            if v == n.getDados().getChave():
                return True
            elif v < n.getDados().getChave():
                return self.BuscarValor(n.getFilhoEsquerda(),v)
            else:
                return self.BuscarValor(n.getFilhoDireita(), v)
        return False
    
    def ContarElementos(self,n):                                 #3
        if n is None:
            return 0
        else:
            return 1 + self.ContarElementos(n.getFilhoEsquerda()) + self.ContarElementos(n.getFilhoDireita())
        
    def SomarElementos(self,n):                                  #4
        if n is None:
            return 0 
        else:
            return n.getDados().getChave() + self.SomarElementos(n.getFilhoEsquerda()) + self.SomarElementos(n.getFilhoDireita())
    

    def EncontrarMenorValor(self, n):                           #5
        if n.getFilhoEsquerda() != None:
            return self.EncontrarMenorValor(n.getFilhoEsquerda())
        elif n != None:
            return n.getDados().getChave()
        else:
            return None
        
    
    def EncontrarMaiorValor(self, n):                           #6
        if n.getFilhoDireita() != None:
            return self.EncontrarMaiorValor(n.getFilhoDireita())
        elif n != None:
            return n.getDados().getChave()
        else:
            return None
    
    def Espelho(self, n):
        if n != None:
            self.Espelho(n.getFilhoEsquerda())
            self.Espelho(n.getFilhoDireita())            #inverter
            fe = n.getFilhoEsquerda()
            fd = n.getFilhoDireita()
            n.setFilhoEsquerda(fd)
            n.setFilhoDireita(fe)

    
    

    


            

        

        
             
       
        
        
            
            


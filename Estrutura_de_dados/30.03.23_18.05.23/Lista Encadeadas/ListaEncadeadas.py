from No import No

class ListaEncadeadas:
    def __init__(self):
        self.__cabeca = No()
    
    def listaVazia(self):
        # return self.__cabeca.getProximo() == None
        return self.getCabeca().getProximo() == None
    
    def getCabeca(self):
        return self.__cabeca
    
    def setCabeca(self, valor):
        self.__cabeca = valor

    def insereNoInicio(self,n):
        # n.setProximo(self.__cabeca.getProximo())          #aula 6.04.23
        n.setProximo(self.getCabeca().getProximo()) 
        self.__cabeca.setProximo(n)
    
    def retiraNoInicio(self):
        ret = None
        if not self.listaVazia():
            ret = self.getCabeca().getProximo()              #aula 6.04.23
            self.getCabeca().setProximo(ret.getProximo())
            ret.setProximo(None)

        return ret
    
    def insereNoFim(self,n):
        ant = self.getCabeca()                              #aula 6.04.23
        atu = self.getCabeca().getProximo()
        while atu != None:
            ant = atu
            atu = atu.getProximo()
        ant.setProximo(n)

    
    def retiraNoFim(self,n):
        ret = None                              
        if not self.listaVazia():
            ant = self.getCabeca()                              #aula 6.04.23
            atu = self.getCabeca().getProximo()
            while atu.getProximo() != None:
                ant = atu
                atu = atu.getProximo()
            ret = atu
            ant.setProximo(None)
        return ret
    
    def insereOrdenado(self, n):
        ant = self.getCabeca()
        atual = self.getCabeca().getProximo()                                        #aula 4.05.23
        while atual != None and atual.getDados().getChave() < n.getDados().getChave():  
            ant = atual
            atual = atual.getProximo()
        n.setProximo(atual)
        ant.setProximo(n)

    def retiraElemento(self, x):
        ret = None
        if not self.listaVazia():
            ant = self.getCabeca()
            atu = self.getCabeca().getProximo()
            while atu != None and atu.getDados().getChave() != x:          #aula 4.05.23
                ant = atu
                atu = atu.getProximo()
            if atu != None:
                ant.setProximo(atu.getProximo())
                atu.setProximo(None)
            ret = atu
        return ret

    def mostraLista(self):
        atual = self.getCabeca().getProximo()                        #aula 6.04.23
        while atual !=None:
            print(atual.getDados().getValores())
            atual = atual.getProximo()
    
    def tamanho (self):
        ret = 0 
        atu = self.getCabeca().getProximo()
        while atu!=None:                                      #exercício 3
            ret = ret + 1 
        return ret
    
    def mostraRec(self,n):
        if n !=None:
            print(n.getDados().getValores())                 #exercício 4
            self.mostraRec(n.getProximo())

    def mostraRecinv(self,n):
        if n !=None:
            self.mostrarecinv(n.getproximo())              #exercício 5
            print(n.getDados().getValores())
            

    
        

    
    
    

        
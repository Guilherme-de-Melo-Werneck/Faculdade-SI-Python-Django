def mostraRec(self,n):
        if n !=None:
            print(n.getDados().getValores())                 
            self.mostraRec(n.getProximo())
def mostraRecinv(self,n):
        if n !=None:
            self.mostrarecinv(n.getproximo())             
            print(n.getDados().getValores())
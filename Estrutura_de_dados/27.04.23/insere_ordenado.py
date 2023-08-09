def insereOdernado(self,n):
    ant = self.getCabeca()
    atu = self.getCabeca().getProximo()
    while atu !=None and atu.getDados().getChave()<n.getDados(). getChave():
        ant = atu
        atu = atu.getProximo()

    ant.setProximo(n)
    n.setProximo(atu)
def retiraElemento(self,x):
    ret = None
    if not self.listavazia():
        ant = self.getCabeca()
        atu = self.getCabeca().getProximo()
        while atu!=None and atu.getDados().getChave()!= x:
            ant = atu
            atu = atu.getProximo()
        if atu!=None:
            ant.setProximo(atu.getProximo())
            atu.setProximo(None)
        ret = atu
    return ret
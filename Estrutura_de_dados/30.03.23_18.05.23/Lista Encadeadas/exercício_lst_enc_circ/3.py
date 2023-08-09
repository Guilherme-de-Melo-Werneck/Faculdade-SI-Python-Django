def tamanho (self):
        ret = 0 
        atu = self.getCabeca().getProximo()
        while atu!=None:                                     
            ret = ret + 1 
        return ret
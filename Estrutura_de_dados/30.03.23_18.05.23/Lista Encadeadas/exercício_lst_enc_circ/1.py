from ListaEncadeadas import ListaEncadeadas
class PilhaEncadeada(ListaEncadeadas):
    def pilhaVazia(self):
        return self.listaVazia()
    
    def push(self,n):
        self.insereNoInicio()

    def pop(self,n):
        self.retiraNoInicio()
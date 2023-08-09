def mostraLista(self):
		atual = self.getCabeca().getProximo()
		while atual != None:
			print(atual.getDados().getValores())
			atual = atual.getProximo()
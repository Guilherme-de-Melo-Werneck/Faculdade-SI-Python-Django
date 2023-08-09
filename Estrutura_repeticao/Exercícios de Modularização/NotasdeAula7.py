#7)	Crie uma função que, dada uma cadeia, imprima cada letra da cadeia em uma linha. Esta função deverá ser chamada de umaLetraPorLinha(cadeia).

def umaLetraPorLinha(cadeia):
    for c in cadeia:
        print(c)

cadeia = str(input('Digite uma palavra: '))

umaLetraPorLinha(cadeia)

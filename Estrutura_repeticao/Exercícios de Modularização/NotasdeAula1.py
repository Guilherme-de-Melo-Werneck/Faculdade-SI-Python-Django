'''
1) Escrever um programa para imprimir o cabeçalho:

IFRJ – Técnico em Informática
xx/xx/xxxx		    Pág. 9999

'''

def cabecalho(data,pag):
    Pag = str('Pág')
    print(f'IFRJ - Técnico em Informática \n{data} {Pag:>15} {pag:>1}')
    
    '''
    ou apague o \n e adicione outro print embaixo (acho mais organizado):
    print(f'{data} {Pag:>16} {pag:>1}')
    '''

cabecalho('08/06/2022', 30)

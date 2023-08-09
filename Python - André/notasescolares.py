nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))
nota5 = float(input('Informe a quinta nota: '))

media = (nota1+nota2+nota3+nota4+nota5)/5

if media >= 7:
    print(f'Sua média foi {media} \nVocê foi aprovado!')
else:
    print(f'Sua média foi {media} \nVocê deverá fazer o exame!')
    
    notaexame = float(input('Informe a nota do exame: '))    
    mediaexame = (media+notaexame)/2
    
    if mediaexame >= 5: 
        print(f'Aprovado em exame com nota {mediaexame}')
    else:
        print(f'Reprovado com nota {mediaexame}')



   



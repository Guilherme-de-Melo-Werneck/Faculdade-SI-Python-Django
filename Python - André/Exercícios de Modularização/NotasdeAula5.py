# 5) Crie um algoritmo que solicite ao usuário informar a temperatura em graus Celsius e retorne a mesma em Fahrenheit, calculando o resultado na função fahrenheit(temp).

def fahrenheit(temp):
    return temp * 1.8 + 32

temp = float(input('Digite a temperatura em Celsius: '))
print(f'A temperatura {temp}° em Fahrenheit é: {fahrenheit(temp)}°')
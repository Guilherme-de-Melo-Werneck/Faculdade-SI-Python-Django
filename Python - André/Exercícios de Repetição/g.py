# Potências na base 3

base = 3

for num in range(0,16):
    resultado = base ** num      
    print(f'{base}^{num} = {resultado:,}')

print()

# While

num = 0

while num <= 15:
    resultado = base ** num
    print(f'{base}^{num} = {resultado:,}')    
    
    num = num + 1
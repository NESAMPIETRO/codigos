# controlar looping

for variavel in range(5):
    print(variavel)
    
# comecar a partir de 1
    
for variavel in range(1, 5):
    print(variavel)  

# intervalos de 3 numeros 
    
for variavel in range(1, 12, 3):
    print(variavel)

# somar 3 notas e tirar a media

soma = 0 
for i in range(1, 4):
    nota = float(input(f"Informe sua nota {i}: "))
    
    soma = soma + nota

print(soma / 3)
     
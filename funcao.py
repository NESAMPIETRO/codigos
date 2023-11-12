# funções

# 1 o  que sao funções e por que utiliza-las 

# funções que ja utilizamos anteriormente 
"""
print() # imprimi uma mensagem ( float , int, str) no console original ( termninal ou cmd )
input() # retorna um dado infomado pelo usuario ( entrada padrao ) e pode receber um stringer 
len() # recebe uma lista e retorna o tamanho dessa lista 
max() # retorna o maior valor de uma lista """

# 2 criação de funções 

# função inicial 

def saudacao(): 
    print("Seja bem vindo")
    print("É um prazer ter você fazendo parte desse curso !")
    
saudacao()

# função com parametros 

def saudacao(nome, curso):
    print(f"Seja bem vindo, {nome}")
    print(f"É um prazer ter você fazendo parte do curso de {curso}!")
    
saudacao("Rodrigo", "Python")    
saudacao("Rosa", "Culinaria")

# funcao com parametros default

def saudacao(nome, curso="Python"): # criando valor padrao para o nome do curso
    print(f"Seja bem vindo, {nome}")
    print(f"É um prazer ter você fazendo parte do curso de {curso}!")
    
saudacao("Rodrigo")    

# funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print("O resultado da soma é", resultado)

def calculadora(num1, num2, operacao="+"):
    if operacao == "+":
        return num1 + num2 
    elif operacao == "-":
        return num1 - num2
   
resultado = calculadora(10, 20, "+")    

print(resultado)
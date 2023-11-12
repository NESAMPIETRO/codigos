#  dicionarios 
# criando dicionarios 
dicionario = {}
dicionario = dict()

dicionario = { "nome": "Rodrigo", "idade": 47, "altura": 1.70 }
print(dicionario)
print(dicionario["idade"])

# adicionando elementos no docionario 

dicionario["programador"] = True

print(dicionario)

dicionario["altura"] = 2

print(dicionario)

# Iterando um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])
    
    
    # Testando a existencia de uma chave 
    
print("peso" in dicionario)    
print("altura" in dicionario)    


numeros = []

for _ in range(5):
  numero = int(input('Digite um número inteiro: '))
  numeros.append(numero)

# SOMA METODO 1
# soma = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]
# SOMA METODO 2
soma = sum(numeros)
# SOMA METODO 3
# soma = 0
# for numero in numeros:
#   soma += numero

# MULTIPLICACAO METODO 1
# multiplicacao = numeros[0] * numeros[1] * numeros[2] * numeros[3] * numeros[4]
# MULTIPLICACAO METODO 2
multiplicacao = 1
for numero in numeros:
  multiplicacao *=numero

print(numeros)
print(soma)
print(multiplicacao)
  
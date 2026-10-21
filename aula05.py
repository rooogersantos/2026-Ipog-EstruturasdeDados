# PROCEDIMENTO
def saudacao (texto):
    print(texto)

saudacao('Olá, mundo!')
saudacao('Roger é um viadinho!')


# FUNÇÃO
def potencia(num, potencia):
    return num ** potencia

resultado = potencia(2, 3)
print(resultado)


# PONTEIROS
a = 5
b = a # Atribuição por referência

print(a) # Saída 5
print(b) # Saída 5

a = 10 # Modificando o valor de a

print(a) # Saída 10
print(b) # Saída 5


# RECURSIVIDADE
# Fatorial
# 5! = 5 X 4 X 3 x 2 x 1 = 120

def fatorial(num):
    result = 1
    for x in range(1, num +1):
        result = result * x
    return result
teste01 = fatorial(5)
print(teste01)

def fatorial_recursivo(num):
    if num == 0:
        return 1
    else:
        return num * fatorial_recursivo(num - 1)
teste02 = fatorial_recursivo(5)
print(teste02)
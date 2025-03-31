import math

def is_perfect_square(x):
    return int(math.sqrt(x))**2 == x

def is_fibonacci(num):
    if num < 0:
        return False
    return is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci!")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

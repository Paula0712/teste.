def fibonacci_check(num):
    a, b = 0, 1
    # Gerar a sequência até que um número maior ou igual ao num seja alcançado
    while b < num:
        a, b = b, a + b
    # Verificar se o número é igual a 'b', que está na sequência
    if b == num or num == 0:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de entrada
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(fibonacci_check(numero))

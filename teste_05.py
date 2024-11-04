# Função para inverter uma string
def inverter_string(s):
    string_invertida = ""  # Inicializa a string invertida como vazia
    # Loop para percorrer a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  # Adiciona o caractere na nova string
    return string_invertida  # Retorna a string invertida

# Solicita que o usuário digite uma string
entrada = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada)  # Chama a função para inverter a string

# Exibe o resultado
print("String invertida:", resultado)

def calcular_faturamento() :
    # Dados de faturamento diário diretamente no código
    dados = [
        {"dia" : 1, "valor" : 1000.0},
        {"dia" : 2, "valor" : 2500.0},
        {"dia" : 3, "valor" : 0.0},
        {"dia" : 4, "valor" : 3200.0},
        {"dia" : 5, "valor" : 0.0},
        {"dia" : 6, "valor" : 4300.0},
        {"dia" : 7, "valor" : 2900.0}
        # ... mais dias do mês
    ]

    # Filtrar os valores de faturamento positivo (dias úteis)
    faturamento_diario = [dia["valor"] for dia in dados if dia["valor"] > 0]

    # Calcular o menor e maior faturamento
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)

    # Calcular a média e dias acima da média
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    dias_acima_media = len([valor for valor in faturamento_diario if valor > media_mensal])

    # Exibir resultados
    print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")


# Executar a função
calcular_faturamento()

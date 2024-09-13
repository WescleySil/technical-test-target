import json

# Função para calcular os valores desejados
def calcular_faturamento(dados):
    valores = [item['valor'] for item in dados if item['valor'] > 0]

    if not valores:
        return "Não há faturamento para calcular."

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)

    dias_acima_da_media = sum(1 for item in dados if item['valor'] > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

# Função principal para ler o arquivo JSON e calcular os valores
def main():
    # Substitua 'faturamento.json' pelo caminho do seu arquivo JSON
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)["faturamento"]

    resultados = calcular_faturamento(dados)

    print(f"Menor valor de faturamento: {resultados['menor_faturamento']}")
    print(f"Maior valor de faturamento: {resultados['maior_faturamento']}")
    print(f"Número de dias com faturamento acima da média:             {resultados['dias_acima_da_media']}")

if __name__ == "__main__":
    main()

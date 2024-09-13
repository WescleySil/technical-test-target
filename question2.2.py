import xml.etree.ElementTree as ET


def processar_faturamento(arquivo_xml):
    try:
        # Parse o arquivo XML
        tree = ET.parse(arquivo_xml)
        root = tree.getroot()
    except ET.ParseError as e:
        return f"Erro ao parsear o arquivo XML: {e}"

    # Lista para armazenar os valores de faturamento
    valores = []

    # Itera sobre cada elemento <row> no XML
    for row in root.findall('row'):
        try:
            valor = float(row.find('valor').text)
            if valor > 0:
                valores.append(valor)
        except (ValueError, AttributeError) as e:
            return f"Erro ao processar os valores do XML: {e}"

    if not valores:
        return "Não há dados de faturamento válidos."

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)

    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }


def main():
    # Substitua 'faturamento.xml' pelo caminho do seu arquivo XML
    arquivo_xml = './dados.xml'

    resultados = processar_faturamento(arquivo_xml)

    if isinstance(resultados, dict):
        print(
            f"Menor valor de faturamento: {resultados['menor_faturamento']:.2f}"
        )
        print(
            f"Maior valor de faturamento: {resultados['maior_faturamento']:.2f}"
        )
        print(
            f"Número de dias com faturamento acima da média: {resultados['dias_acima_da_media']}"
        )
    else:
        print(resultados)


if __name__ == "__main__":
    main()

import requests, json, datetime

# Data de início: 6 meses atrás
inicio = datetime.date.today() - datetime.timedelta(days=180)
fim = datetime.date.today()

# Laço para cada dia
for delta in range((fim - inicio).days + 1):
    dia = inicio + datetime.timedelta(days=delta)
    data_str = dia.strftime("%Y-%m-%d")
    # Exemplo de URL, adapta conforme a API real
    url = f"https://api.fogocruzado.org.br/v1/ocorrencias?cidade=Salvador&data={data_str}"
    try:
        resposta = requests.get(url)
        dados = resposta.json().get("resultados", [])
        arquivo = f"tiroteios_salvador_{data_str}.json"
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print(f"Salvo para {data_str}: {len(dados)} registros.")
    except Exception as e:
        print(f"Erro em {data_str}: {e}")

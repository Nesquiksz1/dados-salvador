import requests, json, datetime

# Chama a API do Fogo Cruzado (ou outra desejada)
url = "https://api.fogocruzado.org.br/v1/ocorrencias?cidade=Salvador"

data = requests.get(url).json()["resultados"]

# Gera nome do arquivo com a data do dia
hoje = datetime.date.today().strftime("%Y-%m-%d")
arquivo = f"tiroteios_salvador_{hoje}.json"

# Salva o arquivo localmente
with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Arquivo {arquivo} salvo com sucesso!")

# dados-salvador

Coleta diária automática e visualização de dados de tiroteios em Salvador via API Fogo Cruzado, sem banco de dados nem servidor.

## Arquivos e funções

- **`coletar.py`**: Faz a coleta dos dados do dia e salva em JSON.
- **`.github/workflows/update.yml`**: Automatiza a coleta e salva tudo no GitHub todo dia.
- **`index.html`**: Mostra os dados do dia na web, direto do JSON.
- **`README.md`**: Explica tudo de forma rápida.

## Como funciona

1. O GitHub Actions executa o `coletar.py` automaticamente todo dia.
2. O script salva um arquivo `tiroteios_salvador_YYYY-MM-DD.json` com os dados do dia.
3. O histórico de todos os dias fica salvo no repositório, sem banco nem backend.
4. O `index.html` exibe o total de ocorrências do dia, diretamente do arquivo.

## Como usar

1. Faça um fork/clonagem do repositório.
2. Habilite o GitHub Actions.
3. (Opcional) Rode o script manualmente com `python coletar.py`.
4. Abra `index.html` via GitHub Pages ou localmente.

## Observação

Fique à vontade para mudar a fonte de dados ou adaptar para outros usos!]

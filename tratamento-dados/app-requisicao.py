import requests
import json
import os
from datetime import datetime

#Conexões com o supabase
supabase_url = "https://klcbbojkwwwggysgunbs.supabase.co/rest/v1/dados_monitoramento"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtsY2Jib2prd3d3Z2d5c2d1bmJzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU4MDczNjIsImV4cCI6MjA3MTM4MzM2Mn0.nATTz99KeHvHmoV84pUdqiXl3_Ag0koFd6_DOutKfsE"

#Cabeçalhos obrigatórios
headers = {
    "apikey": supabase_key,
    "Authorization":f"Bearer {supabase_key}",
    "Content-Type": "application/json"
}

#Filtros - caso necessário
# params = {
# "id": "1", "2"...
# }
# response = requests.get(supabase_url, headers=headers, params=params)

#Respostas do supabase
response = requests.get(supabase_url, headers=headers)
codigo = response.status_code

#Estrutura de recebimento dos dados
pasta = "arquivos_json"
if codigo == 200:
    print(f"Dados recebidos com sucesso!")
    dados = response.json()
     
  #Caminho para salvar os arquivos
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    os.makedirs(pasta, exist_ok=True)
    nome_arquivo = f"dados_{timestamp}.json"
    print(f"{len(dados)} dados recebidos.")
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

  #salvando os dados em um único arquivo
    with open (caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f"Sucesso. Arquivo {nome_arquivo} salvo no diretório arquivos_json.")

else:
    print(f"Dados não recebidos. Erro {codigo}.")

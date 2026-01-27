import random
import time
import requests
import json
from datetime import datetime, timezone

# --- Config do Supabase ---
supabase_url = "https://klcbbojkwwwggysgunbs.supabase.co/rest/v1/dados_monitoramento"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtsY2Jib2prd3d3Z2d5c2d1bmJzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU4MDczNjIsImV4cCI6MjA3MTM4MzM2Mn0.nATTz99KeHvHmoV84pUdqiXl3_Ag0koFd6_DOutKfsE"  # RLS desativado, anon key suficiente

# --- Funções para gerar dados simulados ---
def gerar_temperatura(): return round(random.uniform(20.0, 30.0), 2)
def gerar_ph(): return round(random.uniform(6.5, 7.5), 2)
def gerar_pressao(): return round(random.uniform(1.0, 2.5), 2)
def gerar_nivel(): return round(random.uniform(0.0, 100.0), 1)
def gerar_vazao(): return round(random.uniform(10.0, 50.0), 2)

# --- Loop de envio de dados ---
INTERVALO = 5  # segundos entre cada envio

while True:
    dados = {
        "temperatura": gerar_temperatura(),
        "ph": gerar_ph(),
        "pressao": gerar_pressao(),
        "nivel": gerar_nivel(),
        "vazao": gerar_vazao(),
        "timestamp": datetime.now(timezone.utc).isoformat()  # timestamp seguro
    }
    
    #cabeçalhos obrigatórios
    headers = {
        "Content-Type": "application/json",
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}"
    }

    print("Dados gerados:", dados)

    # Inserir no Supabase
    response = requests.post(supabase_url, 
                             headers=headers,
                             data=json.dumps(dados))
    responseStatus = response.status_code
    # Verificar se os dados foram retornados (sucesso)
    if response.status_code == 201:
        print("Dados enviados com sucesso!")
    else:
        print(f"Erro ao enviar. Verifique a configuração da tabela. Código de erro: {responseStatus}")

    time.sleep(INTERVALO)


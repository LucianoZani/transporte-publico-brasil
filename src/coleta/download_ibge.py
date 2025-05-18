import os
import requests
from datetime import datetime

DATA_DIR = "../../data/external/ibge"
os.makedirs(DATA_DIR, exist_ok=True)

def download_populacao_municipios():
    url = "https://basedosdados-public.s3.amazonaws.com/dataset/ibge/populacao_municipio.csv"  # Exemplo fictício ou substituível por fonte real
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(DATA_DIR, f"populacao_municipios_{timestamp}.csv")

    print(f"Baixando dados de população IBGE para: {output_path}")
    r = requests.get(url)
    with open(output_path, "wb") as f:
        f.write(r.content)
    print("Download concluído.")

if __name__ == "__main__":
    download_populacao_municipios()

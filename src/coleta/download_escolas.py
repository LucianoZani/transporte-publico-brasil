import os
import requests
from datetime import datetime

DATA_DIR = "../../data/external/inep"
os.makedirs(DATA_DIR, exist_ok=True)

def download_localizacao_escolas():
    url = "https://inepdata.inep.gov.br/municipios/censo_escolar/localizacao_escolas.csv"  # Exemplo ilustrativo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(DATA_DIR, f"escolas_localizacao_{timestamp}.csv")

    print(f"Baixando localização das escolas para: {output_path}")
    r = requests.get(url)
    with open(output_path, "wb") as f:
        f.write(r.content)
    print("Download concluído.")

if __name__ == "__main__":
    download_localizacao_escolas()


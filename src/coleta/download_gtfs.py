import os
import requests
from datetime import datetime

# Pasta onde vamos salvar
DATA_DIR = "../../data/external/gtfs"
os.makedirs(DATA_DIR, exist_ok=True)

def download_gtfs_sptrans():
    url = "http://dados.mobilidade.rio/gps/gtfs.zip"  # Exemplo real, pode variar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(DATA_DIR, f"gtfs_rio_{timestamp}.zip")

    print(f"Baixando GTFS para: {output_path}")
    r = requests.get(url)
    with open(output_path, "wb") as f:
        f.write(r.content)
    print("Download concluído.")

if __name__ == "__main__":
    download_gtfs_sptrans()

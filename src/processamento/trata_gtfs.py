import zipfile
import os
import pandas as pd

INPUT_PATH = "../../data/external/gtfs"
OUTPUT_PATH = "../../data/processed_/gtfs"
os.makedirs(OUTPUT_PATH, exist_ok=True)

def extrair_gtfs_zip():
    arquivos_zip = [f for f in os.listdir(INPUT_PATH) if f.endswith(".zip")]
    if not arquivos_zip:
        print("Nenhum arquivo ZIP encontrado.")
        return

    zip_mais_recente = sorted(arquivos_zip)[-1]
    zip_path = os.path.join(INPUT_PATH, zip_mais_recente)
    print(f"Extraindo {zip_path}...")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(OUTPUT_PATH)
    
    print(f"Arquivos extraídos para {OUTPUT_PATH}")

if __name__ == "__main__":
    extrair_gtfs_zip()

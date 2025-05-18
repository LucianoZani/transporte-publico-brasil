import pandas as pd
import os

INPUT_PATH = "../../data/external/inep"
OUTPUT_PATH = "../../data/processed_"
os.makedirs(OUTPUT_PATH, exist_ok=True)

def tratar_escolas():
    arquivos = [f for f in os.listdir(INPUT_PATH) if f.endswith(".csv")]
    if not arquivos:
        print("Nenhum arquivo CSV encontrado.")
        return

    arquivo_mais_recente = sorted(arquivos)[-1]
    caminho = os.path.join(INPUT_PATH, arquivo_mais_recente)
    print(f"Processando: {caminho}")

    df = pd.read_csv(caminho, encoding='latin1')

    df.columns = [col.lower().strip() for col in df.columns]

    col_lat = [col for col in df.columns if "latitude" in col][0]
    col_lon = [col for col in df.columns if "longitude" in col][0]
    col_nome = [col for col in df.columns if "escola" in col or "nome" in col][0]
    col_muni = [col for col in df.columns if "municipio" in col][0]

    df = df.rename(columns={
        col_nome: "nome_escola",
        col_lat: "latitude",
        col_lon: "longitude",
        col_muni: "municipio"
    })

    df = df[["nome_escola", "municipio", "latitude", "longitude"]]
    df = df.dropna()

    df.to_csv(os.path.join(OUTPUT_PATH, "escolas_tratadas.csv"), index=False)
    print("Salvo em data/processed/escolas_tratadas.csv")

if __name__ == "__main__":
    tratar_escolas()

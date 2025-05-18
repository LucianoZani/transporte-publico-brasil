import pandas as pd
import os

INPUT_PATH = "../../data/external/ibge"
OUTPUT_PATH = "../../data/processed_"
os.makedirs(OUTPUT_PATH, exist_ok=True)

def tratar_populacao():
    arquivos = [f for f in os.listdir(INPUT_PATH) if f.endswith(".csv")]
    if not arquivos:
        print("Nenhum arquivo CSV encontrado.")
        return

    arquivo_mais_recente = sorted(arquivos)[-1]
    caminho = os.path.join(INPUT_PATH, arquivo_mais_recente)
    print(f"Processando: {caminho}")

    df = pd.read_csv(caminho)

    # Exemplo de tratamento
    df = df.rename(columns={
        "municipio": "municipio",
        "ano": "ano",
        "populacao": "populacao"
    })

    df = df[df["ano"] == df["ano"].max()]  # Mantém apenas o ano mais recente
    df.to_csv(os.path.join(OUTPUT_PATH, "populacao_tratada.csv"), index=False)
    print("Arquivo salvo em data/processed/populacao_tratada.csv")

if __name__ == "__main__":
    tratar_populacao()

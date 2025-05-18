import pandas as pd
import os
from pathlib import Path

# Caminhos
RAW_DATA_DIR = Path("data/external/inep")
PROCESSED_DATA_DIR = Path("data/processed_")
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

def processar_arquivo_escola(filepath):
    print(f"Processando {filepath.name}...")
    df = pd.read_csv(filepath, sep=';', encoding='latin1', low_memory=False)

    # Exemplo: selecionando colunas relevantes
    colunas = [
        "ANO_CENSO", "ID_ESCOLA", "COD_MUNICIPIO", "UF", "NOME_DA_ESCOLA",
        "DEPENDENCIA_ADM", "LOCALIZACAO", "REGIAO", "SITUACAO_FUNCIONAMENTO"
    ]
    df = df[colunas]

    # Conversões / renomeações se necessário
    df.columns = [col.lower() for col in df.columns]

    return df

def processar_todos():
    arquivos = list(RAW_DATA_DIR.glob("*.csv"))
    if not arquivos:
        print("Nenhum arquivo CSV encontrado em data/external/inep/")
        return

    df_final = pd.concat([processar_arquivo_escola(fp) for fp in arquivos], ignore_index=True)
    df_final.to_csv(PROCESSED_DATA_DIR / "escolas_processado.csv", index=False, encoding="utf-8")
    print(f"Dados processados salvos em: {PROCESSED_DATA_DIR / 'escolas_processado.csv'}")

if __name__ == "__main__":
    processar_todos()

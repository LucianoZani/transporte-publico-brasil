# 5. Pipeline de Dados - Arquitetura e Execução

## 5.1 Visão Geral

O pipeline será dividido em cinco camadas principais, cada uma com responsabilidade clara e desacoplada. Isso garante manutenção simples, escalabilidade e governança eficiente dos dados.

## 5.2 Arquitetura do Pipeline

┌────────────────────┐
│ Camada 1: Coleta │
└────────────────────┘
│
▼
┌───────────────────────────────┐
│ Camada 2: Armazenamento Raw │
│ (/data/raw) │
└───────────────────────────────┘
│
▼
┌───────────────────────────────┐
│ Camada 3: Processamento │
│ (limpeza, padronização) │
└───────────────────────────────┘
│
▼
┌───────────────────────────────┐
│ Camada 4: Banco de Dados │
│ (PostgreSQL estruturado) │
└───────────────────────────────┘
│
▼
┌───────────────────────────────┐
│ Camada 5: Visualização │
│ (Power BI / Streamlit) │
└───────────────────────────────┘

## 5.3 Tecnologias por Camada

| Camada       | Tecnologias/Ferramentas        |
|--------------|-------------------------------|
| Coleta       | Python (requests, pandas), APIs, downloads |
| Armazenamento Raw | Sistema de arquivos local, Git LFS (se necessário) |
| Processamento | Pandas, GeoPandas, scripts ETL em Python |
| Banco de Dados | PostgreSQL (localhost ou em nuvem gratuita) |
| Visualização  | Power BI (dashboard oficial), Streamlit (opcional para deploy web) |

## 5.4 Estratégia de Execução

- Todos os scripts serão versionados em `/src`.
- A execução inicial será manual (via Jupyter ou script direto).
- Em etapas futuras, será possível automatizar com `Makefile`, agendamentos locais ou integração com Airflow.

## 5.5 Boas Práticas Adotadas

- **Separação de ambientes**: raw, processed e final.
- **Versionamento de scripts e dados**: Git.
- **Documentação contínua**: todos os dados e scripts terão README.
- **Reprodutibilidade**: pipeline pode ser executado por qualquer pessoa com os arquivos de entrada e scripts.
- **Logs**: serão gerados para etapas críticas (coleta e transformação).

## 5.6 Proposta de Pastas no Repositório

transporte-publico-brasil/
│
├── data/
│ ├── raw/ # dados originais
│ ├── processed/ # dados tratados
│ └── final/ # datasets prontos para análise
│
├── src/
│ ├── coleta/ # scripts de ingestão
│ ├── tratamento/ # scripts de limpeza e transformação
│ └── analise/ # scripts analíticos e geração de indicadores
│
├── docs/ # documentação do projeto
├── notebooks/ # exploração inicial e análises pontuais
└── dashboard/ # arquivos do Power BI
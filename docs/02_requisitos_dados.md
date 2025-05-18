# 2. Levantamento de Requisitos e Fontes de Dados

## 2.1 Requisitos Funcionais

- Coletar dados de mobilidade urbana com abrangência nacional.
- Integrar dados de diferentes fontes públicas (IBGE, dados abertos de transporte, APIs etc.).
- Limpar, padronizar e transformar os dados em um formato analisável.
- Criar um pipeline de dados robusto e automatizável.
- Construir visualizações interativas para análise e acompanhamento da demanda e oferta de transporte público.
- Produzir relatórios analíticos com recomendações por região.

## 2.2 Requisitos Não Funcionais

- O projeto deve ser desenvolvido utilizando ferramentas de código aberto.
- O pipeline deve permitir execução periódica (automatização futura via scheduler).
- A estrutura deve seguir boas práticas de Governança de Dados: rastreabilidade, documentação e versionamento.
- Os dados devem ser armazenados em banco relacional (PostgreSQL) e/ou em formato tabular (.csv/.parquet).
- Os scripts devem ser organizados em Jupyter Notebooks ou arquivos `.py` com versionamento via Git.

## 2.3 Fontes de Dados Planejadas

| Fonte | Descrição | Formato | Acesso |
|-------|-----------|---------|--------|
| [IBGE](https://www.ibge.gov.br/) | População por município, densidade demográfica | CSV / XLS | Download |
| [Dados Abertos Gov.br](https://dados.gov.br/) | Dados gerais de transporte, políticas públicas | CSV / API | Download/API |
| [Google Mobility Reports](https://www.google.com/covid19/mobility/) | Tendência de mobilidade por categoria e local | CSV | Download |
| [GTFS Brasil (MobilityData)](https://transitfeeds.com/) | Dados abertos de transporte público (rotas, horários, paradas) | GTFS (ZIP/CSV) | Download |
| [Censo Escolar INEP](https://inep.gov.br) | Dados sobre escolas e deslocamento de alunos | CSV / XLS | Download |

## 2.4 Dados Complementares (opcional)

- Dados de trânsito (Waze, MapLink, APIs municipais).
- Dados meteorológicos (INMET) para correlacionar com variações de demanda.
- Dados de eventos e sazonalidades locais.

## 2.5 Critérios para Seleção dos Dados

- Relevância para entender padrões de mobilidade.
- Abrangência nacional ou municipal com recorte por região.
- Frequência de atualização adequada (preferência por dados recentes ou históricos contínuos).
- Facilidade de acesso e uso permitido para fins de análise.

## 2.6 Possíveis Desafios

- Qualidade inconsistente ou dados desatualizados.
- Diferentes formatos e estruturas de arquivos.
- Falta de granularidade em regiões específicas.
- Restrições de acesso em algumas APIs ou bases protegidas.


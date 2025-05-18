# 4. Fontes de Dados e Estratégia de Coleta

## 4.1 IBGE - Dados Populacionais

- **Fonte**: [IBGE Cidades](https://cidades.ibge.gov.br/)
- **Formato**: CSV / XLS
- **Frequência**: Anual
- **Uso no Projeto**: Permite entender a distribuição populacional para avaliar cobertura e necessidade de transporte público por região.
- **Coleta**: Download manual inicialmente, com automação planejada.

## 4.2 Google Mobility Reports

- **Fonte**: [Google Mobility](https://www.google.com/covid19/mobility/)
- **Formato**: CSV
- **Frequência**: Atualizações semanais (em histórico)
- **Uso no Projeto**: Análise de variação de mobilidade ao longo do tempo por região.
- **Coleta**: Download manual, automatizável com Python.

## 4.3 GTFS - Dados de Transporte Público

- **Fonte**: [TransitFeeds](https://transitfeeds.com/) ou [MobilityData GTFS](https://github.com/MobilityData)
- **Formato**: ZIP (com arquivos CSV dentro)
- **Frequência**: Varia por cidade
- **Uso no Projeto**: Estrutura oficial das linhas de ônibus, horários, rotas, pontos de parada.
- **Coleta**: Download por cidade; usar Python para leitura dos arquivos `routes.txt`, `trips.txt`, `stops.txt` e `stop_times.txt`.

## 4.4 INEP - Censo Escolar

- **Fonte**: [INEP](https://inep.gov.br)
- **Formato**: CSV / XLS
- **Frequência**: Anual
- **Uso no Projeto**: Possível cruzamento com dados de deslocamento escolar para identificar impacto do transporte em acesso à educação.
- **Coleta**: Manual, com extração seletiva de colunas relevantes.

## 4.5 Dados Abertos Gov.br

- **Fonte**: [Portal de Dados Abertos](https://dados.gov.br/)
- **Formato**: CSV / JSON / XLS
- **Frequência**: Variada
- **Uso no Projeto**: Complementar com dados de mobilidade urbana, políticas públicas e investimentos.
- **Coleta**: Manual e com uso de APIs quando disponível.

---

## 4.6 Considerações Técnicas

- Todos os arquivos serão armazenados inicialmente na pasta `/data/raw`.
- Após tratamento, os dados irão para `/data/processed`.
- Fontes que oferecem APIs serão integradas com scripts Python

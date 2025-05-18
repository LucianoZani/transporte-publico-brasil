# 7. Tratamento e Qualidade dos Dados

## 7.1 Fontes de Dados e Possíveis Problemas

| Fonte                      | Possíveis Problemas                                   |
|---------------------------|-------------------------------------------------------|
| GTFS (dados de transporte)| Dados faltantes, horários inconsistentes, nomes duplicados |
| Censos e estatísticas IBGE| Divergência de granularidade (UF, cidade, bairro), dados desatualizados |
| Dados escolares (INEP)    | Dados agregados demais ou com formatos diferentes por ano |
| Dados de mobilidade urbana| Formatos diferentes (CSV, JSON), geocódigos ausentes |

---

## 7.2 Estratégias de Tratamento

### Dados Tabulares
- Remoção de duplicados
- Conversão de colunas para tipos corretos
- Normalização de nomes (ex: bairros, cidades)
- Preenchimento de valores ausentes com:
  - Média ou mediana (quando aplicável)
  - Imputação geográfica (dados próximos)
  - "Desconhecido" para categorias

### Dados Geográficos
- Verificação de coordenadas fora do território nacional
- Correção de projeções geográficas
- Conversão para GeoJSON padronizado
- Simplificação de geometrias pesadas para visualização

---

## 7.3 Métricas de Qualidade a Serem Monitoradas

| Métrica                          | Objetivo |
|----------------------------------|----------|
| % de linhas sem coordenadas      | Avaliar qualidade do GTFS |
| % de escolas sem linhas próximas | Medir acesso escolar |
| % de registros incompletos       | Medir cobertura de preenchimento |
| % de nomes duplicados por UF     | Padronização de regiões e localidades |
| % de erros em formatos de data   | Validação temporal |

---

## 7.4 Ferramentas e Técnicas Usadas

- **Pandas Profiling**: para análise exploratória inicial
- **Great Expectations** *(opcional)*: para criação de testes de dados
- **GeoPandas + Shapely**: validação de geometria e sobreposição
- **Logs em JSON**: cada etapa do pipeline terá logs com timestamp, input/output e status
- **Validações manuais por amostragem**: auditoria de resultados

---

## 7.5 Documentação e Auditoria

- Todos os datasets terão um arquivo `README.md` explicando:
  - Origem dos dados
  - Estrutura esperada
  - Regras de limpeza aplicadas
- Cada transformação relevante será registrada em changelogs automáticos ou manuais

---

## 7.6 Governança Aplicada

Este projeto segue práticas de Governança de Dados como:

- **Linhas de Responsabilidade (Accountability)**: cada script/documento será atribuído a uma fase e autor
- **Lineage (Rastreabilidade)**: dados de entrada, transformação e saída serão documentados
- **Padrões e Consistência**: nomenclatura uniforme e reutilização de scripts

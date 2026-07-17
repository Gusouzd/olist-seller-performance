# Olist Seller Performance Pipeline

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)

Pipeline ETL que extrai dados de e-commerce do PostgreSQL, valida a qualidade dos dados, calcula métricas de performance por vendedor e entrega os resultados prontos para consulta no banco de dados e em CSV.

---

## O que o pipeline faz

```
PostgreSQL (dados brutos)
    ↓ Extrai
Python — lê as tabelas do banco
    ↓ Valida
Verifica qualidade e consistência dos dados
    ↓ Transforma
Calcula métricas por vendedor
    ↓ Carrega
PostgreSQL → tabela olist_sales_performance
CSV        → relatório para o gestor
```

**Métricas calculadas por vendedor:**

| Métrica | Descrição |
|---|---|
| `receita_total` | Soma de todos os pedidos do vendedor |
| `ticket_medio` | Valor médio por pedido |
| `avaliacao_media` | Média das avaliações dos clientes |
| `taxa_entrega_no_prazo` | % de pedidos entregues antes da data estimada |

---

## Validação de qualidade dos dados

Antes de transformar, o pipeline valida automaticamente:

| Validação | O que verifica |
|---|---|
| Preço inválido | Itens com preço menor ou igual a zero |
| Integridade referencial | Order IDs sem correspondência em orders |
| Avaliações fora do range | Review scores fora do intervalo de 1 a 5 |
| Datas impossíveis | Entregas registradas antes da data de compra |
| Nulos por coluna | Colunas com valores ausentes em orders e order_items |

Problemas encontrados são registrados como `WARNING` no log de execução.

---

## Por que isso importa

Monitorar a performance de vendedores é essencial em qualquer operação de e-commerce. Este pipeline automatiza esse processo — eliminando relatórios manuais e garantindo que a análise esteja sempre atualizada com os dados mais recentes.

---

## Tecnologias utilizadas

| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| pandas | Transformação e agregação dos dados |
| NumPy | Cálculo da métrica de entrega no prazo |
| SQLAlchemy | Conexão com o banco de dados |
| psycopg2 | Driver PostgreSQL |
| python-dotenv | Gerenciamento seguro de credenciais |
| PostgreSQL | Banco de dados fonte e destino |

---

## Estrutura do projeto

```
olist-seller-performance/
├── .env                        # credenciais (não vai pro GitHub)
├── .gitignore
├── pipeline.py                 # pipeline ETL principal
├── pipeline.log                # logs de execução (gerado automaticamente)
├── olist_sales_performance.csv # relatório exportado
└── README.md
```

---

## Como rodar

### Pré-requisitos

- Python 3.8+
- PostgreSQL com o dataset Olist importado
- Bibliotecas instaladas:

```bash
pip install pandas numpy sqlalchemy psycopg2-binary python-dotenv
```

### Configuração

Crie um arquivo `.env` na raiz do projeto com suas credenciais:

```
DB_USUARIO=seu_usuario
DB_SENHA=sua_senha
DB_BANCO=nome_do_banco
```

### Execução

```bash
python pipeline.py
```

### Saídas

| Saída | Descrição |
|---|---|
| Tabela `olist_sales_performance` | Resultado carregado no PostgreSQL |
| `olist_sales_performance.csv` | Relatório exportado para análise |
| `pipeline.log` | Log completo da execução com timestamps |

---

## Dataset

[Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — dataset público com dados reais de uma plataforma de e-commerce brasileira.

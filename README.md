# Olist Seller Performance Pipeline

Pipeline ETL que extrai dados de e-commerce do PostgreSQL, calcula métricas de performance por vendedor e entrega os resultados prontos para consulta no banco de dados e em CSV.

---

## O que o pipeline faz

1. **Extrai** as tabelas de pedidos, itens, avaliações e vendedores direto do banco de dados
2. **Transforma** os dados calculando quatro métricas por vendedor:
   - Receita total
   - Ticket médio
   - Avaliação média dos clientes
   - Taxa de entrega no prazo
3. **Carrega** o resultado em uma tabela no PostgreSQL e exporta um CSV pronto para análise

## Por que isso importa

Monitorar a performance de vendedores é essencial em qualquer operação de e-commerce. Este pipeline automatiza esse processo — eliminando relatórios manuais e garantindo que a análise esteja sempre atualizada com os dados mais recentes.

---

## Tecnologias utilizadas

- **Python** — linguagem principal
- **pandas** — transformação e agregação dos dados
- **NumPy** — cálculo da métrica de entrega no prazo
- **SQLAlchemy** — conexão com o banco de dados
- **psycopg2** — driver PostgreSQL
- **python-dotenv** — gerenciamento seguro de credenciais
- **PostgreSQL** — banco de dados fonte e destino

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

---

## Dataset

[Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — dataset público disponível no Kaggle com dados reais de uma plataforma de e-commerce brasileira.

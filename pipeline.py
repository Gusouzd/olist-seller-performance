import pandas as pd
import numpy as np
import logging
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline.log'), 
        logging.StreamHandler()
    ]
)

def criar_conexao():
    load_dotenv()
    url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.environ['DB_USUARIO'],
        password=os.environ['DB_SENHA'],
        host="localhost",
        port=5432,
        database=os.environ['DB_BANCO']
    )
    return create_engine(url)

def extrair(engine):
    logging.info("Extraindo tabelas...")
    order_items = pd.read_sql("SELECT * FROM order_items", con=engine)
    order_reviews = pd.read_sql("SELECT * FROM order_reviews", con=engine)
    orders = pd.read_sql("SELECT * FROM orders", con=engine)
    sellers = pd.read_sql("SELECT * FROM sellers", con=engine)
    logging.info("Tabelas extraídas com sucesso.")
    return order_items, orders, sellers, order_reviews

def transformar(order_items, orders, sellers, order_reviews):
    logging.info("Realizando as trativas com as tabelas ...")
    df = order_items.merge(orders, on='order_id')
    df = df.merge(sellers, on='seller_id')

    colunas_datas = ['shipping_limit_date', 'order_purchase_timestamp', 'order_approved_at',
                     'order_delivered_carrier_date', 'order_delivered_customer_date',
                     'order_estimated_delivery_date']
    df[colunas_datas] = df[colunas_datas].apply(pd.to_datetime, errors='coerce')

    df["entrega_no_prazo"] = np.where(
        df["order_delivered_customer_date"].isna(), None,
        np.where(df["order_estimated_delivery_date"] >= df["order_delivered_customer_date"], 1, 0)
    )

    df = df.merge(order_reviews, on='order_id')
    df = df.groupby('seller_id').agg(
        receita_total=('price', 'sum'),
        ticket_medio=('price', 'mean'),
        avaliacao_media=('review_score', 'mean'),
        taxa_entrega_no_prazo=('entrega_no_prazo', 'mean')
    )
    logging.info("Trativas realizadas com sucesso.")
    return df

def carregar(df, engine):
    logging.info("Exportando as tabelas...")
    df.to_sql(
        name='olist_sales_performance',
        con=engine,
        if_exists='replace',
        index=True
    )
    df.to_csv('olist_sales_performance.csv')
    logging.info("Tabelas exportadas com sucesso.")

# Execução
engine = criar_conexao()
order_items, orders, sellers, order_reviews = extrair(engine)
df = transformar(order_items, orders, sellers, order_reviews)
carregar(df, engine)
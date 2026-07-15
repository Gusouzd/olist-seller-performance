# Importações

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.environ['DB_USUARIO'],
    password=os.environ['DB_SENHA'],
    host="localhost",
    port=5432,
    database=os.environ['DB_BANCO']
)

engine = create_engine(url)

# Trazendo as tabelas para o python como dataframe

customers = pd.read_sql("SELECT * FROM customers",con=engine)
geolocation = pd.read_sql("SELECT * FROM geolocation LIMIT 1000",con=engine)
order_items = pd.read_sql("SELECT * FROM order_items",con=engine)
order_payments = pd.read_sql("SELECT * FROM order_payments",con=engine)
order_reviews = pd.read_sql("SELECT * FROM order_reviews",con=engine)
orders = pd.read_sql("SELECT * FROM orders",con=engine)
product_category_name_translation = pd.read_sql("SELECT * FROM product_category_name_translation",con=engine)
products = pd.read_sql("SELECT * FROM products",con=engine)
sellers = pd.read_sql("SELECT * FROM sellers",con=engine)
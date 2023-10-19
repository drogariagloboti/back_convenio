import psycopg2
import pymssql

def connect_loja(ip): # connect_loja(ip):
    con = psycopg2.connect(
    host=f'{ip}', # host=f'{ip}'
    database='pdv', # alterado para o pdv1 para usar a base de teste, padrão é pdv
    user='postgres', # alterado para usar a base de teste, padrão é postgres
    password='postgres' # 2021#Pgl0B0&9810 alterado para usar a base de teste, padrão é postgres
    )

    return con

def sqlServer():
    
    conn = pymssql.connect(server='10.10.0.5', user='gestao', password='jbglobo', database='GloboProducao')  

    return conn

def connect_pg(): # connect_loja(ip):
    con = psycopg2.connect(
    host='10.10.0.52', # host=f'{ip}'
    database='conv_model', # alterado para o pdv1 para usar a base de teste, padrão é pdv
    user='postgres', # alterado para usar a base de teste, padrão é postgres
    password='Gl0b0@2021#pgSQL' # 2021#Pgl0B0&9810 alterado para usar a base de teste, padrão é postgres
    )

    return con

def connect_teste(): # connect_loja(ip):
    con = psycopg2.connect(
    host=f'10.10.254.108', # host=f'{ip}'
    database='pdv', # alterado para o pdv1 para usar a base de teste, padrão é pdv
    user='postgres', # alterado para usar a base de teste, padrão é postgres
    password='2021#Pgl0B0&9810' # 2021#Pgl0B0&9810 alterado para usar a base de teste, padrão é postgres
    )

    return con

def connect_heroku(): # connect_loja(ip):
    con = psycopg2.connect(
    host='ec2-54-80-122-11.compute-1.amazonaws.com', 
    database='dekv4drpjp1cad', 
    user='yrnaovbgfzldkl', 
    password='a830eb6dc2335d4764627e8c4728e6848e1bfa1b905379a458b1d725497ee8a4', 
    sslmode='require')

    return con
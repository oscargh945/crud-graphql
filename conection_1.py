import psycopg2

try:
    connection = psycopg2.connect("dbname=postgres user=debug1 password=debug1 port=5432 host=0.0.0.0")
except Exception as error:
    print("error al conectarse a la db", error)


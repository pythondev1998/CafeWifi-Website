import psycopg2

# Datos de conexión
hostname = "dpg-cj0m9tc07spl5oqcr3e0-a.oregon-postgres.render.com"
port = "5432"
database = "dbnamecafe"
username = "dbnamecafe_user"
password = "AmMwLwTkclMVGOJ25T5RSYaTqGzUy9jY"

# Intenta conectarte a la base de datos
try:
    conn = psycopg2.connect(
        host=hostname,
        port=port,
        dbname=database,
        user=username,
        password=password
    )
    print("Conexión exitosa a la base de datos PostgreSQL.")
    conn.close()
except Exception as e:
    print("Error al conectarse a la base de datos PostgreSQL:", e)

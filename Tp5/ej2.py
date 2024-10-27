import psycopg2
from psycopg2 import pool

class DatabaseConnectionSingleton:
    _instance = None
    _connection_pool = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnectionSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, dbname, user, password, host, port):
        if not self._connection_pool:
            try:
                self._connection_pool = psycopg2.pool.SimpleConnectionPool(
                    minconn=1,
                    maxconn=10,
                    dbname=dbname,
                    user=user,
                    password=password,
                    host=host,
                    port=port
                )
                print("Connection pool created successfully")
            except Exception as e:
                print(f"Error creating connection pool: {e}")

    def get_connection(self):
        if self._connection_pool:
            return self._connection_pool.getconn()
        else:
            raise Exception("Connection pool is not initialized")

    def put_connection(self, connection):
        if self._connection_pool:
            self._connection_pool.putconn(connection)

    def close_all_connections(self):
        if self._connection_pool:
            self._connection_pool.closeall()

# Uso
db_singleton = DatabaseConnectionSingleton(
    dbname="your_database",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)

connection = db_singleton.get_connection()
# Realizar operaciones con la conexión

# Liberar la conexión de vuelta al pool
db_singleton.put_connection(connection)

# Cerrar todas las conexiones cuando se termine el uso
db_singleton.close_all_connections()


""""Explicación del Código
Singleton con __new__: La clase verifica si ya existe una instancia; si no, la crea y la almacena en _instance. De esta manera, solo se creará una instancia de DatabaseConnectionSingleton.

Pool de Conexiones: Utilizamos un pool de conexiones con psycopg2.pool.SimpleConnectionPool para gestionar las conexiones de manera eficiente y reutilizable. Esto ayuda a mantener bajo el número de conexiones activas al servidor de base de datos.

Métodos get_connection y put_connection: Estos métodos manejan el préstamo y retorno de conexiones del pool.

Cierre de Conexiones: Cuando el programa ya no necesite acceder a la base de datos, se puede usar close_all_connections para cerrar todas las conexiones activas.

Ventajas del Patrón Singleton en Conexiones de Base de Datos
Eficiencia: Evita crear múltiples conexiones innecesarias.
Reutilización: Permite reutilizar la misma conexión, ahorrando recursos.
Fácil mantenimiento: Centraliza el acceso y manejo de la base de datos en una sola clase.
Este patrón también se puede aplicar a MySQL, reemplazando psycopg2 con un cliente compatible como mysql-connector-python o PyMySQL, con ajustes menores en el código."""
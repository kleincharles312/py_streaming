import oracledb

# TODO: more configs
username = 'SYS'
host = 'localhost'
port = 1521
service_name = 'FREE'
password = 'super_str0ng!'
mode = oracledb.SYSDBA

class OracleDBConnection:
    def __init__(self, username, password, service_name):
        self.username = username
        self.password = password
        self.service_name = service_name
        self.connection = None

    def connect(self):
        try:
            self.connection = oracledb.connect(user=self.username, password=self.password, dsn=f"{host}:{port}/{self.service_name}", mode=mode)
            print("Connected to Oracle Database")
        except oracledb.DatabaseError as e:
            print(f"Error connecting to Oracle Database: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

    def write_keystroke_message(self, source, username, keystroke):
        if not self.connection:
            print("Not connected to the database")
            return

        cursor = self.connection.cursor()
        try:
            sql = f"INSERT INTO messages (source, username, keystroke) VALUES ('{source}', '{username}', '{keystroke}');"
            print(sql)
            cursor.execute(sql)
            self.connection.commit()
            print("Keystroke message written to database")
        except oracledb.DatabaseError as e:
            print(f"Error writing keystroke message to database: {e}")
        finally:
            cursor.close()

def get_oracle_db_connection():
    return OracleDBConnection(username=username, password=password, service_name=service_name)
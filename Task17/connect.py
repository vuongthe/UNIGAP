import mysql.connector
from config import load_config

def connect(config):
    try:
        with mysql.connector.connect(**config) as conn :
            print('Connected to the MySql')
            return conn
    except (mysql.connector.Error) as error:
        print(error)    

if __name__ == '__main__':
    config = load_config()
    connect(config)

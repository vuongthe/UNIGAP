import mysql.connector
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE vendors (
        vendor_id INT AUTO_INCREMENT PRIMARY KEY,
        vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (s
                part_id INT AUTO_INCREMENT PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
            part_id INT PRIMARY KEY,
            file_extension VARCHAR(5) NOT NULL,
            drawing_data BLOB NOT NULL,
            FOREIGN KEY (part_id)
            REFERENCES parts (part_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
            vendor_id INT NOT NULL,
            part_id INT NOT NULL,
            PRIMARY KEY (vendor_id, part_id),
            FOREIGN KEY (vendor_id)
            REFERENCES vendors (vendor_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (part_id)
            REFERENCES parts (part_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    try:
        config = load_config()
        with mysql.connector.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except mysql.connector.Error as error:
        print(error)

if __name__ == '__main__':
    create_tables()
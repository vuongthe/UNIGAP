import mysql.connector
from config import load_config

def insert_vendor(vendor_name):
    """ Insert a new vendor into the vendors table """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    vendor_id = None
    config = load_config()
    try:
        conn = mysql.connector.connect(**config)
        cur = conn.cursor()
        # Execute the INSERT statement
        cur.execute(sql, (vendor_name,))
        # Get the generated id back
        vendor_id = cur.lastrowid
        # Commit the changes to the database
        conn.commit()
    except (mysql.connector.Error, Exception) as error:
        print("Error:", error)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        return vendor_id

def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    config = load_config()
    try:
        conn = mysql.connector.connect(**config)
        cur = conn.cursor()
        # Execute the INSERT statement
        cur.executemany(sql, vendor_list)
        # Commit the changes to the database
        conn.commit()
    except (mysql.connector.Error, Exception) as error:
        print("Error:", error)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    print("Inserted vendor ID:", insert_vendor("3M Co."))

    insert_many_vendors([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])

import mysql.connector
from config import load_config

def write_blob(part_id, path_to_file, file_extension):
    """ Insert a BLOB into a table """
    # read database configuration
    params = load_config()

    # read data from a picture
    data = open(path_to_file, 'rb').read()

    try:
        # connect to the MySQL database
        with mysql.connector.connect(**params) as conn:
            # create a new cursor object
            with conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(
                    "INSERT INTO part_drawings(part_id, file_extension, drawing_data) VALUES (%s, %s, %s)",
                    (part_id, file_extension, data)  # Gửi trực tiếp dữ liệu BLOB vào đây
                )
            conn.commit()

    except (Exception, mysql.connector.Error) as error:
        print(error)

if __name__ == '__main__':
    write_blob(1, 'images/input/simtray.png', 'png')
    write_blob(2, 'images/input/speaker.png', 'png')

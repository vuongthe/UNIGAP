import mysql.connector
from config import load_config
import os

def read_blob(part_id, path_to_dir):
    """ Read BLOB data from a table and save it to a file """
    # read database configuration
    config = load_config()

    try:
        # connect to the MySQL database
        with mysql.connector.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the SELECT statement
                cur.execute("""
                    SELECT part_name, file_extension, drawing_data
                    FROM part_drawings
                    INNER JOIN parts ON parts.part_id = part_drawings.part_id
                    WHERE parts.part_id = %s
                """, (part_id,))

                # fetch one result
                blob = cur.fetchone()

                if blob:  # Check if blob is not None
                    # ensure the output directory exists
                    if not os.path.exists(path_to_dir):
                        os.makedirs(path_to_dir)

                    # write the BLOB data to a file
                    with open(os.path.join(path_to_dir, f"{blob[0]}.{blob[1]}"), 'wb') as file:
                        file.write(blob[2])
                    print(f"File saved as {blob[0]}.{blob[1]}")
                else:
                    print(f"No data found for part_id {part_id}")

    except (Exception, mysql.connector.Error) as error:
        print("Error:", error)

if __name__ == '__main__':
    read_blob(1, 'images/output/')
    read_blob(2, 'images/output/')

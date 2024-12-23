import mysql.connector
from config import load_config


def add_part(part_name, vendor_list):
    # Câu lệnh thêm vào bảng parts
    insert_part = "INSERT INTO parts(part_name) VALUES(%s);"

    # Câu lệnh thêm vào bảng vendor_parts
    assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s);"

    conn = None
    config = load_config()

    try:
        with mysql.connector.connect(**config) as conn:
            with conn.cursor() as cur:
                # Thêm một part mới
                cur.execute(insert_part, (part_name,))
                
                # Lấy part_id
                part_id = cur.lastrowid
                if not part_id:
                    raise Exception(f"Could not get the part ID. Lastrowid returned: {part_id}")
                print(f"Inserted part '{part_name}' with ID: {part_id}")

                # Ánh xạ với vendor
                for vendor_id in vendor_list:
                    cur.execute(assign_vendor, (vendor_id, part_id))
                    print(f"Assigned part ID {part_id} to vendor ID {vendor_id}")

                # Commit giao dịch
                conn.commit()

    except (Exception, mysql.connector.Error) as error:
        if conn and conn.is_connected():
            conn.rollback()
        print("Error:", error)


if __name__ == '__main__':
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Vibrator', (5, 6))
    add_part('Antenna', (6, 7))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))

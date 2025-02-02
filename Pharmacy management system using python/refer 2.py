import sqlite3

def delete_all_data(database_name):
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            cursor.execute(f"DELETE FROM {table_name}")

        conn.commit()
        print("All data in the tables has been deleted.")
    except sqlite3.Error as e:
        print(f"Error deleting data: {e}")
    finally:
        conn.close()

# Specify the name of your database file
database_name = 'pharmacy.db'

delete_all_data(database_name)

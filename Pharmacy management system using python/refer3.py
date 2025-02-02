import sqlite3

def display_table_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_record(table_name, ref_no, field, value):
    try:
        cursor.execute(f"UPDATE {table_name} SET {field} = ? WHERE REF_NO = ?", (value, ref_no))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Record with REF_NO {ref_no} updated successfully.")
        else:
            print(f"No records found with REF_NO {ref_no}.")
    except sqlite3.Error as e:
        print(f"Error updating record: {e}")

# Connect to the SQLite database
conn = sqlite3.connect('pharmacy.db')
cursor = conn.cursor()

# List all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"Table: {table_name}")
    display_table_data(table_name)

    user_choice = input("Enter the REF_NO to update the record: ")
    field = input("Enter the field name to update: ")
    value = input("Enter the new value: ")

    update_record(table_name, user_choice, field, value)

    print("\n")

# Close the database connection
conn.close()

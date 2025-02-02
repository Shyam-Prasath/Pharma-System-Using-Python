import sqlite3

def update_medicine_info(conn, cursor, ref_no, new_ref_no, new_med_name):
    try:
        # Update the record in the Information table
        cursor.execute("UPDATE Information SET REF_NO = ?, MED_NAME = ? WHERE REF_NO = ?", (new_ref_no, new_med_name, ref_no))
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

# Get user input for REF_NO and new values
ref_no = input("Enter the REF_NO to update the record: ")
new_ref_no = input("Enter the new REF_NO: ")
new_med_name = input("Enter the new MED_NAME: ")

# Update the record
update_medicine_info(conn, cursor, ref_no, new_ref_no, new_med_name)

# Close the database connection
conn.close()

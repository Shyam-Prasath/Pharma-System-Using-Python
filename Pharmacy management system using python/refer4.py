import sqlite3

def update_record(ref_no, new_ref_no, new_med_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()

        # Update the record in the pharma table
        cursor.execute("UPDATE pharma SET REF_NO = ?, MED_NAME = ? WHERE REF_NO = ?", (new_ref_no, new_med_name, ref_no))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Record with REF_NO {ref_no} updated successfully.")
        else:
            print(f"No information found with REF_NO {ref_no}.")

    except sqlite3.Error as e:
        print(f"Error updating record: {e}")

    finally:
        # Close the database connection
        conn.close()

# Example usage
if __name__ == "__main__":
    ref_no = input("Enter the REF_NO to update the record: ")
    new_ref_no = input("Enter the new REF_NO: ")
    new_med_name = input("Enter the new medicine name: ")

    update_record(ref_no, new_ref_no, new_med_name)

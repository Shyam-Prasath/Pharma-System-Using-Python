import sqlite3

def add():
    con = sqlite3.connect(database='pharmacy.db')  # Use a relative path if the database is in the same directory
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Information(REF_NO text PRIMARY KEY,COMPANY_NAME text,TYPE_OF_MED text,MED_NAME text,LOT_NO text,ISSUE_DT text,EXP_DT text,USES text,SIDE_EFFECT text,PRECAUTION text,DOSAGE text,PRICE text,QUANTITY text)")
    con.commit()


add()
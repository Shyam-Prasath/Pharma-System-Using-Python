from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import ttk, messagebox
import sqlite3


class Pharmacy:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1280x770+0+0")
        self.root.resizable(False, False)
        self.root.iconbitmap("image/doc.ico")
        self.conn = sqlite3.connect("medicine.db")
        ##### ADDMED VARIABLE ######
        self.ref_variable = StringVar()
        self.addmed_variable = StringVar()

        ########## MEDICINE DEPARTMENT VARIABLE #######
        self.refno_var = StringVar()
        self.companyname_var = StringVar()
        self.typemed_var = StringVar()
        self.medicine_var = StringVar()
        self.lotno_var = StringVar()
        self.issuedt_var = StringVar()
        self.expdt_var = StringVar()
        self.uses_var = StringVar()
        self.sideeffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        ######## title animation #########
        self.txt = "PHARMACY MANAGEMENT SYSTEM"
        self.count = 0
        self.text = ""
        self.color = ["green"]
        self.heading = Label(self.root, text=self.txt, font=(
            "times new roman", 30, "bold"), bg='grey', fg="blue", bd=9, relief=RIDGE)
        self.heading.pack(side=TOP, fill=X)
        self.slider()
        self.heading_color()

        # lbltitle=Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=11,relief=RIDGE
                            # ,bg='#7FFFD4',fg='#0020C2',font=('times new roman',35,'bold'),padx=2,pady=4)
        # lbltitle.pack(side=TOP,fill=X)

        ######### pharmacy logo label #######
        img1 = Image.open("image/new.png")  # Assuming 'new.png' is in the "image" folder relative to your script
        img1 = img1.resize((70, 45))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1,
                    borderwidth=0, bg='grey')
        b1.place(x=15, y=8)

        ###### Top Frame #####
        topframe = Frame(self.root, bg='grey', bd=10, relief=RIDGE, padx=20)
        topframe.place(x=0, y=62, width=1350, height=400)

        ########  down button frame #######
        down_buttonframe = Frame(
            self.root, bg='grey', bd=10, relief=RIDGE, padx=20)
        down_buttonframe.place(x=0, y=462, width=1350, height=60)

            ###### all buttons ######
        add_button = Button(down_buttonframe, text="Add Medicine", command=self.addmedicine, font=(
            "arial", 12, "bold"), width=14, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        add_button.grid(row=0, column=0)

        update_button = Button(down_buttonframe, command=self.update_new, text="Update", font=(
            "arial", 13, "bold"), width=14, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        update_button.grid(row=0, column=1)

        delete_button = Button(down_buttonframe, text="Delete", font=("arial", 13, "bold"), width=13,
                               fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white",command=self.Delete_new)
        delete_button.grid(row=0, column=2)

        reset_button = Button(down_buttonframe, text="Reset", command=self.clear_new, font=("arial", 13, "bold"), width=12,
                              fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        reset_button.grid(row=0, column=3)

        exit_button = Button(down_buttonframe, command=self.root.quit, text="Exit", font=(
            "arial", 13, "bold"), width=10, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        exit_button.grid(row=0, column=4)

        search_by = Label(down_buttonframe, text="Search By", font=(
            "arial", 15, "bold"), fg="black", bg="grey", bd=3, padx=3)
        search_by.grid(row=0, column=5, sticky=W)

        self.search_combo = ttk.Combobox(down_buttonframe, width=12, font=(
            "arial", 13, "bold"), state="readonly", textvariable=self.search_by)
        self.search_combo["values"] = ("Select Options", "Ref No.")
        self.search_combo.grid(row=0, column=6)
        self.search_combo.current(0)

        entry_button = Entry(down_buttonframe, font=("arial", 15, "bold"), fg="black",
                             bg="grey", bd=3, width=12, relief=RIDGE, textvariable=self.search_txt)
        entry_button.grid(row=0, column=7)

        search_button = Button(down_buttonframe, text="Search", font=("arial", 13, "bold"), width=10, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.search_data)
        search_button.grid(row=0, column=8)

        show_button = Button(down_buttonframe, text="Show All", font=("arial", 13, "bold"), fg="white", bg="black",
                             width=10, bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.fetch_new)
        show_button.grid(row=0, column=9)

        ######## left small frame #######
        left_smallframe = LabelFrame(topframe, bg='grey', bd=10, relief=RIDGE,
                                     padx=20, text="Medicine Information", font=("arial", 13, "bold"), fg="white")
        left_smallframe.place(x=0, y=5, width=820, height=350)

           #### labeling & entry box #########

        # 1

        ref_label = Label(left_smallframe, text="Reference No. :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        ref_label.grid(row=0, column=0, sticky=W)

        conn = sqlite3.connect(database='pharmacy.db')
        my_cursor = conn.cursor()
        my_cursor.execute("Select Ref_no from pharma")
        row_01 = my_cursor.fetchall()

        self.ref_combo = ttk.Combobox(left_smallframe, textvariable=self.refno_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.ref_combo["values"] = ('Select',row_01)
        self.ref_combo.grid(row=0, column=1)
        self.ref_combo.current(0)

        # 2

        company_label = Label(left_smallframe, text="Company Name  :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        company_label.grid(row=1, column=0)

        self.company_entry = Entry(left_smallframe, textvariable=self.companyname_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.company_entry.grid(row=1, column=1)

        # 3
        type_label = Label(left_smallframe, text="Type Of Medicine :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        type_label.grid(row=2, column=0, sticky=W)

        self.type_combo = ttk.Combobox(left_smallframe, textvariable=self.typemed_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.type_combo["values"] = (
            " Select  ", "Tablet", "Capsule", "Injection", "Ayurvedic", "Drops", "Inhales")
        self.type_combo.grid(row=2, column=1)
        self.type_combo.current(0)

        # 4

        medname_label = Label(left_smallframe, text="Medicine Name :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        medname_label.grid(row=3, column=0, sticky=W)

        conn = sqlite3.connect(database='pharmacy.db')  # Use a relative path if the database is in the same directory
        my_cursor = conn.cursor()
        my_cursor.execute("Select Med_name from pharma")
        row_02 = my_cursor.fetchall()

        self.medname_combo = ttk.Combobox(left_smallframe, textvariable=self.medicine_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.medname_combo["values"] = ('Select',row_02)
        self.medname_combo.grid(row=3, column=1)
        self.medname_combo.current(0)

        # 5

        lot_label = Label(left_smallframe, text=" Lot No. :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        lot_label.grid(row=4, column=0)

        self.lot_entry = Entry(left_smallframe, textvariable=self.lotno_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.lot_entry.grid(row=4, column=1)

        # 6

        issue_label = Label(left_smallframe, text=" Issue Date :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        issue_label.grid(row=5, column=0)

        self.issue_entry = Entry(left_smallframe, textvariable=self.issuedt_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.issue_entry.grid(row=5, column=1)

        # 7

        exp_label = Label(left_smallframe, text=" Expiry Date :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        exp_label.grid(row=6, column=0)

        self.exp_entry = Entry(left_smallframe, textvariable=self.expdt_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.exp_entry.grid(row=6, column=1)

        # 8

        use_label = Label(left_smallframe, text=" Uses :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        use_label.grid(row=7, column=0)

        self.use_entry = Entry(left_smallframe, textvariable=self.uses_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.use_entry.grid(row=7, column=1)

        # 9

        sideeffect_label = Label(left_smallframe, text=" Side Effect :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        sideeffect_label.grid(row=8, column=0)

        self.sideeffect_entry = Entry(left_smallframe, textvariable=self.sideeffect_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.sideeffect_entry.grid(row=8, column=1)

        # 10

        warn_label = Label(left_smallframe, text=" Prec & warning:", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        warn_label.grid(row=9, column=0)

        self.warn_entry = Entry(left_smallframe, textvariable=self.warning_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.warn_entry.grid(row=9, column=1)

        # 11

        dosage_label = Label(left_smallframe, text=" Dosage :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        dosage_label.grid(row=0, column=2)

        self.dosage_entry = Entry(left_smallframe, textvariable=self.dosage_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.dosage_entry.grid(row=0, column=3)

        # 12

        price_label = Label(left_smallframe, text=" Tablet Price :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        price_label.grid(row=1, column=2)

        self.price_entry = Entry(left_smallframe, textvariable=self.price_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.price_entry.grid(row=1, column=3)

        # 13

        qt_label = Label(left_smallframe, text=" Tablet Quantity :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        qt_label.grid(row=2, column=2)

        self.qt_entry = Entry(left_smallframe, textvariable=self.quantity_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.qt_entry.grid(row=2, column=3)

            ######## image in left small frame #####
        # image 1
        self.bg = ImageTk.PhotoImage(file='image/med.jpg')
        lbl_bg = Label(left_smallframe, image=self.bg)
        lbl_bg.place(x=370, y=165, width=200, height=150)
        # image 2
        self.bgg = ImageTk.PhotoImage(file='image/medi.jpg')
        lbl_bgg = Label(left_smallframe, image=self.bgg)
        lbl_bgg.place(x=570, y=165, width=200, height=150)

        # save life label
        save_bgg = Label(left_smallframe, text="----------- Stay Home Stay Safe -----------",
                         font=("arial", 13, "bold"), bg='grey', fg="white")
        save_bgg.place(x=370, y=120, width=400)

        ############ right frame #########
        right_frame = LabelFrame(topframe, bg='grey', bd=10, relief=RIDGE, padx=5,
                                 text="New Medicine Add department", font=("arial", 13, "bold"), fg="white")
        right_frame.place(x=846, y=5, width=452, height=350)

          # image & label

        # image 1
        self.bg1 = ImageTk.PhotoImage(file='image/co.jpg')
        lbl_bg1 = Label(right_frame, image=self.bg1)
        lbl_bg1.place(x=0, y=0, width=240, height=100)
        # image 2
        self.bg2 = ImageTk.PhotoImage(file='image/inject.jpg')
        lbl_bg2 = Label(right_frame, image=self.bg2)
        lbl_bg2.place(x=242, y=0, width=180, height=150)

        #### label & entry in right frame ####
        # 1
        no_label = Label(right_frame, text="Reference No:", font=(
            "times new roman", 11, "bold"), bg="grey")
        no_label.place(x=0, y=105)

        self.no_entry = Entry(right_frame, textvariable=self.ref_variable, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.no_entry.place(x=100, y=105)
        # 2
        med_label = Label(right_frame, text="Med. Name:", font=(
            "times new roman", 11, "bold"), bg="grey")
        med_label.place(x=0, y=130)

        self.med_entry = Entry(right_frame, textvariable=self.addmed_variable, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.med_entry.place(x=100, y=130)

        #### in right frame small frame #####

        newframe = Frame(right_frame, bg='darkgreen', bd=5, relief=RIDGE)
        newframe.place(x=256, y=160, width=150, height=150)

          ###### button in this frame ###
        add_button = Button(newframe, text="Add", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                            bd=3, command=self.AddMed, relief=RIDGE, activebackground="black", activeforeground="white")
        add_button.grid(row=0, column=0)

        updatenew_button = Button(newframe, text="Update", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                                  bd=3, command=self.Update_med, relief=RIDGE, activebackground="black", activeforeground="white")
        updatenew_button.grid(row=1, column=0)

        delnew_button = Button(newframe, text="Delete", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.Delete_med)
        delnew_button.grid(row=2, column=0)

        clr_button = Button(newframe, text="Clear", command=self.clear_med, font=("arial", 13, "bold"), width=13,
                            fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        clr_button.grid(row=3, column=0)

        ##### scrollbar frame in right frame ####
        side_frame = Frame(right_frame, bd=4, relief=RIDGE, bg="dark green")
        side_frame.place(x=0, y=160, width=250, height=150)

        ### scrollbar code ###

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        self.medicine_table = ttk.Treeview(side_frame, column=(
            "ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.pack(side=RIGHT, fill=Y)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.medget_cursor)
        self.fetch_datamed()

        ######### down frame #######
        down_frame = Frame(self.root, bg='grey', bd=10, relief=RIDGE)
        down_frame.place(x=0, y=522, width=1350, height=212)

        ########## scrollbar in down frame ########
        scroll_frame = Frame(down_frame, bd=2, relief=RIDGE, bg="white")
        scroll_frame.place(x=0, y=0, width=1330, height=192)

        ##### scrollbar code #####
        scroll_x = ttk.Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(scroll_frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(scroll_frame, column=("ref no", "comp name", "type", "medi name", "lot no", "issue", "exp",
                                       "uses", "side effect", "warning", "dosage", "price", "product"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.info_table.xview)
        scroll_y.config(command=self.info_table.yview)

        self.info_table.heading("ref no", text="Ref No.")
        self.info_table.heading("comp name", text="Company Name")
        self.info_table.heading("type", text="Type Of Medicine")
        self.info_table.heading("medi name", text="Medicine Name")
        self.info_table.heading("lot no", text="Lot No.")
        self.info_table.heading("issue", text="Issue Date")
        self.info_table.heading("exp", text="Expiry Date")
        self.info_table.heading("uses", text="Uses")
        self.info_table.heading("side effect", text="Side Effects")
        self.info_table.heading("warning", text="Prec & Warning")
        self.info_table.heading("dosage", text="Dosage")
        self.info_table.heading("price", text="Medicine Price")
        self.info_table.heading("product", text="Product Qt.")

        self.info_table["show"] = "headings"
        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("ref no", width=100)
        self.info_table.column("comp name", width=100)
        self.info_table.column("type", width=100)
        self.info_table.column("medi name", width=100)
        self.info_table.column("lot no", width=100)
        self.info_table.column("issue", width=100)
        self.info_table.column("exp", width=100)
        self.info_table.column("uses", width=100)
        self.info_table.column("side effect", width=100)
        self.info_table.column("warning", width=100)
        self.info_table.column("dosage", width=100)
        self.info_table.column("price", width=100)
        self.info_table.column("product", width=100)

        self.info_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_new()

    ####### MEDICINE ADD FUNCTIONALITY  DECLARATION #######

    def AddMed(self):

        if self.ref_variable.get() == "" or self.addmed_variable.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            conn = sqlite3.connect(database='pharmacy.db')
            my_cursor = conn.cursor()
            my_cursor.execute("Insert into pharma(Ref_no,Med_name) values(?,?)", (
                self.ref_variable.get(),
                self.addmed_variable.get(),))

            conn.commit()
            self.fetch_datamed()
            conn.close()

            messagebox.showinfo("Success", "MEDICINE ADDED")
    def Delete_new(self):  # Add self parameter
        def display_table_data(table_name):
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        def delete_record(table_name, ref_no):
            try:
                cursor.execute(f"DELETE FROM {table_name} WHERE REF_NO = ?", (ref_no,))
                conn.commit()
                if cursor.rowcount > 0:
                    print(f"Record with REF_NO {ref_no} deleted successfully.")
                else:
                    print(f"No records found with REF_NO {ref_no}.")
            except sqlite3.Error as e:
                print(f"Error deleting record: {e}")

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

            user_choice = input("Enter the REF_NO to delete the record: ")
            
            # Assuming REF_NO is the key column for all tables
            delete_record(table_name, user_choice)

            print("\n")

        # Close the database connection
        conn.close()

    def fetch_datamed(self):
        conn = sqlite3.connect(database='pharmacy.db')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("", END, values=i)

        conn.commit()
        conn.close()

    ###### for show data on click #####

    def medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content.get("values", [])  # Use get method with a default empty list
        if len(row) >= 2:  # Ensure row has at least two elements
            self.ref_variable.set(row[0])
            self.addmed_variable.set(row[1])
        else:
            messagebox.showerror("Error", "No data selected or incomplete data.")


    def Update_med(self):
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
                    messagebox.showinfo("Updated sucessfully")
                else:
                    print(f"No information found with REF_NO {ref_no}.")

            except sqlite3.Error as e:
                print(f"Error updating record: {e}")
                messagebox.showerror(f"Error on{e}")

            finally:
                # Close the database connection
                conn.close()

        # Example usage
        if __name__ == "__main__":
            ref_no = input("Enter the REF_NO to update the record: ")
            new_ref_no = input("Enter the new REF_NO: ")
            new_med_name = input("Enter the new medicine name: ")

            update_record(ref_no, new_ref_no, new_med_name)


    def Delete_med(self):
        if self.ref_variable.get()=="":
            messagebox.showerror("Error","Ref no is required",parent=self.root)
        else:

            try:
                conn = sqlite3.connect(database='pharmacy.db')
                my_cursor=conn.cursor()
            
                my_cursor.execute("Delete from pharma where Ref_no=? ",(self.ref_variable.get(),))
                conn.commit()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
                self.fetch_datamed()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)
       

    def clear_med(self):
        self.ref_variable.set("")
        self.addmed_variable.set("")
               
    
    ######## MEDICINE DEPARTMENT FUNCTIONALITY #######
    def addmedicine(self):
        if self.refno_var.get() == "" or self.lotno_var.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = sqlite3.connect(database='pharmacy.db')
            new_cursor=conn.cursor()
            new_cursor.execute("Insert into Information(REF_NO,COMPANY_NAME,TYPE_OF_MED,MED_NAME,LOT_NO,ISSUE_DT,EXP_DT,USES,SIDE_EFFECT,PRECAUTION,DOSAGE,PRICE,QUANTITY) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                self.refno_var.get(),
                self.companyname_var.get(),
                self.typemed_var.get(),
                self.medicine_var.get(),
                self.lotno_var.get(),
                self.issuedt_var.get(),
                self.expdt_var.get(),
                self.uses_var.get(),
                self.sideeffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.quantity_var.get(),
            ))
            conn.commit()
            conn.close()

            # Fetch and update the medicine information
            self.fetch_new()
            messagebox.showinfo("Success","Successfully added")

    def fetch_new(self):
        conn = sqlite3.connect(database='pharmacy.db')
        new_cursor = conn.cursor()
        new_cursor.execute("SELECT * FROM Information")
        rows = new_cursor.fetchall()

        if len(rows) != 0:
            self.info_table.delete(*self.info_table.get_children())
            for row in rows:
                self.info_table.insert("", END, values=row)

        conn.commit()
        conn.close()
    
    def get_cursor(self, event=""):
        cursor_row = self.info_table.focus()
        content = self.info_table.item(cursor_row)
        row = content["values"]
        if row:  # Check if row is not empty
            if len(row) > 0:  # Check if row has elements
                self.refno_var.set(row[0])  # Set REF_NO
                self.companyname_var.set(row[1])  # Set COMPANY_NAME
                self.typemed_var.set(row[2])  # Set TYPE_OF_MED
                self.medicine_var.set(row[3])  # Set MED_NAME
                self.lotno_var.set(row[4])  # Set LOT_NO
                self.issuedt_var.set(row[5])  # Set ISSUE_DT
                self.expdt_var.set(row[6])  # Set EXP_DT
                self.uses_var.set(row[7])  # Set USES
                self.sideeffect_var.set(row[8])  # Set SIDE_EFFECT
                self.warning_var.set(row[9])  # Set PRECAUTION
                self.dosage_var.set(row[10])  # Set DOSAGE
                self.price_var.set(row[11])  # Set PRICE
                self.quantity_var.set(row[12])  # Set QUANTITY
            else:
                print("Row is empty or not in the expected format.")

    def update_new(self):
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



    def clear_new(self):
        self.refno_var.set("")
        self.companyname_var.set("")
        self.typemed_var.set("")
        self.medicine_var.set("")
        self.lotno_var.set("")
        self.issuedt_var.set("")
        self.expdt_var.set("")
        self.uses_var.set("")
        self.sideeffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")
    

    def search_data(self):

        conn = sqlite3.connect(database='pharmacy.db')
        new_cursor=conn.cursor()
        selected = self.search_combo.get()
        if selected == "Select Options":
            messagebox.showerror("Error","You have to choose an option")

        else:
            new_cursor.execute("Select * from Information where REF_NO=?",(self.search_txt.get(),))
            row=new_cursor.fetchone()

            if len(row)!=0:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("",END,values=i)

                conn.commit()
    def slider(self):
        if self.count>=len(self.txt):
            self.count=-1
            self.text=""
            self.heading.config(text=self.text)
        else:
            self.text=self.text+self.txt[self.count]
            self.heading.config(text=self.text)
        self.count+=1
        self.heading.after(200,self.slider)
    def heading_color(self):
        fg=random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(100,self.heading_color)


def main():
    root=Tk()
    obj=Pharmacy(root)
    root.mainloop()

if __name__ == '__main__':
    main()
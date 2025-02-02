from tkinter import *
from tkinter import messagebox, simpledialog
import json
import os
import hashlib
from PIL import Image, ImageTk

def hash_password(password):
    # SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def signup():
    username = user.get()
    password = code.get()
    confirm_password = conform_code.get()

    if password == confirm_password:
        try:
            # Hashed password
            hashed_password = hash_password(password)

            with open('datasheet.json', 'r') as file:
                data = json.load(file)

            data[username] = hashed_password

            with open('datasheet.json', 'w') as file:
                json.dump(data, file)

            messagebox.showinfo('Sign Up', 'Successfully Signed Up')
        except FileNotFoundError:
            data = {username: hashed_password}
            with open('datasheet.json', 'w') as file:
                json.dump(data, file)
            messagebox.showinfo('Sign Up', 'Successfully Signed Up')
        except Exception as e:
            print(e)
            messagebox.showerror('Error', 'An error occurred while signing up.')
    else:
        messagebox.showerror('Invalid', 'Both Passwords should match!')

def signin():
    username = user.get()

    # Prompt the user for an additional password
    additional_password = simpledialog.askstring("Additional Password", "Enter additional password:", show='*')

    # Check if the additional password is correct
    if additional_password == 'Prasath@18':
        try:
            with open('datasheet.json', 'r') as file:
                data = json.load(file)

            # Check if username exists in the loaded JSON data
            if username in data:
                stored_password = data[username]
                # Hash the provided password
                provided_password = hash_password(code.get())
                # Check if the hashed provided password matches the stored hashed password
                if stored_password == provided_password:
                    messagebox.showinfo('Sign In', 'Successfully Signed In')
                    open_second_gui()
                else:
                    messagebox.showerror('Invalid', 'Invalid Username or Password')
            else:
                messagebox.showerror('Invalid', 'Invalid Username or Password')

        except FileNotFoundError:
            messagebox.showerror('File Not Found', 'User data file not found. Please sign up first.')
        except json.JSONDecodeError:
            messagebox.showerror('Invalid Data', 'User data is not valid. Please sign up again.')
        except Exception as e:
            print(e)
            messagebox.showerror('Error', 'An error occurred while signing in.')
    else:
        messagebox.showerror('Invalid', 'Additional password is incorrect.')

def open_second_gui():
    os.system('pythonw med.py')

window = Tk()
window.title("Sign Up / Sign In")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size to fit the screen
window.geometry(f"{screen_width}x{screen_height}")
window.configure(bg='#fff')

# Create a grid layout with rows and columns to make it responsive
window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Your GUI elements
original_image = Image.open("image (1).png")
img = ImageTk.PhotoImage(original_image)

# Increase the size of the image by specifying width and height
label = Label(window, image=img, border=0, bg='white', width=300, height=2000)
label.grid(row=0, column=0, sticky='nsew')

frame = Frame(window, bg='#fff')
frame.grid(row=0, column=1, sticky='nsew')

heading = Label(frame,width=30, fg='black', border=0, bg='white', font=('Microsoft Yahei UI LIGHT', 11))

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI LIGHT', 11))
user.place(x=30, y=230)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=250)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI LIGHT', 11))
code.place(x=30, y=290)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=310)

def on_enter(e):
    conform_code.delete(0, 'end')

def on_leave(e):
    if conform_code.get() == '':
        conform_code.insert(0, 'Confirm Password')

conform_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI LIGHT', 11))
conform_code.place(x=30, y=350)
conform_code.insert(0, 'Confirm Password')
conform_code.bind("<FocusIn>", on_enter)
conform_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=370)

Button(frame, width=42, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).grid(row=20, column=0, pady=(340,10),padx=25)
Button(frame, width=10, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).grid(row=20, column=0,pady=(450,20),padx=(10,23),sticky='e')

# Label for "I have an account"
label_signup = Label(frame, text='I have an account=>=>', fg='black', bg='white', font=('Microsoft Yahei UI LIGHT', 9))
label_signup.grid(row=21, column=0 ,columnspan=2,sticky='w', padx=(0, 10))
label_signup.place(x=25,y=460)


# Set column and row weights to make the frame expand to fit the screen
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

window.mainloop()


import tkinter as tk
import sqlite3
from tkinter import messagebox, ttk

root = tk.Tk()
root.geometry('700x500')
root.title('Tkinter Hub')


conn = sqlite3.connect('login_data.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS people
             (name TEXT, age INTEGER, email TEXT, phone TEXT)''')



def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def login_page():
    def forward_register_page():
        login_frame.destroy()
        register_page()

    def toggle_password_visibility():
        if password['show'] == '*':
            password.config(show='')
            show_hide_btn.config(text='Hide')
        else:
            password.config(show='*')
            show_hide_btn.config(text='See')

    def login():
        entered_username = username.get()
        entered_password = password.get()

        c.execute('SELECT * FROM users WHERE username=? AND password=?', (entered_username, entered_password))
        result = c.fetchone()

        if result:
            login_frame.destroy()
            create_records_page()
        else:
            messagebox.showerror("Invalid Credentials", "Invalid username or password!")

    login_frame = tk.Frame(root)

    username_lb = tk.Label(login_frame, bg='white', text='Enter Username', font=('Arial', 11))
    username_lb.place(x=65, y=20)

    username = tk.Entry(login_frame, font=('Arial', 11), highlightthickness=1, highlightcolor='#158aff')
    username.place(x=50, y=45, width=140, height=30)

    password_lb = tk.Label(login_frame, bg='white', text='Enter Password', font=('Arial', 11))
    password_lb.place(x=65, y=90)

    password = tk.Entry(login_frame, font=('Arial', 11), show='*', highlightthickness=1, highlightcolor='#158aff')
    password.place(x=50, y=120, width=140, height=30)

    show_hide_btn = ttk.Button(login_frame, text="See", command=toggle_password_visibility)
    show_hide_btn.place(x=420, y=133, width=335)

    login_btn = tk.Button(login_frame, text='Login', font=('Arial', 12), bg='#158aff', fg='white', command=login)
    login_btn.place(x=51, y=155, width=140)

    register_page_link = tk.Button(login_frame, text='Register', font=('Arial', 12), fg='#158aff', bd=0, underline=True,
                                   command=forward_register_page)
    register_page_link.place(x=17, y=195, width=120)

    login_frame.pack(pady=10)
    login_frame.pack_propagate(False)

    login_frame.configure(height=400, width=250)


def create_records_page():
    def logout():
        records_window.destroy()
        login_page()

    def create_record_person():
        def save_person():
            name_val = name_entry.get()
            age_val = age_entry.get()
            email_val = email_entry.get()
            phone_val = phone_entry.get()

            if not name_val or not age_val or not email_val or not phone_val:
                messagebox.showerror("Incomplete Form", "Please fill in all fields.")
                return

            c.execute("INSERT INTO people (name, age, email, phone) VALUES (?, ?, ?, ?)",
                      (name_val, age_val, email_val, phone_val))
            conn.commit()
            messagebox.showinfo("Success", "Person added successfully!")
            create_person_window.destroy()

        create_person_window = tk.Toplevel(root)
        create_person_window.geometry('400x300')
        create_person_window.title('Create Person')

        name_label = tk.Label(create_person_window, text='Name:', font=('Arial', 12))
        name_label.pack(pady=10)
        name_entry = tk.Entry(create_person_window, font=('Arial', 12))
        name_entry.pack()

        age_label = tk.Label(create_person_window, text='Age:', font=('Arial', 12))
        age_label.pack(pady=10)
        age_entry = tk.Entry(create_person_window, font=('Arial', 12))
        age_entry.pack()

        email_label = tk.Label(create_person_window, text='Email:', font=('Arial', 12))
        email_label.pack(pady=10)
        email_entry = tk.Entry(create_person_window, font=('Arial', 12))
        email_entry.pack()

        phone_label = tk.Label(create_person_window, text='Phone:', font=('Arial', 12))
        phone_label.pack(pady=10)
        phone_entry = tk.Entry(create_person_window, font=('Arial', 12))
        phone_entry.pack()

        save_button = tk.Button(create_person_window, text='Save', font=('Arial', 12), bg='#158aff', fg='white',
                                command=save_person)
        save_button.pack(pady=10)

    def edit_record_person():
    
        pass

    def delete_record_person():
         global tree
         selected_item = tree.selection()
         if selected_item:
           confirmation = messagebox.askyesno("Delete Person", "Are you sure you want to delete this person?")
           if confirmation:
            item_values = tree.item(selected_item)['values']
            name = item_values[0]
            c.execute("DELETE FROM people WHERE name=?", (name,))
            conn.commit()
            messagebox.showinfo("Success", "Person deleted successfully!")
            show_people_list(tree)

    def show_people_list():
        people_window = tk.Toplevel(root)
        people_window.geometry('500x400')
        people_window.title('People List')

        c.execute("SELECT * FROM people")
        records = c.fetchall()

        global tree  
        
        tree = ttk.Treeview(people_window)
        tree["columns"] = ("name", "age", "email", "phone")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("name", anchor=tk.CENTER, width=100)
        tree.column("age", anchor=tk.CENTER, width=50)
        tree.column("email", anchor=tk.CENTER, width=150)
        tree.column("phone", anchor=tk.CENTER, width=100)

        tree.heading("#0", text="", anchor=tk.CENTER)
        tree.heading("name", text="Name", anchor=tk.CENTER)
        tree.heading("age", text="Age", anchor=tk.CENTER)
        tree.heading("email", text="Email", anchor=tk.CENTER)
        tree.heading("phone", text="Phone", anchor=tk.CENTER)

        for record in records:
            tree.insert("", tk.END, text="", values=(record[0], record[1], record[2], record[3]))

        tree.pack(expand=tk.YES, fill=tk.BOTH)

    records_window = tk.Toplevel(root)
    records_window.geometry('500x400')
    records_window.title('Records')

    create_frame = tk.Frame(records_window)
    create_frame.pack(pady=10)

    create_label = tk.Label(create_frame, text='Select record type:', font=('Arial', 12))
    create_label.pack()

    create_btn_person = tk.Button(create_frame, text='Create Person', font=('Arial', 12), bg='#158aff', fg='white',
                                  command=create_record_person)
    create_btn_person.pack(pady=5)

    edit_btn_person = tk.Button(create_frame, text='Edit Person', font=('Arial', 12), bg='#158aff', fg='white',
                                command=edit_record_person)
    edit_btn_person.pack(pady=5)

    delete_btn_person = tk.Button(create_frame, text='Delete Person', font=('Arial', 12), bg='#158aff', fg='white',
                                  command=delete_record_person)
    delete_btn_person.pack(pady=5)

    show_btn_people = tk.Button(create_frame, text='Show People List', font=('Arial', 12), bg='#158aff', fg='white',
                                command=show_people_list)
    show_btn_people.pack(pady=5)

    logout_btn = tk.Button(records_window, text='Logout', font=('Arial', 12), bg='#158aff', fg='white',
                           command=logout)
    logout_btn.pack(pady=10)

    records_window.mainloop()


def register_page():
    def forward_login_page():
        register_frame.destroy()
        login_page()

    def register():
        entered_username = username.get()
        entered_password = password.get()
        repeat_password = repeat_password_entry.get()

        if entered_password != repeat_password:
            messagebox.showerror("Password Mismatch", "Passwords don't match!")
        else:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (entered_username, entered_password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")

    register_frame = tk.Frame(root)

    username_lb = tk.Label(register_frame, text='Enter Username', font=('Arial', 12))
    username_lb.place(x=200, y=20)

    username = tk.Entry(register_frame, font=('Arial', 12), bd=0, highlightbackground='gray',
                        highlightcolor='#158aff', highlightthickness=1)
    username.place(x=200, y=60, width=140, height=30)

    password_lb = tk.Label(register_frame, bg='white', text='Enter Password', font=('Arial', 11))
    password_lb.place(x=200, y=90)

    password = tk.Entry(register_frame, font=('Arial', 11), show='*', highlightthickness=1, highlightcolor='#158aff')
    password.place(x=200, y=120, width=140, height=30)

    repeat_password_lb = tk.Label(register_frame, bg='white', text='Repeat Password', font=('Arial', 11))
    repeat_password_lb.place(x=200, y=160)

    repeat_password_entry = tk.Entry(register_frame, font=('Arial', 11), show='*', highlightthickness=1,
                                     highlightcolor='#158aff')
    repeat_password_entry.place(x=200, y=180, width=140, height=30)

    register_btn = tk.Button(register_frame, text='Register', font=('Arial', 12), bg='#158aff', fg='white',
                             command=register)
    register_btn.place(x=200, y=220, width=150)

    login_page_link = tk.Button(register_frame, text='Login', fg='#158aff', underline=True, font=('Arial', 12), bd=0,
                                command=forward_login_page)
    login_page_link.place(x=220, y=255)

    register_frame.pack()
    register_frame.configure(height=400, width=400)


center_window(root)
login_page()
root.mainloop()
from tkinter import Frame

import pandas as pd
import tkinter as tk
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base



Base = declarative_base()


def connect_db():

    label = tk.Label(window, text="Podaj swoje dane do logowania bazy dancyh")
    label.pack()
    user_name = tk.Entry(window, bg="#fdbce1", width=30)
    user_name.pack()
    password = tk.Entry(window, bg="#fdbce1", width=30, show='*')
    password.pack()
    db_host = tk.Entry(window, bg="#fdbce1", width=30)
    db_host.pack()
    db_name1 = tk.Entry(window, bg="#fdbce1", width=30)
    db_name1.pack()

    db_user = str(user_name.get())
    db_password = str(password.get())
    db_hostname = str(db_host.get())
    db_name = str(db_name1.get())


def create_new_db():
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Enter database name to create: ",bg='#333',fg='white').grid(row=0,column=0,padx=5)
    db_name_enter = tk.Entry(frame)
    db_name_enter.grid(row=1,column=0,padx=5,columnspan=3)
    tk.Button(frame,text='Go back:',command=main_window).grid(row=2,column=0,pady=5)



    def create_db():
        db_name = str(db_name_enter.get())
        if db_name:
            engine = create_engine(f'sqlite:///{db_name}.db')
            Base.metadata.create_all(engine)
            tk.Label(frame, text=f"Database '{db_name}' created successfully!", bg='#333', fg='white').grid(row=3, column=0, pady=5)
        else:
            tk.Label(frame, text="Database name cannot be empty", bg='#333', fg='red').grid(row=3, column=0, pady=5)

    tk.Button(frame, text='Create',command=create_db).grid(row=1, column=1, pady=5, padx=5)





window = tk.Tk()
window.title("SQL Managment App")
window.geometry("440x320")
window.configure(bg='#333')
frame =Frame(window,bg='#333')
frame.pack(pady=20, padx=20)

def main_window():
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame,text="Choose your action: ",bg='#333',fg='white').grid(row=0, column=0,pady=5)

    create_db_button = tk.Button(frame, text="Create new local DataBase", command=create_new_db, bg='#333', fg='white').grid(row=1, column=0, pady=5)
    load_db_button =tk.Button(frame,text="Load local DataBase",bg='#333',fg='white').grid(row=2,column=0,pady=5)

main_window()
window.mainloop()
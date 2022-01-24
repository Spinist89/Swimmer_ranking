import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Настройка соревнования')
window.geometry('500x300')

frame_setting = tk.Frame(window, width=500, height=150, bg='green')
frame_setting.place(relx=0, rely=0, relwidth=1, relheight=1)


s_search_name = ttk.Entry(frame_setting, justify=tk.CENTER)
s_search_button = ttk.Button(frame_setting, text="Найти")
s_change_button = ttk.Button(frame_setting, text="ИЗМЕНИТЬ")

s_search_name.grid(row=0, column=0)
s_search_button.grid(row=0, column=1)
s_change_button.grid(row=0, column=2)

window.mainloop()
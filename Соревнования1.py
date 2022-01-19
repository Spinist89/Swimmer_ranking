import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry, Calendar

window = tk.Tk()
window.title('Соревнования № РАЗЗЗ')
window.geometry('775x500')
window.minsize(499,499)

frame_top_menu = tk.Frame(window, width=500, height=50, bg='green')
frame_swim_window = tk.Frame(window, width=350, height=200, bg='yellow')
frame_buttons = tk.Frame(window, width=150, height=200, bg='blue')
frame_manual_entry_field = tk.Frame(window, width=500, height=50, bg='red')

frame_top_menu.place(relx=0, rely=0, relwidth=1, relheight=0.2)
frame_swim_window.place(relx=0, rely=0.1, relwidth=0.7, relheight=0.6)
frame_buttons.place(relx=0.7, rely=0.1, relwidth=0.3, relheight=0.6)
frame_manual_entry_field.place(relx=0, rely=0.7, relwidth=1, relheight=0.4)

#  Поле таблица дистанций
lst = [('Фамил', 'Им', 'отч', 12, 2.09),
       (2, 12, 2.09),
       (3, 12, 2.09),
       (4, 12, 2.09),
        (5, 12, 2.09),
        (6, 12, 2.09),
       (7, 12, 2.09),
       (8, 12, 2.09),
       (9, 12, 2.09),
       (10, 12, 2.09),
       (11, 12, 2.09),
       (12, 12, 2.09),
        (1, 12, 2.09),
       (2, 12, 2.09),
       (3, 12, 2.09),
       (4, 12, 2.09),
        (5, 12, 2.09),
        (6, 12, 2.09),
       (7, 12, 2.09),
       (8, 12, 2.09),
       (9, 12, 2.09),
       (10, 12, 2.09),
       (11, 12, 2.09),
       (12, 12, 2.09),
       ]

heads = ['Фамилия', 'Имя', 'Отчество', "Дата рождения", "Предварительный результат"]
table = ttk.Treeview(frame_swim_window, show='headings') #show='headings' убирает первый пустой столбец
table['columns'] = heads
table['displaycolumns'] = ['Фамилия', 'Имя', 'Отчество', "Дата рождения", "Предварительный результат"] #установка порядка столбцов

for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center')
for row in lst:
    table.insert('', tk.END, values=row)

scroll_pane = ttk.Scrollbar(frame_swim_window, command=table.yview) #добавление ползунка скролинга
table.configure(yscrollcommand=scroll_pane.set)
scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)



table.pack(expand=tk.YES, fill=tk.BOTH)

# Поле кнопочек
v_import_document = ttk.Button(frame_buttons, text="Импортировать документ")
v_competition_setup = ttk.Button(frame_buttons, text="Настройка соревнования")
v_export_document = ttk.Button(frame_buttons, text="Эксспортировать документ")

v_import_document.grid(row=0, column=0)
v_competition_setup.grid(row=1, column=0)
v_export_document.grid(row=2, column=0)

# Поле добавления спортсмена
distance = [1, 2, 3, 4, 5]

e_athletes_name = ttk.Entry(frame_manual_entry_field, justify=tk.CENTER)
e_athletes_age = DateEntry(frame_manual_entry_field, date_pattern="dd-mm-YYYY")
e_athletes_result = ttk.Entry(frame_manual_entry_field, justify=tk.CENTER)
e_choice_of_distance = ttk.Combobox(frame_manual_entry_field, values=distance)
e_button_add = ttk.Button(frame_manual_entry_field, text='Добавить спорсмена') #command=.......

e_athletes_name.grid(row=0, column=0)
e_athletes_age.grid(row=0, column=1)
e_athletes_result.grid(row=0, column=2)
e_choice_of_distance.grid(row=0, column=3)
e_button_add.grid(row=0, column=4)


window.mainloop()
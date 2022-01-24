import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Поиск спортсмена')
window.geometry('500x300')

frame_search = tk.Frame(window, width=500, height=150, bg='green')
frame_addition = tk.Frame(window, width=500, height=350, bg='yellow')

frame_search.place(relx=0, rely=0, relwidth=1, relheight=0.3)
frame_addition.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

#Поле поиска
s_search_name = ttk.Entry(frame_search, justify=tk.CENTER)
s_search_button = ttk.Button(frame_search, text="Найти")
s_change_button = ttk.Button(frame_search, text="ИЗМЕНИТЬ")

s_search_name.grid(row=0, column=0)
s_search_button.grid(row=0, column=1)
s_change_button.grid(row=0, column=2)

#поле изменения
# lst = [('Фамил', 'Им', 'отч', 12, 2.09),
#        (2, 12, 2.09),
#        (3, 12, 2.09),
#        (4, 12, 2.09),
#         (5, 12, 2.09),
#         (6, 12, 2.09),
#        ]

heads = ['Фамилия', 'Имя', 'Отчество', "Дата рождения", "Предварительный результат"]
table = ttk.Treeview(frame_addition, show='headings') #show='headings' убирает первый пустой столбец
table['columns'] = heads
table['displaycolumns'] = ['Фамилия', 'Имя', 'Отчество', "Дата рождения", "Предварительный результат"] #установка порядка столбцов

for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center')
# for row in lst:
#     table.insert('', tk.END, values=row)

scroll_content_x = ttk.Scrollbar(frame_addition, orient='horizontal', command=table.xview)
scroll_content_x.pack(side=tk.BOTTOM, fill=tk.BOTH)
table.configure(xscrollcommand=scroll_content_x.set)

scroll_content_y = ttk.Scrollbar(frame_addition, command=table.yview)
table.configure(yscrollcommand=scroll_content_y.set)
scroll_content_y.pack(side=tk.RIGHT, fill=tk.Y)

table.pack(expand=tk.YES, fill=tk.BOTH)


window.mainloop()
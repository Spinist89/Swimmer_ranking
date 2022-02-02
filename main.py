from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import filedialog as fd

import tkinter as tk
import athlete_search as atlser
import competition_setup as comset

class Main_screen(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Соревнования № РАЗЗЗ')
        self.minsize(499, 499)
        self.geometry('775x500')
        self.frames()

    def frames(self):
        self.frame_top_menu()
        self.frame_swim_window()
        self.frame_buttons()
        self.frame_manual_entry_field()

    def frame_top_menu(self):
        frame_top_menu = tk.Frame(self, width=500, height=50, bg='green')
        frame_top_menu.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    def frame_swim_window(self):
        frame_swim_window = tk.Frame(self, width=350, height=200, bg='yellow')
        frame_swim_window.place(relx=0, rely=0.1, relwidth=0.7, relheight=0.6)
        lst = [('Фамил', 'Им', 'отч', 12, 2.09),
               (2, 12, 2.09),
               (3, 12, 2.09),
               (4, 12, 2.09),
               ]
        heads = ['Фамилия', 'Имя', 'Отчество', "Год рождения", "Пол", "Предварительный результат", "Тренер",
                 "Итоговый результат", "Разряд", "Место"]
        table = ttk.Treeview(frame_swim_window, show='headings')  # show='headings' убирает первый пустой столбец
        table['columns'] = heads
        table['displaycolumns'] = ['Фамилия', 'Имя', 'Отчество', "Год рождения", "Пол", "Предварительный результат",
                                   "Тренер", "Итоговый результат", "Разряд", "Место"]  # установка порядка столбцов
        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')
        for row in lst:
            table.insert('', tk.END, values=row)
        scroll_pane = ttk.Scrollbar(frame_swim_window, command=table.yview)  # добавление ползунка скролинга по оси Y
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_content_x = ttk.Scrollbar(frame_swim_window, orient='horizontal', command=table.xview) # добавление ползунка скролинга по оси X
        scroll_content_x.pack(side=tk.BOTTOM, fill=tk.BOTH)
        table.configure(xscrollcommand=scroll_content_x.set)
        table.pack(expand=tk.YES, fill=tk.BOTH)

    def frame_buttons(self):
        frame_buttons = tk.Frame(self, width=150, height=200, bg='blue')
        frame_buttons.place(relx=0.7, rely=0.1, relwidth=0.3, relheight=0.6)

        v_import_document = ttk.Button(frame_buttons, text="Импортировать документ", command=lambda:print(fd.askopenfilename()))
        v_competition_setup = ttk.Button(frame_buttons, text="Настройка соревнования", command=comset.Competition_setup)
        v_athlete_search = ttk.Button(frame_buttons, text="Поиск спортсмена", command=atlser.Athlete_search)
        v_remove_athlete = ttk.Button(frame_buttons, text="Удалить спортсмена")
        v_export_document = ttk.Button(frame_buttons, text="Эксспортировать документ")

        v_import_document.grid(row=0, column=0, padx=10, pady=10)
        v_competition_setup.grid(row=1, column=0, padx=10, pady=10)
        v_athlete_search.grid(row=2, column=0, padx=10, pady=10)
        v_remove_athlete.grid(row=3, column=0, padx=10, pady=10)
        v_export_document.grid(row=4, column=0, padx=10, pady=10)

    def frame_manual_entry_field(self):
        frame_manual_entry_field = tk.Frame(self, width=500, height=50, bg='red')
        frame_manual_entry_field.place(relx=0, rely=0.7, relwidth=1, relheight=0.4)
        distance = [1, 2, 3, 4, 5]

        e_athletes_name = ttk.Entry(frame_manual_entry_field, justify=tk.CENTER)
        e_athletes_age = DateEntry(frame_manual_entry_field, date_pattern="dd-mm-YYYY")
        e_athletes_result = ttk.Entry(frame_manual_entry_field, justify=tk.CENTER)
        e_choice_of_distance = ttk.Combobox(frame_manual_entry_field, values=distance)
        e_button_add = ttk.Button(frame_manual_entry_field, text='Добавить спорсмена')  # command=.......

        e_athletes_name.grid(row=0, column=0)
        e_athletes_age.grid(row=0, column=1)
        e_athletes_result.grid(row=0, column=2)
        e_choice_of_distance.grid(row=0, column=3)
        e_button_add.grid(row=0, column=4)

        e_athletes_age._top_cal.overrideredirect(False)  # исправление ошибка календаря на макОС

main_screen = Main_screen()
main_screen.mainloop()
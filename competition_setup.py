import tkinter as tk
from tkinter import ttk

class CompetitionSetup(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Настройка соревнования')
        self.FONT = 'Helvetica 14 bold'
        self.geometry('650x300')
        self.frame_setting()

    def frame_setting(self):
        frame_setting = tk.Frame(self, width=500, height=150, bg='grey')
        frame_setting.place(relx=0, rely=0, relwidth=1, relheight=1)

        tracks = ['4', '6', '8']

        s_competition_name = ttk.Label(frame_setting, text='Название соеревнований', font=self.FONT)
        s_competition_name_input = ttk.Entry(frame_setting, justify=tk.CENTER)
        s_distances = ttk.Label(frame_setting, text='Дистанции', font=self.FONT)
        s_distances_input = ttk.Entry(frame_setting, justify=tk.CENTER)
        s_add_distance = ttk.Button(frame_setting, text='Добавить дистанцию')
        s_window_distance = ttk.Label(frame_setting)
        s_drop_distance = ttk.Button(frame_setting, text='Удалить дистанцию')
        s_number_of_tracks = ttk.Label(frame_setting, text='Количество дорожек', font=self.FONT)
        s_number_of_tracks1 = ttk.Combobox(frame_setting, values=tracks)
        s_save_button = ttk.Button(frame_setting, text='Сохранить')

        s_competition_name.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        s_competition_name_input.grid(row=0, column=1, sticky='e', padx=10, pady=10)
        s_distances.grid(row=1, column=0, sticky='w', padx=10, pady=10)
        s_distances_input.grid(row=1, column=1, padx=10, pady=10)
        s_add_distance.grid(row=1, column=2, sticky='e', padx=10, pady=10)
        s_window_distance.grid(row=2, column=0, columnspan=2, sticky='w', padx=10, pady=10)
        s_drop_distance.grid(row=2, column=2, sticky='e', padx=10, pady=10)
        s_number_of_tracks.grid(row=3, column=0, sticky='w', padx=10, pady=10)
        s_number_of_tracks1.grid(row=3, column=1, padx=10, pady=10)
        s_save_button.grid(row=3, column=2, sticky='e', padx=10, pady=10)

if __name__=="__main__":
    competition_setup = Competition_setup()
    competition_setup.mainloop()
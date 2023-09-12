# ***Algorithmic simulator***
# Task 1
# import tkinter
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.label = tkinter.Label(self.main_window, text='Programming is cool!')
#         self.label.pack()
#         tkinter.mainloop()
#
#
# my_gui = MyGUI()
# Task 2
# import tkinter
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.label1 = tkinter.Label(self.main_window, text='Hello')
#         self.label2 = tkinter.Label(self.main_window, text='Hello2')
#         self.label1.pack(side='left')
#         self.label2.pack(side='left')
#         tkinter.mainloop()
#
#
# my_gui = MyGUI()
# Task 3
# import tkinter
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.top_frame = tkinter.Frame(self.main_window)
#         self.label = tkinter.Label(self.top_frame, text='Hello')
#         self.label.pack(side='top')
#         self.top_frame.pack()
#         tkinter.mainloop()
#
#
# my_gui = MyGUI()
# Task 4
# import tkinter
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.top_frame = tkinter.Frame(self.main_window)
#         self.bottom_frame = tkinter.Frame(self.main_window)
#         self.label1 = tkinter.Label(self.top_frame, text='Stop')
#         self.label1.pack(side='top')
#         self.label2 = tkinter.Label(self.bottom_frame, text='Press enter')
#         self.label2.pack(side='left')
#         self.top_frame.pack()
#         self.bottom_frame.pack()
#         tkinter.mainloop()
#
#
# my_gui = MyGUI()
# Task 5
# import tkinter
# import tkinter.messagebox
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.my_button = tkinter.Button(
#             self.main_window,
#             text='Calculate',
#             command=self.calc
#             )
#         self.my_button.pack()
#         tkinter.mainloop()
#
#     def calc(self):
#         tkinter.messagebox.showinfo('Thanks!', 'Calculate')
#
#
# my_gui = MyGUI()
# Task 6
# import tkinter
# import tkinter.messagebox
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.my_button = tkinter.Button(
#             self.main_window,
#             text='Quit',
#             command=self.main_window.destroy
#         )
#         self.my_button.pack()
#         tkinter.mainloop()
#
#
# my_gui = MyGUI()
# Task 7
# import tkinter
# import tkinter.messagebox
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.top_frame = tkinter.Frame(self.main_window)
#         self.bottom_frame = tkinter.Frame(self.main_window)
#         self.prompt_label = tkinter.Label(self.top_frame, text='Enter:')
#         self.converter_entry = tkinter.Entry(self.top_frame, width=12)
#         self.prompt_label.pack(side='left')
#         self.converter_entry.pack(side='left')
#         self.converter_button = tkinter.Button(
#             self.bottom_frame,
#             text='Convert',
#             command=self.convert
#         )
#         self.converter_button.pack(side='left')
#         self.top_frame.pack()
#         self.bottom_frame.pack()
#         tkinter.mainloop()
#
#     def convert(self):
#         var = int(self.converter_entry.get())
#         tkinter.messagebox.showinfo(
#              'Results',
#              str(var)
#         )
#
#
# converter = MyGUI()
# ***Programming tasks***
# Task 1
# import tkinter
# import tkinter.messagebox
#
#
# class MyGUI:
#     def __init__(self):
#         self.text = 'Python is powerful!'
#         self.main_window = tkinter.Tk()
#         self.top_frame = tkinter.Frame(self.main_window)
#         self.bottom_frame = tkinter.Frame(self.main_window)
#         self.address = tkinter.StringVar()
#         self.label = tkinter.Label(self.top_frame, textvariable=self.address)
#         self.label.pack(side='left')
#         self.my_button = tkinter.Button(
#             self.bottom_frame,
#             text='Show info',
#             command=self.show_info
#         )
#         self.quit_button = tkinter.Button(
#             self.bottom_frame,
#             text='Quit',
#             command=self.main_window.destroy
#         )
#         self.my_button.pack(side='left')
#         self.quit_button.pack(side='left')
#         self.top_frame.pack()
#         self.bottom_frame.pack()
#         self.main_window.mainloop()
#
#     def show_info(self):
#         self.address.set(self.text)
#
#
# my_info = MyGUI()
# Task 2
# import tkinter
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.top_frame = tkinter.Frame(self.main_window)
#         self.bottom_frame = tkinter.Frame(self.main_window)
#         self.translate1 = tkinter.StringVar()
#         self.translate2 = tkinter.StringVar()
#         self.translate3 = tkinter.StringVar()
#         self.label1 = tkinter.Label(
#             self.top_frame,
#             textvariable=self.translate1
#         )
#         self.label2 = tkinter.Label(
#             self.top_frame,
#             textvariable=self.translate2
#         )
#         self.label3 = tkinter.Label(
#             self.top_frame,
#             textvariable=self.translate3
#         )
#         self.label1.pack(side='left')
#         self.label2.pack(side='left')
#         self.label3.pack(side='left')
#         self.first_button = tkinter.Button(
#             self.bottom_frame,
#             text='Brother',
#             command=self.show_info1
#         )
#         self.second_button = tkinter.Button(
#             self.bottom_frame,
#             text='Sister',
#             command=self.show_info2
#         )
#         self.third_button = tkinter.Button(
#             self.bottom_frame,
#             text='Road',
#             command=self.show_info3
#         )
#         self.label1.pack(side='right')
#         self.label2.pack(side='right')
#         self.label3.pack(side='right')
#         self.first_button.pack(side='left')
#         self.second_button.pack(side='left')
#         self.third_button.pack(side='left')
#         self.top_frame.pack()
#         self.bottom_frame.pack()
#         self.main_window.mainloop()
#
#     def show_info1(self):
#         self.translate1.set('Брат')
#
#     def show_info2(self):
#         self.translate2.set('Сестра')
#
#     def show_info3(self):
#         self.translate3.set('Дорога')
#
#
# my_gui = MyGUI()
# Task 3
# import tkinter
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.first_frame = self.create_first_frame()
#         self.second_frame = tkinter.Frame(self.main_window)
#         self.third_frame = tkinter.Frame(self.main_window)
#         self.fourth_frame = tkinter.Frame(self.main_window)
#         self.label1 = tkinter.Label(
#             self.first_frame,
#             text='Enter number of gallons: '
#         )
#         self.first_entry = tkinter.Entry(self.first_frame, width=10)
#         self.label2 = tkinter.Label(
#             self.second_frame,
#             text='Enter number of mills: '
#         )
#         self.second_entry = tkinter.Entry(self.second_frame, width=10)
#         self.display_message = tkinter.Label(
#             self.third_frame,
#             text='MPG = '
#         )
#         self.result = tkinter.StringVar()
#         self.show_miles = tkinter.Label(
#             self.third_frame,
#             textvariable=self.result
#         )
#         self.calculate_button = tkinter.Button(
#             self.fourth_frame,
#             text='Calculate',
#             command=self.calculate
#         )
#         self.quit_button = tkinter.Button(
#             self.fourth_frame,
#             text='Quit',
#             command=self.main_window.destroy
#         )
#         self.label1.pack(side='left')
#         self.first_entry.pack(side='left')
#         self.label2.pack(side='left')
#         self.second_entry.pack(side='left')
#         self.calculate_button.pack(side='left')
#         self.quit_button.pack(side='left')
#         self.display_message.pack(side='left')
#         self.show_miles.pack(side='left')
#         self.first_frame.pack()
#         self.second_frame.pack()
#         self.third_frame.pack()
#         self.fourth_frame.pack()
#         self.main_window.mainloop()
#
#     def calculate(self):
#         result = (int(self.second_entry.get()) / int(self.first_entry.get()))
#         self.result.set(format(result, ",.2f"))
#
#     def create_first_frame(self):
#         return tkinter.Frame(self.main_window)
#
#
# my_gui = MyGUI()
# Task 4
class MyGUI:
    def __init(self):

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
# import tkinter
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.top_frame = self.create_top_frame()
#         self.middle_frame = self.create_middle_frame()
#         self.bottom_frame = self.create_bottom_frame()
#         self.label1 = self.create_label1()
#         self.entry = self.create_entry()
#         self.label1.pack(side='left')
#         self.entry.pack(side='left')
#         self.label2 = self.create_label2()
#         self.result = tkinter.StringVar()
#         self.calculate_result = self.show_temperature()
#         self.label2.pack(side='left')
#         self.calculate_result.pack(side='left')
#         self.quit_button = self.create_quit_button()
#         self.calculate_button = self.create_calculate_button()
#         self.quit_button.pack(side='left')
#         self.calculate_button.pack(side='left')
#         self.top_frame.pack()
#         self.middle_frame.pack()
#         self.bottom_frame.pack()
#         self.main_window.mainloop()
#
#     def create_top_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_middle_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_bottom_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_label1(self):
#         return tkinter.Label(
#             self.top_frame,
#             text='Input temperature in C:'
#         )
#
#     def show_temperature(self):
#         return tkinter.Label(
#             self.middle_frame,
#             textvariable=self.result
#         )
#
#     def create_entry(self):
#         return tkinter.Entry(
#             self.top_frame,
#             width=10
#         )
#
#     def create_label2(self):
#         return tkinter.Label(
#             self.middle_frame,
#             text='Temperature in F:'
#         )
#
#     def create_quit_button(self):
#         return tkinter.Button(
#             self.bottom_frame,
#             text='Quit',
#             command=self.main_window.destroy
#         )
#
#     def create_calculate_button(self):
#         return tkinter.Button(
#             self.bottom_frame,
#             text='Calculate',
#             command=self.calculate
#         )
#
#     def calculate(self):
#         result = (9*(int(self.entry.get()))/5 + 32)
#         self.result.set(str(result))
#
#
# my_gui = MyGUI()
# Task 5
# import tkinter
#
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.top_frame = self.create_top_frame()
#         self.top2_frame = self.create_top2_frame()
#         self.middle_frame = self.create_middle_frame()
#         self.bottom_frame = self.create_bottom_frame()
#         self.label1 = self.create_label1()
#         self.entry = self.create_entry()
#         self.label2 = self.create_label2()
#         self.assessment_value = tkinter.StringVar()
#         self.total_value = self.show_value()
#         self.label3 = self.create_label3()
#         self.property_tax = tkinter.StringVar()
#         self.total_tax = self.show_tax()
#         self.calculate_button = self.create_calculate_button()
#         self.quit_button = self.create_quit_button()
#         self.label1.pack(side='left')
#         self.entry.pack(side='left')
#         self.label2.pack(side='left')
#         self.label3.pack(side='left')
#         self.total_value.pack(side='left')
#         self.total_tax.pack(side='left')
#         self.calculate_button.pack(side='left')
#         self.quit_button.pack(side='left')
#         self.top_frame.pack()
#         self.top2_frame.pack()
#         self.middle_frame.pack()
#         self.bottom_frame.pack()
#         self.main_window.mainloop()
#
#     def create_top_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_label1(self):
#         return tkinter.Label(
#             self.top_frame,
#             text='Enter full cost: '
#         )
#
#     def create_entry(self):
#         return tkinter.Entry(
#             self.top_frame,
#             width=10
#         )
#
#     def create_top2_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_label2(self):
#         return tkinter.Label(
#             self.top2_frame,
#             text='Estimated value'
#         )
#
#     def show_value(self):
#         return tkinter.Label(
#             self.top2_frame,
#             textvariable=self.assessment_value
#         )
#
#     def create_middle_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_label3(self):
#         return tkinter.Label(
#             self.middle_frame,
#             text='Property tax:'
#         )
#
#     def show_tax(self):
#         return tkinter.Label(
#             self.middle_frame,
#             textvariable=self.property_tax
#         )
#
#     def create_bottom_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_calculate_button(self):
#         return tkinter.Button(
#             self.bottom_frame,
#             text='Calculate',
#             command=self.calculate
#         )
#
#     def create_quit_button(self):
#         return tkinter.Button(
#             self.bottom_frame,
#             text='Quit',
#             command=self.main_window.destroy
#         )
#
#     def calculate(self):
#         assessed_value = float(self.entry.get()) * 0.60
#         calculated_tax = assessed_value * (0.75 / 100)
#         self.assessment_value.set(str(assessed_value))
#         self.property_tax.set(format(calculated_tax, ",.2f"))
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
#         self.top_frame = self.create_top_frame()
#         self.bottom_frame = self.create_bottom_frame()
#         self.total = 0
#         self.total_message = 0
#         self.cb_var1 = tkinter.IntVar()
#         self.cb_var2 = tkinter.IntVar()
#         self.cb_var3 = tkinter.IntVar()
#         self.cb_var4 = tkinter.IntVar()
#         self.cb_var5 = tkinter.IntVar()
#         self.cb_var6 = tkinter.IntVar()
#         self.cb_var7 = tkinter.IntVar()
#         self.cb_var1.set(0)
#         self.cb_var2.set(0)
#         self.cb_var3.set(0)
#         self.cb_var4.set(0)
#         self.cb_var5.set(0)
#         self.cb_var6.set(0)
#         self.cb_var7.set(0)
#         self.cb1 = self.create_first_checkbutton()
#         self.cb2 = self.create_second_checkbutton()
#         self.cb3 = self.create_third_checkbutton()
#         self.cb4 = self.create_fourth_checkbutton()
#         self.cb5 = self.create_fifth_checkbutton()
#         self.cb6 = self.create_sixth_checkbutton()
#         self.cb7 = self.create_seventh_checkbutton()
#         self.cb1.pack()
#         self.cb2.pack()
#         self.cb3.pack()
#         self.cb4.pack()
#         self.cb5.pack()
#         self.cb6.pack()
#         self.cb7.pack()
#         self.show_button = self.create_show_button()
#         self.quit_button = self.create_quit_button()
#         self.show_button.pack(side='left')
#         self.quit_button.pack(side='left')
#         self.top_frame.pack()
#         self.bottom_frame.pack()
#         self.main_window.mainloop()
#
#     def create_top_frame(self):
#         return tkinter.Frame(
#             self.main_window
#         )
#
#     def create_bottom_frame(self):
#         return tkinter.Frame(
#             self.main_window
#         )
#
#     def create_first_checkbutton(self):
#         return tkinter.Checkbutton(
#             self.top_frame,
#             text='Oil 30',
#             variable=self.cb_var1,
#             onvalue=30,
#             offvalue=0
#         )
#
#     def create_second_checkbutton(self):
#         return tkinter.Checkbutton(
#             self.top_frame,
#             text='Lube job 500',
#             variable=self.cb_var2,
#             onvalue=500,
#             offvalue=0,
#         )
#
#     def create_third_checkbutton(self):
#         return tkinter.Checkbutton(
#             self.top_frame,
#             text='Radiator Flush 350',
#             variable=self.cb_var3,
#             onvalue=350,
#             offvalue=0
#         )
#
#     def create_fourth_checkbutton(self):
#         return tkinter.Checkbutton(
#             self.top_frame,
#             variable=self.cb_var4,
#             text='Transmission Flush 100',
#             onvalue=750,
#             offvalue=0
#         )
#
#     def create_fifth_checkbutton(self):
#         return tkinter.Checkbutton(
#             self.top_frame,
#             variable=self.cb_var5,
#             text='Inspection 150',
#             onvalue=150,
#             offvalue=0
#         )
#
#     def create_sixth_checkbutton(self):
#         return tkinter.Checkbutton(
#             self.top_frame,
#             text='Inspection 1300',
#             variable=self.cb_var6,
#             onvalue=1300,
#             offvalue=0
#         )
#
#     def create_seventh_checkbutton(self):
#         return tkinter.Checkbutton(
#             self.top_frame,
#             text='Muffler Replacement 1500',
#             variable=self.cb_var7,
#             onvalue=1500,
#             offvalue=0
#         )
#
#     def create_quit_button(self):
#         return tkinter.Button(
#             self.bottom_frame,
#             text='Quit',
#             command=self.main_window.destroy
#         )
#
#     def create_show_button(self):
#         return tkinter.Button(
#             self.bottom_frame,
#             text='Show cost',
#             command=self.show_cost
#         )
#
#     def show_cost(self):
#         self.total = (
#             self.cb_var1.get() +
#             self.cb_var2.get() +
#             self.cb_var3.get() +
#             self.cb_var4.get() +
#             self.cb_var5.get() +
#             self.cb_var6.get() +
#             self.cb_var7.get()
#         )
#         self.total_message = str(self.total)
#         tkinter.messagebox.showinfo('Total is:', self.total_message)
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
#         self.top_frame = self.create_top_frame()
#         self.bottom_frame = self.create_bottom_frame()
#         self.middle_frame = self.create_middle_frame()
#         self.radio_var = tkinter.DoubleVar()
#         self.calculated_total = ''
#         self.radio_var.set(1)
#         self.rb1 = self.create_first_radiobutton()
#         self.rb2 = self.create_second_radiobutton()
#         self.rb3 = self.create_third_radiobutton()
#         self.label = self.create_label()
#         self.entry = self.create_entry()
#         self.show_button = self.create_show_button()
#         self.quit_button = self.create_quit_button()
#         self.rb1.pack()
#         self.rb2.pack()
#         self.rb3.pack()
#         self.label.pack()
#         self.entry.pack()
#         self.show_button.pack()
#         self.quit_button.pack()
#         self.top_frame.pack()
#         self.bottom_frame.pack()
#         self.middle_frame.pack()
#         self.main_window.mainloop()
#
#     def create_top_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_bottom_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_middle_frame(self):
#         return tkinter.Frame(self.main_window)
#
#     def create_first_radiobutton(self):
#         return tkinter.Radiobutton(
#             self.top_frame,
#             text='Daily time: 6:00 to 17:59',
#             variable=self.radio_var,
#             value=0.1
#         )
#
#     def create_second_radiobutton(self):
#         return tkinter.Radiobutton(
#             self.top_frame,
#             text='Dinner time: 18:00 to 23:59',
#             variable=self.radio_var,
#             value=0.12
#         )
#
#     def create_third_radiobutton(self):
#         return tkinter.Radiobutton(
#             self.top_frame,
#             text='No pick time: 0:00 to 5:59',
#             variable=self.radio_var,
#             value=0.5
#         )
#
#     def create_label(self):
#         return tkinter.Label(
#             self.middle_frame,
#             text='Enter amount of minutes: '
#         )
#
#     def create_entry(self):
#         return tkinter.Entry(
#             self.middle_frame,
#             width=10
#         )
#
#     def create_show_button(self):
#         return tkinter.Button(
#             self.middle_frame,
#             text='Show cost',
#             command=self.show_cost
#         )
#
#     def create_quit_button(self):
#         return tkinter.Button(
#             self.middle_frame,
#             text='Quit',
#             command=self.main_window.destroy
#         )
#
#     def show_cost(self):
#         self.calculated_total = (
#                 float(self.entry.get()) *
#                 float(self.radio_var.get())
#         )
#
#         tkinter.messagebox.showinfo(
#             'Total cost', str(self.calculated_total)
#         )
#
#
# my_gui = MyGUI()
        
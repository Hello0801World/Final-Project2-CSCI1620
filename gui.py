from tkinter import *
from weather import *

class gui:
    def __init__(self,window):
        self.window = window

        self.frame_top = Frame(self.window)
        self.label_city = Label(self.frame_top, text='City')
        self.text_city = Text(self.frame_top,height=1,width=20)
        self.label_city.pack(padx=5,pady=10, side = LEFT)
        self.text_city.pack(padx=5,pady=10, side = LEFT)
        self.frame_top.pack()

        self.frame_middle = Frame(self.window)
        self.button_weather = Button(self.frame_middle, text = 'See the weather', command = self.button_clicked)
        self.button_weather.pack(padx=5,pady=10, side = LEFT)
        self.frame_middle.pack()

        self.frame_bottom = Frame(self.window)
        self.label_weather= Label(self.frame_bottom, text='')
        self.label_weather.pack(padx=5,pady=10,side=LEFT)
        self.frame_bottom.pack()

    def button_clicked(self):
        city_name = self.text_city.get(1.0, "end")
        city = weather(city_name)
        self.label_weather.config(text = city)
from time import sleep
import threading

from pyautogui import click
from keyboard import add_hotkey
import customtkinter as ctk

class AppLogic:
    def __init__(self, interface):
        self.interface = interface
        self.speed = 0.5
        self.a = False

        t1 = threading.Thread(target=self.clickstop, 
                              daemon=True
                             )
        t1.start()

        add_hotkey('shift+F6', lambda: self.clickstop())

    def setspeed(self):
        try:
            self.speed = float(self.interface.entry.get())
        except:
            pass

    def click(self):
        sleep(5)
        self.a = True
    
        while self.a:
            sleep(self.speed)
            click()

    def clickinit(self):
        t2 = threading.Thread(target=self.click)
        t2.start()

    def clickstop(self):
        self.a = False
    
class AppInterface:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title('AutoClickerKiller')
        self.app.resizable(False, False)
        self.app.geometry('250x350')

        try:
            self.app.iconbitmap('image.ico')
        except:
            pass

        ctk.set_appearance_mode('dark') 

        self.entry = ctk.CTkEntry(self.app, 
                                  placeholder_text='Speed', 
                                  text_color='#000000', 
                                  fg_color='#FFFFFF', 
                                  border_color='#000000'
                                 ) # speed of click
        self.entry.pack(pady=30)

        Obj = AppLogic(self)

        self.button1 = ctk.CTkButton(self.app, 
                                     text='Set Speed',
                                     command=Obj.setspeed, 
                                     fg_color='#020202', 
                                     hover_color='#131212', 
                                     border_width=2, 
                                     border_color='#FFFFFF'
                                    ) # Stop click button
        self.button1.pack()

        self.button2 = ctk.CTkButton(self.app, 
                                     text='Start Click',
                                     command=Obj.clickinit, 
                                     fg_color='#020202', 
                                     hover_color='#131212', 
                                     border_width=2, 
                                     border_color='#FFFFFF' 
                                    ) # Start click button
        self.button2.pack(pady=10)

        self.button3 = ctk.CTkButton(self.app, 
                                     text='Stop - Press Shift+F6', 
                                     command=Obj.clickstop, 
                                     fg_color='#020202', 
                                     hover_color='#131212', 
                                     border_width=2, 
                                     border_color='#FFFFFF'
                                    ) # Stop click button
        self.button3.pack()

        self.app.mainloop()

AppInterface()
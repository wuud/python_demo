from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.creatWidgets()
    def creatWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name=self.nameInput.get()or'world'
        messagebox.showinfo('Message','hello,{}'.format(name))

app=Application()
app.master.title('hello,world')

app.mainloop()

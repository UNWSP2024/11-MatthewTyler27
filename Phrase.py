import tkinter

class phrase:
    def __init__(self):
        self.window = tkinter.Tk()
        label = tkinter.Label(self.window, text= "Life is like a box of chocolates")
        label.pack()
        tkinter.mainloop()

phrase()

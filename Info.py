import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.Showinfo_button = tkinter.Button(self.window, text= "Show Info", command= show_info)
        self.Showinfo_button.pack()

        self.quit_button = tkinter.Button(self.window, text="Quit", command=self.window.quit)
        self.quit_button.pack()
        
        tkinter.mainloop()

name = "Matthew"
address = "123 Main street"


def show_info():
    tkinter.messagebox.showinfo("Info",name + "," + address)
    

MyGUI()

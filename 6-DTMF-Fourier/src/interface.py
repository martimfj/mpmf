import tkinter as tk
import encoderDTMF

class Main():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x400")
        self.window.title("MPMF")
        self.window.configure(background = 'black')
        self.window.resizable(False, False)

        self.window.rowconfigure(0, minsize = 100)
        self.window.rowconfigure(1, minsize = 100)
        self.window.rowconfigure(2, minsize = 100)
        self.window.rowconfigure(3, minsize = 100)

        self.window.columnconfigure(0, minsize = 100)
        self.window.columnconfigure(1, minsize = 100)
        self.window.columnconfigure(2, minsize = 100)

        height = 5
        width = 5

        self.buttonOne = tk.Button(self.window, text = "1", height = height, width = width)
        self.buttonOne.grid(row = 0, column = 0,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone1)

        self.buttonOne = tk.Button(self.window, text = "2", height = height, width = width)
        self.buttonOne.grid(row = 0, column =1,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone2)

        self.buttonOne = tk.Button(self.window, text = "3", height = height, width = width)
        self.buttonOne.grid(row = 0, column = 2,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone3)

        self.buttonOne = tk.Button(self.window, text = "4", height = height, width = width)
        self.buttonOne.grid(row = 1, column = 0,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone4)

        self.buttonOne = tk.Button(self.window, text = "5", height = height, width = width)
        self.buttonOne.grid(row = 1, column = 1,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone5)

        self.buttonOne = tk.Button(self.window, text = "6", height = height, width = width)
        self.buttonOne.grid(row = 1, column = 2,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone6)

        self.buttonOne = tk.Button(self.window, text = "7", height = height, width = width)
        self.buttonOne.grid(row = 2, column = 0,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone7)
        
        self.buttonOne = tk.Button(self.window, text = "8", height = height, width = width)
        self.buttonOne.grid(row = 2, column = 1,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone8)

        self.buttonOne = tk.Button(self.window, text = "9", height = height, width = width)
        self.buttonOne.grid(row = 2, column = 2,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone9)
        
        self.buttonOne = tk.Button(self.window, text = "*", height = height, width = width)
        self.buttonOne.grid(row = 3, column = 0,  sticky="nsew")
        self.buttonOne.configure(command = self.ToneA)

        self.buttonOne = tk.Button(self.window, text = "0", height = height, width = width)
        self.buttonOne.grid(row = 3, column = 1,  sticky="nsew")
        self.buttonOne.configure(command = self.Tone0)

        self.buttonOne = tk.Button(self.window, text = "#", height = height, width = width)
        self.buttonOne.grid(row = 3, column = 2,  sticky="nsew")
        self.buttonOne.configure(command = self.ToneH)
    
    def iniciar(self):
        self.window.mainloop()

    def Tone1(self):
        encoderDTMF.makeTone(1)

    def Tone2(self):
        encoderDTMF.makeTone(2)

    def Tone3(self):
        encoderDTMF.makeTone(3)

    def Tone4(self):
        encoderDTMF.makeTone(3)

    def Tone5(self):
        encoderDTMF.makeTone(4)

    def Tone6(self):
        encoderDTMF.makeTone(6)

    def Tone7(self):
        encoderDTMF.makeTone(7)

    def Tone8(self):
        encoderDTMF.makeTone(8)

    def Tone9(self):
        encoderDTMF.makeTone(9)

    def Tone0(self):
        encoderDTMF.makeTone(0)

    def ToneA(self):
        encoderDTMF.makeTone("A")

    def ToneH(self):
        encoderDTMF.makeTone("H")

app = Main()
app.iniciar()
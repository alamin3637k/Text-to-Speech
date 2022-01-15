from tkinter import END, HORIZONTAL, Label, Scale, Tk, Text, Button
import pyttsx3


class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x500')
        self.window.title("TTS")
    
    def speak(self, text):
        self.engine = pyttsx3.init()
        rate = self.e1.get()
        if rate == 0:
            rate = 120
        self.engine.setProperty("rate", rate)
        self.engine.say(text)
        self.engine.runAndWait()
    
    def b1(self):
        self.text = self.t_box.get(1.0, END)
        self.speak(text=self.text)
    
    def b2(self):
        self.gender = 0
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[self.gender].id)

    def b3(self):
        self.gender = 1
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[self.gender].id)

    def ui(self):
        self.t_box = Text(self.window, width=60, height=20)
        self.t_box.pack()
        b1 = Button(self.window, text="speak", command=self.b1)
        b1.pack()
        l1 = Label(self.window, text="voice speed:")
        l1.pack()
        self.e1 = Scale(self.window, from_=0, to=200, orient=HORIZONTAL)
        self.e1.pack()
        b2 = Button(self.window, text="change voice to male", command=self.b2)
        b2.pack()
        b3 = Button(self.window, text="change voice to female", command=self.b3)
        b3.pack()

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    app = App()
    app.ui()
    app.run()
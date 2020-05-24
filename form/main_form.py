from tkinter import Tk, Canvas
from tkinter.messagebox import askyesno
from fractal import Fractal
from form import ask_int
from threading import Thread


class Form:
    def __init__(self):
        self.main_form = Tk()
        self.main_form.geometry('1000x1000')
        self.main_form.title("Fractal (developed by Duuuda)")
        self.main_form['bg'] = "#555555"
        self.main_form.resizable(width=False, height=False)
        self.__center_screen(self.main_form)
        self.main_form.protocol("WM_DELETE_WINDOW", self.__exit)
        self.canvas = Canvas(self.main_form,
                             width=self.main_form.winfo_width(),
                             height=self.main_form.winfo_height(),
                             bg='#000000')
        self.canvas.pack()
        depth = ask_int('Enter the recursion depth:')
        self.main_form.focus_force()
        thread = Thread(target=Fractal, args=(self.canvas, depth), daemon=True)
        thread.start()
        self.main_form.mainloop()

    @staticmethod
    def __center_screen(form):
        """ Centers the form """
        form.update_idletasks()
        form.geometry(f'+{(form.winfo_screenwidth() - form.winfo_width()) // 2}+{0}')

    @staticmethod
    def __exit():
        answer = askyesno(title='Exit', message='Are you sure you want to go out?')
        if answer:
            raise SystemExit

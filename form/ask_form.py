from tkinter import Tk, Entry, Button, Label, Frame, TOP, LEFT, RIGHT
from tkinter.messagebox import askyesno, showerror


class AskForm:
    def __init__(self, text_request):
        self.item = int()
        self.ask_form = Tk()
        self.ask_form.geometry('210x55')
        self.ask_form.title('Fractal')
        self.ask_form['bg'] = '#444444'
        self.ask_form.resizable(width=False, height=False)
        self.__center_screen(self.ask_form)
        self.ask_form.protocol('WM_DELETE_WINDOW', self.__exit)
        self.frame_1 = Frame(self.ask_form)
        self.frame_1.pack(side=TOP)
        self.label = Label(self.frame_1, bg='#444444', fg='#ffffff', text=text_request)
        self.label.pack(side=LEFT)
        self.text_box = Entry(self.frame_1, width=5)
        self.text_box.pack(side=RIGHT)
        self.text_box.focus_force()
        self.button = Button(self.ask_form, text="Ok", width=10, command=self.__get_value)
        self.button.pack(side=TOP)
        self.text_box.bind('<Return>', self.__get_value)
        self.ask_form.mainloop()

    def __get_value(self, event=None):
        try:
            data = int(self.text_box.get())
            if data < 2:
                raise RangeError()
            self.item = data
            self.ask_form.quit()
        except ValueError:
            showerror(title='ValueError', message='Enter an integer!!!')
            self.text_box.focus_force()
        except RangeError:
            showerror(title='RangeError', message='The number must be greater than "2"!!!')
            self.text_box.focus_force()

    @staticmethod
    def __center_screen(form):
        """ Centers the form """
        form.update_idletasks()
        form.geometry(f'+{(form.winfo_screenwidth() - form.winfo_width()) // 2}+'
                      f'{(form.winfo_screenheight() - form.winfo_height()) // 2}')

    @staticmethod
    def __exit():
        answer = askyesno(title='Exit', message='Are you sure you want to go out?')
        if answer:
            raise SystemExit


class RangeError(Exception):
    pass


def ask_int(text_request):
    form = AskForm(text_request)
    return form.item

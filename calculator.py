from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='#d9eaf7')  # Soft blue background
        master.resizable(False, False)
        
        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#f7f7f7', font=('Arial Bold', 22), textvariable=self.equation).place(x=0, y=0)
        
        # General button style
        # bg= '#ffffff' # White for numbers and basic operators
        operator_bg = '#aed6f1'  # Light blue for operators
        special_bg = '#f5b7b1'  # Light pink for special buttons like '=' and 'C'

        # Parentheses and percentage buttons
        Button(width=11, height=4, text='(', relief='flat', bg='#ffffff', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='#ffffff', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='#ffffff', command=lambda: self.show('%')).place(x=180, y=50)

        # Number buttons
        Button(width=11, height=4, text='1', relief='flat', bg='#ffffff', command=lambda: self.show('1')).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='#ffffff', command=lambda: self.show('2')).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='#ffffff', command=lambda: self.show('3')).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='#ffffff', command=lambda: self.show('4')).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='#ffffff', command=lambda: self.show('5')).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='#ffffff', command=lambda: self.show('6')).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='#ffffff', command=lambda: self.show('7')).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='#ffffff', command=lambda: self.show('8')).place(x=90, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='#ffffff', command=lambda: self.show('9')).place(x=180, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='#ffffff', command=lambda: self.show('0')).place(x=180, y=350)

        # Decimal point button
        Button(width=11, height=4, text='.', relief='flat', bg='#ffffff', command=lambda: self.show('.')).place(x=90, y=350)

        # Operator buttons
        Button(width=11, height=4, text='+', relief='flat', bg=operator_bg, command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg=operator_bg, command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg=operator_bg, command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', relief='flat', bg=operator_bg, command=lambda: self.show('*')).place(x=270, y=125)

        # Special buttons
        Button(width=11, height=4, text='=', relief='flat', bg=special_bg, command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', bg=special_bg, command=self.clear).place(x=0, y=350)

        # Delete button
        Button(width=11, height=4, text='DEL', relief='flat', bg='#ffcccb', command=self.delete).place(x=90, y=400)  # Positioned below 'C'

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

    def delete(self):
        # Remove the last character from the input
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

root = Tk()
calculator = Calculator(root)
root.mainloop()

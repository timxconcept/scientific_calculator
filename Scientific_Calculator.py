from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure (background='gray4')
root.resizable(width = False, height = False)
root.geometry("480x568+0+0")

calc = Frame(root, bg="gray4")
calc.grid()

class Calc():
    def _init_(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter (self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str (num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
            self.display(self.current)
    
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
        
addad_value = Calc()
txtDisplay = Entry(calc, font = ('arial',20,'bold'), bg="snow", bd=False, width=32, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad ="789456123"
i = 0   
btn = []
for j in range (2,5):
    for k in range (3):
        btn.append(Button(calc, width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bg="gray4", bd =1, text =numberpad[i]))
        btn[i].grid(row = j, column = k, pady =1)
        btn[i] ["command"] = lambda x = numberpad [i]: added_value.numberEnter(X)
        i +=1

# standard Calculator
btnClear = Button(calc, text=chr(67), width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=1, column=0, pady=1)
btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=1, column=1, pady=1)
btnSq = Button(calc, text="√", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="+", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=1, column=3, pady=1)
btnSub = Button(calc, text="+", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=1, column=3, pady=1)
btnMult = Button(calc, text="-", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=2, column=3, pady=1)
btnDiv = Button(calc, text="*", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=3, column=3, pady=1)
btnDiv = Button(calc, text="÷", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=4, column=3, pady=1)

btnZero = Button(calc, text="0", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=5, column=0, pady=1)
btnDot = Button(calc, text=".", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=5, column=1, pady=1)
btnPM = Button(calc, text="±", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=5, column=2, pady=1)
btnEquals = Button(calc, text="=", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=5, column=3, pady=1)

# Scientific Calculator (1)
btnPi = Button(calc, text="π", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=1, column=4, pady=1)
btnCos = Button(calc, text="cos", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=1, column=5, pady=1)
btntan = Button(calc, text="tan", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=1, column=6, pady=1)
btnsin = Button(calc, text="sin", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=1, column=7, pady=1)

# Scientific Calculator (2)
btn2Pi = Button(calc, text="2π", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=2, column=4, pady=1)
btnCosh = Button(calc, text="cosh", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=2, column=5, pady=1)
btntanh = Button(calc, text="tanh", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=2, column=6, pady=1)
btnsinh = Button(calc, text="sinh", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=2, column=7, pady=1)

# Scientific Calculator (3)
btnlog = Button(calc, text="log", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=3, column=4, pady=1)
btnExp = Button(calc, text="exp", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=3, column=5, pady=1)
btnMod = Button(calc, text="mod", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=3, column=6, pady=1)
btnE = Button(calc, text="e", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=3, column=7, pady=1)

# Scientific Calculator (4)
btnlog2 = Button(calc, text="log2", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=4, column=4, pady=1)
btnDeg = Button(calc, text="deg", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=4, column=5, pady=1)
btnAcosh = Button(calc, text="acosh", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=4, column=6, pady=1)
btnAsinh = Button(calc, text="asinh", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=4, column=7, pady=1)

# Scientific Calculator (5)
btnlog10 = Button(calc, text="log10", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=5, column=4, pady=1)
btnCos = Button(calc, text="log1p", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=5, column=5, pady=1)
btnexpml = Button(calc, text="expm1", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=5, column=6, pady=1)
btnlgamma = Button(calc, text="lgamma", width=6, height=2, font = ('arial',20,'bold'), foreground='snow', bd = 1,bg="gray4").grid(row=5, column=7, pady=1)

lblDisplay = Label (calc, text="Scientific Calculator", font=('arial', 30, 'bold'), justify=CENTER)
lblDisplay.grid(row = 0, column = 4, columnspan=4)


# Menu and Function

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def standard():
    root.resizable(width = False, height = False)
    root.geometry("480x568+0+0")

def scientific():
    root.resizable(width = False, height = False)
    root.geometry("944x568+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "standard", command = standard)
filemenu.add_command(label = "Scientific", command = scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")


helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label = "View Menu")

root.configure(menu=menubar)
root.mainloop()
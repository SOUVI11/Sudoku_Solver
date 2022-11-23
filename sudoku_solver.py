from tkinter import *
from Sudoku_main import solver

win = Tk()
win.title('Sudoku Solver')
win.geometry('324x370')
win['background']='#FFFFFF'
win.iconbitmap('C:\Python Projects\Sudoku\gnome_sudoku.ico')
label = Label(win,text = 'Enter your sudoku pattern').grid(row=0,column=1,columnspan=10)

errlabel = Label(win,text='',fg='red')
errlabel.grid(row=15,column=1,columnspan=10,pady=5)

Solvedlabel = Label(win,text='',fg='red')
Solvedlabel.grid(row=15,column=1,columnspan=10,pady=5)

cells = {}

def validate_number(P):
    out = (P.isdigit() or P=='') and len(P)<2
    return out

reg = win.register(validate_number)

def draw_grid3x3(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(win,width = 5, bg =bgcolor,justify='center',validate='key',validatecommand=(reg,'%P'))
            e.grid(row=row+i+1,column=column+j+1,sticky='nsew',padx=1,pady=1,ipady=5)
            cells[(row+i+1,column+j+1)]=e

def draw_grid9x9():
    color = '#FFFFFF'
    for rowno in range(1,10,3):
        for colno in range(0,9,3):
            draw_grid3x3(rowno,colno,color)
            if color == '#FFFFFF': color = '#76EEC6'
            else: color = "#FFFFFF"

def clear():
    errlabel.configure(text='')
    Solvedlabel.configure(text='')
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,'end')

def value():
    board = []
    errlabel.configure(text='')
    Solvedlabel.configure(text='')
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == '': rows.append(0)
            else: rows.append(int(val))
        board.append(rows)
    updatevalue(board)

def updatevalue(s):
    sol = solver(s)
    if sol != 'no':
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,'end')
                cells[(rows,col)].insert(0,sol[rows-2][col-1])
        Solvedlabel.configure(text='Solved')
    else: errlabel.configure('Invalid Sudoku')

btn = Button(win,command=value,text ='Solve',width = 10).grid(row = 14,column=1,columnspan=5,pady=20)
btn = Button(win,command=clear,text ='Clear',width = 10).grid(row = 14,column=5,columnspan=5,pady=20)

draw_grid9x9()

win.mainloop()
print(cells)
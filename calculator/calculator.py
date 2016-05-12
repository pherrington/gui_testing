from tkinter import *

root = Tk()

# style settings and application info
root.geometry('188x205+150+200')
root.title('Calculator')
root.overrideredirect(1)
root.configure(background='#4D4D4D')
root.option_readfile('optionDB.txt')
# screen
display = StringVar()
display.set('0')
screen = Label(root, background='#101010', foreground='#D6D6D6', borderwidth=18, relief='sunken', width=16, height=1,
               textvariable=display, anchor='e')
screen.grid(row=0, column=0, columnspan=4, padx=4, pady=4)
# buttons (use style from optionDB.txt
Button(root, text='C').grid(row=1, column=0, sticky='we')
Button(root, text='/').grid(row=1, column=1, sticky='we')
Button(root, text='*').grid(row=1, column=2, sticky='we')
Button(root, text='-').grid(row=1, column=3, sticky='we')
for num in range(1, 10, 1):
    row = (num - 1) // 3 + 2
    col = (num - 1) % 3
    Button(root, text=str(num)).grid(row=row, column=col, sticky='we')
Button(root, text='+').grid(row=2, rowspan=2, column=3, sticky='nswe')
Button(root, text='Enter').grid(row=4, rowspan=2, column=3, sticky='nswe')
Button(root, text='0').grid(row=5, column=0, columnspan=2, sticky='we')
Button(root, text='.').grid(row=5, column=2, sticky='we')
# runs the main program loop
root.mainloop()

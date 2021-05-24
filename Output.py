from tkinter import *
import time
import WindowController as wc

'''root = Tk()
root.attributes("-topmost",True)
root.overrideredirect(1)
root.title("Карты в руке")
root.geometry("150x30+90+850")
label1 = Label(text='', fg="#eee", bg="#333",font ='Arial 18')
label1.pack()'''

def createRoots(count):
    for i in range(count):
        root.append(Tk())
        root[i].attributes("-topmost",True)
        root[i].overrideredirect(1)
        if i > 1:
            root[i].geometry("230x60+{0}+910".format(575*(i-2)+1935))
        else:
            root[i].geometry("230x60+{0}+910".format(575*(i+1)+15))
        root[i].config(bg="green")

        labels.append(Label(root[i],text='',anchor = 'nw', fg="#eee", bg="green",font ='Arial 17'))


def printCardsOnScreen(_text,i):
    
    #labels.append(Label(text=_text, fg="#eee", bg="#333",font ='Arial 18'))
    labels[i].config(text = _text)
    labels[i].pack()
    root[i].after(10, root[i].quit)
    root[i].mainloop()
    #root.destroy()
    
root = []
labels = []
count = wc.checkingCountWindows()
createRoots(3)

for i in range(3):
    f = open('TKoutput'+str(i)+'.txt', 'w')
    f.write('Нажмите F10\nдля запуска')
    f.close()        

while True:
    for i in range(3):
        f = open('TKoutput'+str(i)+'.txt', 'r')
        data = f.read()
        printCardsOnScreen(data,i)
        f.close()

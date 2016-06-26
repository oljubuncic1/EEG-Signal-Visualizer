import EEGSignalReader
import Tkinter as tk
import tkFont

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


def showButClick():
    x,y = EEGSignalReader.signalParser(options.index(chosenOption.get()))

    #plotting and embedding the graph
    plt.clf()
    plt.gcf().subplots_adjust(bottom=0.2)
    axes = plt.gca()
    axes.set_xlim([0, 20])
    axes.set_ylim([-100,100])

    plt.xlabel('time(s)')
    plt.ylabel(chosenOption.get() + '(uV)')

    if(chosenOption.get() == 'Eye state'):
        axes.set_ylim([-0.5, 1.5])
        axes.set_xlim([0, 120])
        plt.ylabel(chosenOption.get())

    plt.plot(x,y)
    plt.gcf().canvas.draw()
    toolbar.update()

#main

# root windows settings
root = tk.Tk()
root.geometry('900x650')
root.resizable(width=False, height=False)
root.title('EEG Signal Visualizer')
root.iconbitmap('brain_icon.ico')

#logo image settings
canvas = tk.Canvas(root)
canvas.place(relx=0.05, rely=0.05, relheight=0.4, relwidth=0.4)
logo = tk.PhotoImage(file="logo1.gif")
image = canvas.create_image(100, 100, image=logo)

#control frame settings
ctrlFrame = tk.Frame(root, bg='#91CFE3')
ctrlFrame.place(relx=0.35, rely=0.1, relheight=0.21, relwidth=0.6)


#electrodes combobox settings
myFont = tkFont.Font(family='Roboto', size=12)
text = tk.StringVar()
text.set('Choose the channel: ')
label = tk.Label(ctrlFrame, textvariable=text, font=myFont, bg='#91CFE3')
label.place(relx=0.2, rely=0.22)

chosenOption = tk.StringVar()
chosenOption.set('AF3')  # initial value - 1st electrode
options = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4', 'Eye state']
lb = tk.OptionMenu(ctrlFrame, chosenOption, *options)
lb.place(relx=0.55, rely=0.2, relwidth=0.2)

#show signal button settings
showBut = tk.Button(ctrlFrame, text='Show the signal', font=myFont, command=showButClick)
showBut.place(relx=0.2, rely=0.6, relwidth=0.55)


#signal graph settings
f = plt.figure()
graphCanvas = FigureCanvasTkAgg(f, root)
graphCanvas.get_tk_widget().place(relx=0.09, rely=0.45, relheight=0.45, relwidth=0.855)
toolbar = NavigationToolbar2TkAgg(graphCanvas, root)
graphCanvas.show()



root.mainloop()

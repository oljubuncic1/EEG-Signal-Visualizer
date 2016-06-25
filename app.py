import EEGSignalReader
import Tkinter as tk

#main

# root windows settings
root = tk.Tk()
root.geometry('700x500')
root.resizable(width=False, height=False)
root.title('EEG Signal Visualizer')
root.iconbitmap('brain_icon.ico')

#logo image settings
canvas = tk.Canvas(root)
canvas.place(relx=0.05, rely=0.05, relheight=0.4, relwidth=0.4)
logo = tk.PhotoImage(file="logo1.gif")
image = canvas.create_image(100, 100, image=logo)

#control frame settings
ctrlFrame = tk.Frame(root, bg="green")
ctrlFrame.place(relx=0.3, rely=0.05, relheight=0.35, relwidth=0.65)


#electrodes combobox settings
text = tk.StringVar()
text.set('Choose the signal: ')
label = tk.Label(ctrlFrame, textvariable=text)
label.place(relx=0.15, rely=0.2)

options = tk.StringVar()
options.set('')
lb = tk.OptionMenu(ctrlFrame, "", 'opt1', 'opt2', 'opt3')
lb.place(relx=0.45, rely=0.2)






root.mainloop()

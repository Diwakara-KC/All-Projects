from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=( ("All files","*.*"),("Text files","*.txt*"),)
                                          )

    label_file_explorer.configure(text="File Opened: " + filename)
    imagee = ImageTk.PhotoImage(Image.open(filename, 'r'))
    panel = Label(window, image=imagee)
    panel.pack(side="bottom", fill="both", expand="yes")
    panel.img_ref = imagee

window = Tk()


window.title('Photo Editor created by Diwakara KC')

window.geometry('1270x650+0+0')

window.config(background="pink")

label_file_explorer = Label(window,
                            text="Choose Image",
                            width=100, height=4,
                            fg="blue",font=('arial', 13, 'bold'))


button_explore = Button(window,
                        text="Browse Files",font=('arial', 18, 'bold'),
                        command=browseFiles)

button_exit = Button(window,
                     text="Exit",font=('arial', 16, 'bold'),
                     command=exit)


label_file_explorer.grid(columnspan=5,row=5,column=2)
label_file_explorer.place(relx=0.5, rely=0.5, anchor='s')


button_explore.grid(columnspan=5,row=20,column=2)
button_explore.place(relx=0.51 ,rely=0.55, anchor='center')

button_exit.grid(columnspan=10,row=30,column=4)
button_exit.place(relx=0.49, rely=0.63)



window.mainloop()

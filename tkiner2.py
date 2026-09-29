from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title('My Pokemon')
window.geometry('400x420')
title = Label(window, text='My Photo Album', fg='white', bg='purple', width=40)
title.pack(pady=10)
img_file = Image.open('img.png')
img_file = img_file.resize((300, 180))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=5)
def show_message():
    messagebox.showinfo('Great!', 'You Clicked The Photo')
msg_btn = Button(window, text='Click to React', bg='blue', fg='white', command=show_message) 
msg_btn.pack(pady=5)   
def show_details():
    top = Toplevel()
    top.title('Pikachu Details')
    top.geometry('200x120')
    info = Label(top, text='A Electric Pokemon')
    info.pack(pady=10)
    place = Label(top, text='Pokedex no 25')
    place.pack()
    top.mainloop()
details_btn = Button(window, text='See detail', bg='green',fg='white', command=show_details) 
details_btn.pack(pady=5)   
window.mainloop()
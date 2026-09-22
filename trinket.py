from tkinter import *
window = Tk()
window.title('My Profile card')
window.geometry('400x380')
def display():
     name = name_entry.get()
     hobby = hobby_entry.get()
     about= about_text.get("1.0",END)
     card = "My Profile Card\n\n"
     card+= "Name: " + name + "\n"
     card+= "Hobby: " + hobby + "\n"
     card+= "About Me!: " + about
     result_label.config(text=card)



title = Label(window, text='My Profile Card', fg='white',bg='purple',width=40)
title.grid(row=0, column=0, columnspan=2,padx=10,pady=10)
#pt2
name_label = Label(window, text='Name:', fg='black', bg='white')
name_label.grid(row=1, column=0, padx=10,pady=5)
name_entry = Entry(window, fg='blue', bg='lightyellow', width=25)
name_entry.grid(row=1, column=1, padx=10, pady=5)
hobby_label = Label(window, text='Hobby:', fg='black', bg='white')
hobby_label.grid(row=2, column=0, padx=10,pady=5)
hobby_entry = Entry(window, fg='blue', bg='lightyellow', width=25)
hobby_entry.grid(row=2, column=1, padx=10, pady=5)
about_frame = Frame(window, relief=RAISED, borderwidth=3)
about_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
about_label = Label(about_frame, text='About Me:')
about_label.pack()
about_text = Text(about_frame, fg='green', bg='lightyellow', width=40, height=4)
about_text.pack()
submit = Button(window, text='Show my card', bg='purple', fg='white', width=20,command=display)
submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
result_label = Label( window, text='', bg='white', fg='black', justify=LEFT ) 
result_label.grid( row=5, column=0, columnspan=2, padx=10, pady=10 )
window.mainloop()
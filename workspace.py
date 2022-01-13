from tkinter import*
from tkinter import font

base = Tk()
base.title("Inscription")
base.geometry("600x450")
base.resizable(False,False)
base.configure(bg="#2D64F5")

Label(base, text="Formulaire d'inscription",bg="#2D64F5" ,font="Roboto 25").pack(pady=50)
Label(base,text="Nom", font= "arial 20", bg="#2D64F5" ).place(x=50, y=150)
Label(base, text="Prenom", font="arial 20", bg="#2D64F5" ).place(x=50, y=200)
Label(base, text="Email", font="arial 20" , bg="#2D64F5").place(x=50, y=250)
Label(base, text="Telephone", font="arial 20", bg="#2D64F5").place(x=50, y=300)

nomValue = StringVar()
prenomValue = StringVar()
emailValue = StringVar()
telephoneValue = StringVar()

nomEntry = Entry(base, textvariable=nomValue ,width=30, bd=2, font="arial 20")
prenomEntry = Entry(base, textvariable=prenomValue ,width=30, bd=2, font="arial 20")
emailEntry = Entry(base, textvariable=emailValue ,width=30, bd=2, font="arial 20")
telephoneEntry = Entry(base, textvariable=telephoneValue ,width=30, bd=2, font="arial 20")

def show_entry():
    f = open("name.json", "a")
    f.write("Nom: %s\n Prenom: %s\n Email: %s\n Telephone: %s" % (nomEntry.get(), prenomEntry.get(), emailEntry.get(), telephoneEntry.get()))
    nomEntry.delete(0,END)
    prenomEntry.delete(0,END)
    emailEntry.delete(0,END)
    telephoneEntry.delete(0,END)

nomEntry.config(relief=SUNKEN)
prenomEntry.config(relief=SUNKEN)
emailEntry.config(relief=SUNKEN)
telephoneEntry.config(relief=SUNKEN)

nomEntry.place(x=150, y=150)
prenomEntry.place(x=150, y=200)
emailEntry.place(x=150 , y=250)
telephoneEntry.place(x=150, y=300)

Button(base, text="Submit", command=show_entry, bg="teal", font = "arial 20", width =11, height=2).place(x=200, y=360)

base.mainloop()
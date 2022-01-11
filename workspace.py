from tkinter import*
from tkinter import font

base = Tk()
base.title("Inscription")
base.geometry("600x450")
base.resizable(False,False)
base.configure(bg="#2D64F5")

Label(base, text="Formulaire d'inscription",bg="#2D64F5" ,font="Roboto 25").pack(pady=50)
Label(text="Nom", font= "arial 20", bg="#2D64F5" ).place(x=50, y=150)
Label(text="Prenom", font="arial 20", bg="#2D64F5" ).place(x=50, y=200)
Label(text="Email", font="arial 20" , bg="#2D64F5").place(x=50, y=250)
Label(text="Telephone", font="arial 20", bg="#2D64F5").place(x=50, y=300)

nomValue = StringVar()
prenomValue = StringVar()
emailValue = StringVar()
telephoneValue = StringVar()

nomEntry = Entry(base, textvariable=nomValue ,width=30, bd=2, font="arial 20")
prenomEntry = Entry(base, textvariable=prenomValue ,width=30, bd=2, font="arial 20")
emailEntry = Entry(base, textvariable=emailValue ,width=30, bd=2, font="arial 20")
telephoneEntry = Entry(base, textvariable=telephoneValue ,width=30, bd=2, font="arial 20")

nomEntry.place(x=150, y=150)
prenomEntry.place(x=150, y=200)
emailEntry.place(x=150 , y=250)
telephoneEntry.place(x=150, y=300)

Button(text="Submit",bg="teal", font = "arial 20", width =11, height=2).place(x=200, y=360)





base.mainloop()
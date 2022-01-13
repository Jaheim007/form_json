from ast import Return
from lib2to3.pgen2.grammar import Grammar
from tkinter import*
from tkinter import font
import json

#Creating the Size of the Form and title
base = Tk()
base.title("Inscription")
base.geometry("600x550")
base.resizable(False,False)
base.configure(bg="steel blue")

#Creating the Label First Name, Last Name, Email and Contact
Label(base, text= "Formulaire d'inscription",bg="steel blue" ,font="Roboto 25", fg="white").pack(pady=50)
Label(base,text= "Nom", font= "arial 20", bg="steel blue", fg="white" ).place(x=45, y=150)
Label(base, text="Prenom", font="arial 20", bg="steel blue", fg="white" ).place(x=45, y=200)
Label(base, text="Email", font="arial 20" , bg="steel blue", fg="white").place(x=45, y=250)
Label(base, text="Telephone", font="arial 20", bg="steel blue", fg="white").place(x=45, y=300)

#Stating that the Values are all string
nomValue = StringVar()
prenomValue = StringVar()
emailValue = StringVar()
telephoneValue = StringVar()

#Creating the entry of the Form
nomEntry = Entry(base, textvariable=nomValue ,width=30, bd=2, font="arial 20")
prenomEntry = Entry(base, textvariable=prenomValue ,width=30, bd=2, font="arial 20")
emailEntry = Entry(base, textvariable=emailValue ,width=30, bd=2, font="arial 20")
telephoneEntry = Entry(base, textvariable=telephoneValue ,width=30, bd=2, font="arial 20")

#Placing the entry of the Form
nomEntry.place(x=150, y=150)
prenomEntry.place(x=150, y=200)
emailEntry.place(x=150 , y=250)
telephoneEntry.place(x=150, y=300)

#Creating the JSON file to store all the information
def show_entry():
    f = open("name.json", "a")
    f.write("Nom: %s\nPrenom: %s\nEmail: %s\nTelephone: %s\n" % (nomEntry.get(), prenomEntry.get(), emailEntry.get(), telephoneEntry.get()))
    nomEntry.delete(0,END)
    prenomEntry.delete(0,END)
    emailEntry.delete(0,END)
    telephoneEntry.delete(0,END)
    f.close()

#Creating the button
Button(base ,text="Valider",command=show_entry, fg="black", bg="spring green", font = "arial 20", width =11, height=2).place(x=200, y=360)

base.mainloop()
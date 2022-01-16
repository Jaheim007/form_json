from lib2to3.pgen2.grammar import Grammar
from multiprocessing.dummy import Value
from tkinter import*
from tkinter import font
from tkinter import messagebox
import res

#Creating the Size of the Form and title
base = Tk()
base.title("Page D'Inscrip")
base.geometry("600x550")
base.eval('tk::PlaceWindow . center')
base.resizable(False,False)
base.configure(bg="orange red")

#Creating the Label First Name, Last Name, Email and Contact
Label(base, **res.title).pack(pady=50)
Label(base,text= "Nom", **res.global_style).place(x=45, y=150)
Label(base, text="Prenom", **res.global_style).place(x=45, y=200)
Label(base, text="Email", **res.global_style).place(x=45, y=250)
Label(base, text="Telephone", **res.global_style).place(x=45, y=300)

#Stating that the Values are all string
nomEntry = StringVar()
prenomEntry = StringVar()
emailEntry = StringVar()
telephoneEntry = IntVar()

#Creating the entry of the Form
nomEntry = Entry(base, textvariable=nomEntry ,width=30, bd=2, font="arial 20")
prenomEntry = Entry(base, textvariable=prenomEntry ,width=30, bd=2, font="arial 20")
emailEntry = Entry(base, textvariable=emailEntry ,width=30, bd=2, font="arial 20")
telephoneEntry = Entry(base, textvariable=telephoneEntry ,width=30, bd=2, font="arial 20")

#Placing the entry of the Form
nomEntry.place(x=150, y=150)
prenomEntry.place(x=150, y=200)
emailEntry.place(x=150 , y=250)
telephoneEntry.place(x=150, y=300)

#Creating the JSON file to store all the information
def show_entry():
    f = open("name.json", "a")
    f.write("Nom : %s\nPrenom : %s\nEmail : %s\nTelephone : %s\n" % (nomEntry.get(), prenomEntry.get(), emailEntry.get(), telephoneEntry.get()))
    
    #Creating sereval variables to obtain the input of the user 
    nom = nomEntry.get()
    prenom = prenomEntry.get()
    email = emailEntry.get()
    telephone = telephoneEntry.get()
    
    #Creating the Condition of the message box which is empty
    if nom == "" or prenom =="" or email =="" or telephone =="":
        messagebox.showerror("Error", "Veuillez saisir vos informations.")
    
    #Deleteing the Entry
    nomEntry.delete(0,END)
    prenomEntry.delete(0,END)
    emailEntry.delete(0,END)
    telephoneEntry.delete(0,END)
    f.close()

#Creating the button
Button(base ,text="Valider",command=show_entry, fg="black", bg="spring green", font = "arial 18", width =10, height=2).place(x=250, y=360)

base.mainloop()
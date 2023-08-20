from tkinter import *
from tkinter import ttk
from Groupe_V2 import *
from Stagiare_V2 import *
import re
from tkinter import messagebox

def ajouter():
    if re.search("@",email.get()) :
        reg1 = re.split("@",email.get())
        if len(reg1[0]) > 2 and len(reg1[1]) > 2 :
            if re.search("\.",email.get()) :
                reg2 = re.split("\.",reg1[1])
                if len(reg2[0]) >= 3 and len(reg2[1]) >= 3 :
                    x = Stagiaire(id.get(), nom.get(), email.get(), groupe.get())
                    x.ajouter(x)
                    messagebox.showinfo("Congrats","Stagiare ajouté(e) avec succés")
                else :
                    messagebox.showerror("Email Erreur","Veuiller verifier que la forme de l'email est correct")
            else:
                messagebox.showerror("Email Erreur", "Veuiller verifier que la forme de l'email est correct")
        else:
            messagebox.showerror("Email Erreur", "Veuiller verifier que la forme de l'email est correct")
    else:
        messagebox.showerror("Email Erreur", "Veuiller verifier que la forme de l'email est correct")
def supprimer():
    if messagebox.askyesno("Confirmation","Confirmer la suppresion") :
        x = Stagiaire(id.get(), nom.get(), email.get(), groupe.get())
        x.supprimer(id.get())

def modifier():
    if messagebox.askyesno("Modification des données","Veullez-vous modfier les données?") :
        x = Stagiaire(id.get(), nom.get(), email.get(), groupe.get())
        x.modifier(id.get(), nom.get(), email.get(), groupe.get())
def rechercher():
    x = Stagiaire(id.get(), nom.get(), email.get(), groupe.get())
    ap = x.rechercher(id.get())

    column = ('Id', 'Name', 'Email', 'Groupe')
    Tabel = ttk.Treeview(win, columns=column, show='headings')
    Tabel.place(x = 0 , y = 150)

    for i in column:
        Tabel.heading(i, text=i)

    Tabel.insert("","end",values=ap)
def afficher():
    x = Stagiaire(id.get(), nom.get(), email.get(), groupe.get())

    ap = x.afficher()

    column = ('Id', 'Name', 'Email', 'Groupe')
    Tabel = ttk.Treeview(win, columns=column, show='headings')
    Tabel.place(x=0, y=150)

    for i in column:
        Tabel.heading(i, text=i)

    for j in ap :
        Tabel.insert("", "end", values=j)

def afficher_grp():
    x = Stagiaire(id.get(), nom.get(), email.get(), groupe.get())

    ap = x.afficher_grp(groupe.get())

    column = ('Id', 'Name', 'Email', 'Groupe')
    Tabel = ttk.Treeview(win, columns=column, show='headings')
    Tabel.place(x=0, y=150)

    for i in column:
        Tabel.heading(i, text=i)

    for j in ap:
        Tabel.insert("", "end", values=j)

def ajouter_grp():
    def aj():
        g = Groupe(ngrp.get())
        g.ajouter(g)
        messagebox.showinfo("Congrats","Groupe ajouté avec succés")
        ng.destroy()

    ng = Toplevel(win)
    ng.title("Nouveau Groupe")
    ng.geometry("100x100")

    ngrp = Entry(ng, width=15)
    ngrp.pack()
    btnGrp = Button(ng, command=aj, text="Ajouter", width=12).pack()

def actualiser_grp():
    a = []
    for i in Groupe.affich_gr():
        a.append(i)
    groupe['values'] = a
    groupe.place(x=80, y=80)
    win.after(1000, actualiser_grp)

win = Tk()
win.geometry("1000x1000")
id_L = Label(win,text="Id :").place(x=20,y=20)
name_L= Label(win,text="name:").place(x=20,y=40)
email_L= Label(win,text="email :").place(x=20,y=60)
groupe_L= Label(win,text="Groupe :").place(x=20,y=80)

id = Entry(win)
id.place(x=80,y=20)
nom = Entry(win)
nom.place(x=80,y=40)
email = Entry(win)
email.place(x=80,y=60)

groupe = ttk.Combobox(win, width = 15)

ajouter = Button(win,command=ajouter,text='Ajouter',width=9
                 ,activebackground="#33cc33",activeforeground="white").place(x=250,y =20 )
supprimer = Button(win,command=supprimer,text='Supprimer',width=9
                   ,activebackground="#33cc33",activeforeground="white").place(x=250,y =50 )
modifier = Button(win,command=modifier,text='Modifier',width=9
                  ,activebackground="#33cc33",activeforeground="white").place(x=250,y =80 )
rechercher = Button(win,command=rechercher,text='Rechercher',width=12
                    ,activebackground="#33cc33",activeforeground="white").place(x=330,y =20 )
afficher = Button(win,command=afficher,text='Afficher',width=12
                  ,activebackground="#33cc33",activeforeground="white").place(x=330,y =50 )
afficher_grp = Button(win,command=afficher_grp,text='Afficher Groupe',width=12
                      ,activebackground="#33cc33",activeforeground="white").place(x=330,y =80 )
ajouter_grp = Button(win,command=ajouter_grp,text='Ajouter Groupe',width=12
                     ,activebackground="#33cc33",activeforeground="white").place(x=430,y=20)

actualiser_grp()
win.mainloop()


from tkinter import*
from tkinter import messagebox, simpledialog
import pickle
import random

class App:
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap("playing-cards-with-hearts.ico")
        self.root.title("Kärtchenbox")
    def createWidgets(self):
        self.button_neuekarte = Button(self.root, text="Neue Karte erstellen", width=20, height=10, command=self.rt_new_card)
        self.button_neuekarte.pack(padx=30, pady=30, side="left")
        self.button_kartevergeben = Button(self.root, text="Karte vergeben", width=20, height=10, command=self.karte_vergeben)
        self.button_kartevergeben.pack(padx=30, pady=30, side="left")
        self.button_erledigt = Button(self.root, text="Erledigt", width=20, height=10, command=self.rt_karte_entfernen)
        self.button_erledigt.pack(padx=30, pady=30, side="left")
        self.button_newuser = Button(self.root, text="User erstellen", width=20, height=10, command=self.new_user)
        self.button_newuser.pack(padx=30, pady=30, side="left")
    def rt_new_card(self):
        self.rt_new_card = Tk()
        self.rt_new_card.title("Kärtchenbox")
        self.label1 = Label(self.rt_new_card, text="Menge: ")
        self.entry1 = Entry(self.rt_new_card)
        self.label2 = Label(self.rt_new_card, text="Text: ")
        self.entry2 = Entry(self.rt_new_card)
        self.button = Button(self.rt_new_card, text="Eingabe", command=self.new_card)
        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.button.pack()
    def new_card(self):
        try:
            f = open("karten.dat", "rb")
            karten = pickle.load(f)
        except:
            karten = []
        f.close()
        try:
            f = open("karten.dat", "wb")
            menge = int(self.entry1.get())
            text = self.entry2.get()
            for i in range(0, menge):
                karten.append(text)
            pickle.dump(karten, f)
            f.close()
        except:
            messagebox.showerror("Fehler","Möglicherweise stimmen ihre Eingaben nicht.")
        self.rt_new_card.destroy()
    def new_user(self):
        try:
            f = open("user.dat", "rb")
            user = pickle.load(f)
        except:
            user = {}
        f.close()
        name = simpledialog.askstring("Username", "Wie heißt der User?")
        f = open("user.dat", "wb")
        user[name] = []
        pickle.dump(user, f)
        f.close()
    def karte_vergeben(self):
        try:
            f = open("user.dat", "rb")
            users = pickle.load(f)
        except:
            messagebox.showerror("Fehler","Noch keine User zum vergeben erstellt")
            return
        f.close()
        user = simpledialog.askstring(" ", "Wie heißt der User?")
        if not self.entfuser in users:
            messagebox.showerror("Fehler", "User nicht gefunden")
            return
        try:
            f = open("karten.dat", "rb")
            karten = pickle.load(f)
        except:
            messagebox.showerror("Fehler", "Noch keine Karten erstellt")
            return
        f.close()
        f = open("karten.dat", "wb")
        karte = random.choice(karten)
        users[user].append(karte)
        karten.remove(karte)
        pickle.dump(karten, f)
        f.close()
        f = open("user.dat", "wb")
        pickle.dump(users, f)
        f.close()
    def rt_karte_entfernen(self):
        try:
            f = open("user.dat", "rb")
            users = pickle.load(f)
        except:
            messagebox.showerror("Fehler", "Sie haben noch keine User erstellt.")
            return
        f.close()
        self.entfuser = simpledialog.askstring(" ", "Name des Users:")
        if not self.entfuser in users:
            messagebox.showerror("Fehler", "User nicht gefunden")
            return
        if users[self.entfuser] == []:
            messagebox.showinfo("Herzlichen Glückwunsch", "Alle Aufgaben abgearbeitet")
            return
        self.rt_karte_entfernen = Tk()
        self.rt_karte_entfernen.title("Bitte Karte wählen:")
        self.listbox = Listbox(self.rt_karte_entfernen)
        for i in users[self.entfuser]:
            self.listbox.insert("end", i)
        self.listbox.pack()
        self.button = Button(self.rt_karte_entfernen, text="Eingabe", command=self.karte_entfernen)
        self.button.pack()
    def karte_entfernen(self):
        f = open("user.dat", "rb")
        users = pickle.load(f)
        f.close()
        f = open("karten.dat", "rb")
        karten = pickle.load(f)
        f.close()
        users[self.entfuser].remove(self.listbox.get("active"))
        karten.append(self.listbox.get("active"))
        f = open("user.dat", "wb")
        pickle.dump(users, f)
        f.close()
        f = open("karten.dat", "wb")
        pickle.dump(karten, f)
        f.close()
        self.rt_karte_entfernen.destroy()
a = App()
a.createWidgets()
a.root.mainloop()

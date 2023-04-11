import tkinter as tk

class Fenetre:
    def __init__(self, titre="Accordeur guitare", largeur=400, hauteur=300):
        self.fenetre = tk.Tk()
        self.fenetre.title(titre)
        self.fenetre.geometry("{}x{}".format(largeur, hauteur))
        self.note = tk.Label(self.fenetre, text="", font=('Arial', 50))
        self.note.pack(padx=100, pady=275)
        self.comparaison = tk.Label(self.fenetre, text="", font=('Arial', 50))
        self.comparaison.pack()
        
    def run(self):
        self.fenetre.mainloop()
        
        
win = Fenetre('Accordeur', 1920, 1080)
win.run()

import tkinter as tk
import time

class Fenetre:
    def __init__(self, titre, geometrie, fenetre=None, note=None, comparaison=None):
        self.geometrie = geometrie
        self.titre = titre
        self.fenetre = tk.Tk()
        self.note = tk.Label(fenetre, text="", font=('Arial', 50))
        self.comparaison = tk.Label(fenetre, text="", font=('Arial', 50))
        self.note.pack(padx=100, pady=275)
        self.comparaison.pack()
        
    def afficher(self):
        self.fenetre.mainloop()

    def modifier_note(self, nouv_note):
        self.note.config(text=nouv_note)
        
win = Fenetre('Accordeur', '1920x1080')
win.afficher()
time.sleep(3)
win.modifier_note('A')

"""
def creer_fenetre():
    fenetre = tk.Tk()
    fenetre.geometry("1920x1080")
    fenetre.title("Accordeur Guitare")
    
    note = tk.Label(fenetre, text="pd", font=('Arial', 50))
    global note
    note.pack(padx=100, pady=275)

    comparaison = tk.Label(fenetre, text="oui", font=('Arial', 50))
    global comparaison
    comparaison.pack()
    
    fenetre.mainloop()
    
def modifier_note(nouv_note):
    note.config(text=nouv_note)
    
def modifier_comparaison(nouv_comparaison):
    comparaison.config(text=nouv_comparaison)"""

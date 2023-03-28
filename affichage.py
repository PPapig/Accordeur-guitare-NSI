import tkinter as tk

def créer_fenetre():
    fenetre = tk.Tk()
    fenetre.geometry("640x480")
    fenetre.title("Accordeur Guitare")
    
    note = tk.Label(fenetre, text="oui bonjour", font_size=14)
    note.pack()

    comparaison = tk.Label(fenetre, text="non au revoir")
    comparaison.pack()
    
    fenetre.mainloop()

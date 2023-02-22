from numpy import argmax

def determine_note(data):
    """
    Prend un tableau numpy en argument et renvoie la note jouée
    """
    # Recherche de la fréquence fondamentale
    frequence = argmax(data)
    print(f"Frequence: {frequence} Hz")

    # Recherche de la note correspondante dans la table de correspondance
    notes = {
        "E4": 329,
        "B3": 246,
        "G3": 196,
        "D3": 146,
        "A2": 110,
        "E2": 82,
    }
    for note, f in notes.items():
        if frequence >= f - 5 and frequence <= f + 5:
            return note
        elif frequence >= f - 10 and frequence <= f - 5:
            return "Trop grave"
        elif frequence <= f + 10 and frequence >= f + 5:
            return "Trop aigu"
    return "Note non reconnue"

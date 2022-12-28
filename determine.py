from numpy import argmax

def determine_note(data):
    # Recherche de la fréquence fondamentale
    frequency = argmax(data)
    print(f"Frequency: {frequency} Hz")

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
        if frequency > f - 10 and frequency < f + 10:
            return note
    return "Note non reconnue"
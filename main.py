import pyaudio
import numpy as np

def determine_note(data):
    # Recherche de la fréquence fondamentale
    frequency = np.argmax(data)
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

# Ouvre un flux d'enregistrement avec Pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Enregistre le son pendant 1 seconde
data = stream.read(44100)

# Ferme le flux d'enregistrement
stream.stop_stream()
stream.close()
p.terminate()

# Transforme les données audio en un tableau Numpy
data = np.frombuffer(data, dtype=np.int16)

# Calcule la transformée de Fourier du signal
sp = np.fft.rfft(data)

# Déterminne la note jouée
print(determine_note(sp))

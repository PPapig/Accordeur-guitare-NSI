from pyaudio import PyAudio, paInt16
from numpy import frombuffer, int16, fft

def donnees():
    """
    écoute le micro et convertit les données en tableau numpy
    """
    # Ouvre un flux d'enregistrement avec Pyaudio
    flux = PyAudio()
    stream = flux.open(format=paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    # Définir le seuil de volume
    seuil = 2500

    # Enregistre le son uniquement lorsqu'il dépasse le seuil de volume
    while True:
        donnee = stream.read(1024)
        tab = frombuffer(donnee, dtype=int16)
        volume = abs(tab).mean()
        if volume > seuil:
            break

    # Enregistre le son et calcule la transformée de Fourier du signal
    donnee = stream.read(44100)
    tab = frombuffer(donnee, dtype=int16)
    fourier = fft.rfft(tab)

    # Ferme le flux d'enregistrement
    stream.stop_stream()
    stream.close()
    flux.terminate()

    # Retourne la transformée de Fourier du signal
    return fourier

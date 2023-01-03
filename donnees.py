from pyaudio import PyAudio, paInt16
from numpy import frombuffer, int16, fft

def donnees():
    """
    écoute le mmicro et convertit les données en tableau numpy
    """
    # Ouvre un flux d'enregistrement avec Pyaudio
    flux = PyAudio()
    stream = flux.open(format=paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    # Enregistre le son pendant 1 seconde
    donnee = stream.read(44100)

    # Ferme le flux d'enregistrement
    stream.stop_stream()
    stream.close()
    flux.terminate()

    # Transforme les données audio en un tableau Numpy
    donnee = frombuffer(data, dtype=int16)

    # Calcule la transformée de Fourier du signal
    fourier = fft.rfft(data)

    return fourier

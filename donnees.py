from pyaudio import PyAudio, paInt16
from numpy import frombuffer, int16, fft

def donnees():
    # Ouvre un flux d'enregistrement avec Pyaudio
    p = PyAudio()
    stream = p.open(format=paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    # Enregistre le son pendant 1 seconde
    data = stream.read(44100)

    # Ferme le flux d'enregistrement
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Transforme les données audio en un tableau Numpy
    data = frombuffer(data, dtype=int16)

    # Calcule la transformée de Fourier du signal
    sp = fft.rfft(data)

    return sp
import ctypes
from ctypes import CFUNCTYPE, c_int
import os

# Carica la libreria compilata

lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "lib.so"))


# Definisci la funzione di callback in Python
@CFUNCTYPE(None, c_int)
def stampa_primo(primo):
    print(f"Numero primo: {primo}")


# Definisci la funzione calcola_numeri_primi con il corretto tipo di ritorno e argomenti
lib.prime_numbers_callback.argtypes = [c_int, CFUNCTYPE(None, c_int)]

# Chiama la funzione calcola_numeri_primi con la callback
limite = 10000  # Calcola i numeri primi fino a 100
lib.prime_numbers_callback(limite, stampa_primo)

from hangman_fce import *
import random

def main():
    hadana_slova = ["jablko", "pomeranc", "mandarinka"]
    hrac = pridej_hrace()
    hadane_slovo = vyber_hadane_slovo(hadana_slova)
    print(schovej_slovo(hadane_slovo), len(hadane_slovo))
    postup, zbyvajici_tahy = schovej_slovo(hadane_slovo)

    while zbyvajici_tahy:
        vypis_stav_hry(hrac, postup, zbyvajici_tahy)
        zbyvajici_tahy = hraci_kolo(hadane_slovo, postup, zbyvajici_tahy)
        konecna_kontrola = posouzeni_stavu(postup, hrac, zbyvajici_tahy,hadane_slovo)

if __name__ == "__main__":
    main()
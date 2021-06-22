from prace_se_stringem import *
from prace_s_listem import *
import sys

def main():
    print("Zaciname ")
    data_typ, volba, *zbytek = sys.argv[1:] # zadávání argumentů z přík. řádky, [1:] je kvůli názvu souboru, to je první argument a ten nechceme
    if data_typ == "string":
        if volba == "split":
            necistota = zbytek[0]
            print(ocisteni_od_punkci(slovo, necistota))
        elif volba == "startwith":
            print(zacina_na_urcity_symbol(slovo, start))
        else:
            print("Špatná volba.")
    elif data_typ == "list":
        print("Pracuji s listem.")
        if volba == "delka_listu":
            print(delka_listu(zbytek))

if __name__ == "__main__": # jestli tento modul pouštím přímo z tohoto modulu
    main()
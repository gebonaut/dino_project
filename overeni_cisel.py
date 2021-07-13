from typing import List



def nacti_udaje(nazev_souboru : str) -> List[str]:
  with open(nazev_souboru, "r") as soubor:
    return soubor.readlines()

def ostripuj_cisla(list_dat_neupraveny : List[str]) -> List[str]:
  return [naformatuj_data(radek.strip()) for radek in list_dat_neupraveny ]

def naformatuj_data(udaj : str) -> str:
  return f'ID: {udaj}, TYPE: {type(udaj)}'

def zkontroluj_typ_udaje(upravena_data : List[str]) -> None:
  overene_udaje = []
  while upravena_data:
    overeni_data_typu(overene_udaje, upravena_data)

def overeni_data_typu(uloziste : list, upravena : List[str]) -> None:
  try:
    cislo = upravena.pop().split()[1][:-1]
    prevedena_hodnota = int(cislo)
  except ValueError as e:
    if len(cislo) > 0:
      print(f'Nelze konvertovat, proto vyvolavam -> {e.__class__.__name__}')
  else:
    print(f'Lze konvertovat -> {prevedena_hodnota}')
    uloziste.append(prevedena_hodnota)
  finally:
    if len(cislo) > 0:
      print('-'*50)

def hlavni():
  #Nacteni udaju:
  nactena_cisla = nacti_udaje("numbers.txt")
  #ostripovaní
  ostripovana_data = ostripuj_cisla(nactena_cisla)
  zkontroluj_typ_udaje(ostripovana_data)

hlavni()



import string

def ocisteni_od_punkci(slovo : str, necistota: str, punction = False) -> str:
    """Vezme slovo a zbaví ho nečistot"""
    if punction and not necistota:
        return slovo.strip(string.punctuation)
    else:
        return slovo.strip(necistota)

def zacina_na_urcity_symbol(slovo: str, start: str) -> bool:
    """Vezme slovo a zjistí na co začíná"""
    return True if slovo.startswith(start) else False
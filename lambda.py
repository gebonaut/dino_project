# bezejmenná funkce / annonymous function

def input_list_of_text(l_of_text):
    if isinstance(l_of_text, list):
        for letter in l_of_text:
            if letter in "aeiouy":
                l_of_text.remove(letter)
        return l_of_text
    else:
        text_to_list = lambda text: list(text)
        l_of_text = text_to_list(l_of_text)
        for letter in l_of_text:
            if letter in "aeiouy":
                l_of_text.remove(letter)
        return l_of_text

text = "oshefoashfpoasejfsef"

print(input_list_of_text(text))

# toto je stejné jako funkce níže
text_upper = lambda text: text.upper()

# jako toto, protože pokud něco píšu, nemám možnost psát funkce v kodu, proto existuje lambda, kde si můžu uprostřed kodu definovat funkci
def text_upper2(text): return text.upper()

print(text_upper("awdawdawdawdawdawd"))
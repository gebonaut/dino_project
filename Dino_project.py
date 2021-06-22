# import knihoven
from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *

# colab https://colab.research.google.com/drive/1MnXoNYF0MXlrfxK6_ftPE6Vr1ej1Uno9?usp=sharing#scrollTo=pyVUsukLkljC

# # vytvoříme obdelník
# x1, y1, a, b = 368, 492, 135, 56
# box = x1, y1, x1 + a, y1 + b
#
# # vytvoření obdelníku
# image = ImageGrab.grab(box)
#
# # Převedeme všechny barvy na černo-bílý obrázek
# gray = ImageOps.grayscale(image)
#
# # vytvoříme pole hodnot jednotlivých pixelů (0-255)
# a = array(gray.getcolors()

# while cyklus jednotlivých pokusů, které budeme počítat a vypíšeme vysledek
count = 0
while True:
    x1, y1, a, b = 220, 450, 75, 40
    box = x1, y1, x1 + a, y1 + b
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = array(gray.getcolors())
    value = a.sum()
    print(value)
    if value != 3247:
        count += 1
        print(count, value)
        pyautogui.press("space") # zmáčkne za nás mezerník (space)
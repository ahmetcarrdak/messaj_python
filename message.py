import pyautogui
import time

time.sleep(10)

def mesaj():
    pyautogui.write("kendimizi kandırmayalım (güzellik konusunda)")
    pyautogui.press("Enter")

while True:
    mesaj()   
    time.sleep(0) 

# Uyarı: wp açılınca açtılan bloğu hemen mesaj yağmuruna tutar
# Uyarı2: Bulduğu her yere yazı yazar
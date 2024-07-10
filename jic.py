import webbrowser
import pyautogui
import time

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1"

# Abrir el video en el navegador
webbrowser.open(url)

# Esperar a que el video cargue
time.sleep(1)

# Simular la pulsación de la tecla 'f' para pantalla completa
pyautogui.press('f')

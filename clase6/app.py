from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # Iniciar Chrome maximizado
chrome_options.add_argument("--ignore-certificate-errors") 

# Ruta al chromedriver (cambia esto por la ruta donde esté el chromedriver.exe)
chromedriver_path = "C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre la URL (en este caso Google)
driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')

# Dejar el navegador abierto durante 10 segundos
time.sleep(10)

# Cierra el navegador después de 10 segundos
driver.quit()

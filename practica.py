import locale
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
#driver = webdriver.Chrome("/usr/lib/chromum-browser/chromedriver")

# Initialize the browser driver
driver = webdriver.Chrome()

def modificar (texto):
    return texto.replace('Ñ', 'N')

date=[] #List to store name of the product
annual=[] #List to store price of the product
worth=[] #List to store rating of the product

driver.get("https://datosmacro.expansion.com/pib/ecuador")
contenido = driver.page_source
soup = BeautifulSoup(contenido,'html.parser')
tabla_datos = soup.find('table')


if tabla_datos:
    filas_tabla = tabla_datos.find_all('tr')
    for fila in filas_tabla[1:]:
        celdas = fila.find_all('td')
        date.append(modificar(celdas[0].text.strip()))
        annual.append(modificar(celdas[2].text.strip()))
        worth.append(modificar(celdas[3].text.strip()))

print(len(date))
print(len(annual))
print(len(worth))

df = pd.DataFrame({'Fecha':date,'Pib_anual':annual,'valores_pib':worth})
df.to_csv('pib_anual_Ecuador.csv', index=False,encoding='utf-8')

#Integrantes #4:
#Sanchez Brithanny
#Lopez Juley
#Olvera Shirley
#Narvaez Gabriela
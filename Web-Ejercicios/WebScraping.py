import requests
from bs4 import BeautifulSoup

# URL de la página a analizar
url = "https://news.ycombinator.com/"

# Enviar la solicitud GET
response = requests.get(url)
if response.status_code == 200: # Estado HTTP 200 Solicitud exitosa
    print("Página descargada exitosamente")
else:
    print(f"Error al descargar la página {response.status_code}") # Estado HTTP 404 Recurso no encontrado // 500 Error del servidor

# Analizar el HTML
html = response.text
soup = BeautifulSoup(html, "html.parser")

# Extraer titulares (Buscar la etiqueta dentro del código fuente HTML)
#           soup.find_all(nombreEtiqueta, nombreAtributo_="Etiqueta")
titulares = soup.find_all("span", class_="titleline")  # Extrae todas las etiquetas y los almacena en un set

# Mostrar resultados encotrados
print("\nTitulares encontrados:")
for titular in titulares:
    print(f"৹ {titular.text}") # El método .text imprime solo el texto encontrado
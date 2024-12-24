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
subtextos = soup.find_all("span", class_="subline")

# Crear una lista para almacenar ambos datos extraidos
titulares_subtextos = []

for titulo, subtext in zip(titulares, subtextos):
    titulo_text = titulo.text.strip()
    
    score_span = subtext.find("span", class_="score")
    puntos = int(score_span.text.split()[0]) if score_span else 0
    
    comentario_span =  subtext.find_all("a")[-1]
    comentarios = int(comentario_span.text.split()[0]) if "comment" in comentario_span.text else 0
    
# Guardamos los datos en diccionarios por cada iteración
    titulares_subtextos.append({
        "titulo" : titulo_text,
        "score" : puntos,
        "comentario" : comentarios,  
    })

# filtra el titular más popúlar "con más puntos"
mas_popular = max(titulares_subtextos, key=lambda x: x["score"])

print(f"\nEste es el más popular {mas_popular}")
# Mostrar resultados encotrados
print("\nTitulares encontrados:")
for i, veamos in enumerate(titulares_subtextos, start=1):
    print(f"{i}. {veamos["titulo"]}\n   {veamos["score"]} puntos - {veamos["comentario"]} comentarios")
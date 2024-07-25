from bs4 import BeautifulSoup

# Ouvrir et lire le fichier HTML localement
with open('C:/Users/admin/PycharmProjects/GameJam/gamePage.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Analyser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver toutes les balises avec la classe "tile2"
tiles = soup.find_all('div', class_='tile2')
# Récupérer les valeurs des cases tile2
valeurs_cases = [tile.text.strip() for tile in tiles]

print("Les valeurs des cases tile2 sont :", valeurs_cases)

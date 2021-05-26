
"""Ce fichier contient la méthode qui permet de traduire la couleur (l'id de la priorité)
    en une couleur connue de django pour afficher la priorité du post """

def translate_color(i):
    switcher = {
        1: 'lightgrey',
        2: 'yellow',
        3: 'orange',
        4: 'red',
        5: 'darkred',
    }
    return switcher.get(i, "Invalid color")
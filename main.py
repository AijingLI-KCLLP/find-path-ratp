"""
Vous devrez implémenter une fonction trajet qui prend 2 arguments : une station de départ et une station d'arrivée.
La fonction doit retourner une liste de stations ainsi que les lignes de métro à emprunter pour aller de la station de départ à la station d'arrivée.
Vous indiquerez également le temps de trajet estimé en minutes.

Utilisez l'algorithme A*, une variante de Dijkstra, pour trouver le chemin le plus rapide entre les deux stations.
Vous pourrez utiliser différentes heuristiques pour estimer le temps de trajet restant :
    - La distance à vol d'oiseau entre les stations
    - L'affluence des lignes de métro (plus une ligne est fréquentée, plus le temps d'attente est long)
    - Les perturbations en cours sur les lignes de métro (si une ligne est perturbée, le temps de trajet sera plus long)

Ressource utile : https://www.youtube.com/watch?v=-L-WgKMFuhE
"""


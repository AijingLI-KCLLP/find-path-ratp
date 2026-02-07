Ce planificateur calcule le plus court trajet entre deux stations du métro parisien.

## Prérequis
- Python 3.10+

## Lancer le programme
Dans le dossier du projet:

```bash
python main.py
```

Pour quitter, appuyer sur `Ctrl + C`

## Exemple de sortie
```text
🚇 Trajet Châtelet -> Nation
⏱️ Temps total estimé: 7.7 min
🔢 Correspondances: 2
🟢 Ligne 1 : 🔲 Châtelet 🔲 Hôtel de Ville 🔲 Saint-Paul 🔲 Bastille
🔁 Correspondance à Bastille: ligne 1 -> ligne 8
🟢 Ligne 8 : 🔲 Bastille 🔲 Ledru-Rollin 🔲 Faidherbe – Chaligny 🔲 Reuilly – Diderot
🔁 Correspondance à Reuilly – Diderot: ligne 8 -> ligne 1
🟢 Ligne 1 : 🔲 Reuilly – Diderot 🔲 Nation
🏁 Arrivée
```
### Notes
- L'algorithme optimise le temps estimé, le nombre de correspondances n'est pas considéré.
- Ce planificateur simule des perturbations aléatoires sur le réseau.


## Approche algorithmique (A*)
Ce planificateur utilise l'algorithmique A* (A étoile).
A* est un algorithme de plus court chemin pour un graphe pondéré.

- Dijkstra explore le graphe de manière large, sans direction vers l'objectif.
- Best-First Search va vite vers l'objectif, mais peut rater un meilleur chemin.
- A* combine les deux approches:
  - `g(n)` : coût déjà parcouru depuis le départ, soit temps passé depuis départ ici.
  - `h(n)` : estimation du coût restant jusqu'à l'arrivée, soit temps estimé jusqu'à l'arrivé (admissible si elle ne surestime pas le vrai coût).

Il choisit à chaque étape le nœud le plus prometteur avec le plus petit `f(n)` qui est la somme de `g(n)` et `h(n)`.


### Structures utilisées
- Open list: nœuds découverts à explorer (open_)
- Closed list: nœuds déjà explorés

### Remarque importante
Un noeud dans ce contexte est une entité qui stocke les information pour A* : station, `g(n)`,`h(n)`,`f(n)`, parent
Les informations métier d'une station (nom, lignes, coordonnées) restent dans `stations.py`.

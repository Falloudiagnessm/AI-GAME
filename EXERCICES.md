# 📚 Exercices et Exemples Pratiques

## 🎯 Exercice 1: Comprendre BFS

### Objectif
Observer comment BFS explore la grille niveau par niveau

### Instructions
1. Lancer le programme: `./run.sh` ou `python pathfinding.py`
2. Placer le départ en haut à gauche (vert)
3. Placer l'arrivée en bas à droite (rouge)
4. Ne PAS placer de murs
5. Appuyer sur `1` pour lancer BFS
6. Observer l'exploration en "vagues"

### Questions
- Combien de nœuds sont explorés?
- Le chemin est-il optimal?
- Quelle forme prend la zone explorée?

---

## 🎯 Exercice 2: Comprendre DFS

### Objectif
Observer comment DFS plonge en profondeur

### Instructions
1. Même configuration que l'exercice 1
2. Réinitialiser avec `C`
3. Replacer départ et arrivée
4. Appuyer sur `2` pour lancer DFS
5. Observer comment DFS explore

### Questions
- DFS trouve-t-il le même chemin que BFS?
- Explore-t-il plus ou moins de nœuds?
- Quelle direction prend-il en priorité?

---

## 🎯 Exercice 3: La Puissance de A*

### Objectif
Voir comment l'heuristique guide la recherche

### Instructions
1. Même configuration de base
2. Appuyer sur `3` pour lancer A*
3. Comparer avec BFS/DFS

### Questions
- Combien de nœuds A* explore-t-il?
- Pourquoi est-ce moins que BFS/DFS?
- Le chemin est-il optimal?
- Vers où A* dirige-t-il sa recherche?

---

## 🎯 Exercice 4: Impact des Obstacles

### Objectif
Comprendre comment les murs affectent les algorithmes

### Instructions
1. Créer un labyrinthe avec `M`
2. Comparer les 3 algorithmes avec `Espace`
3. Observer les différences

### Questions
- Quel algorithme explore le plus de nœuds?
- Quel algorithme est le plus rapide?
- BFS et A* trouvent-ils le même chemin?
- Pourquoi DFS peut-il trouver un chemin plus long?

---

## 🎯 Exercice 5: Créer un Labyrinthe Complexe

### Objectif
Tester les algorithmes sur un cas difficile

### Instructions
1. Réinitialiser avec `C`
2. Placer le départ en haut à gauche
3. Placer l'arrivée en bas à droite
4. Créer un "S" de murs au milieu
5. Lancer les 3 algorithmes

### Exemple de labyrinthe en S:
```
S = départ
E = arrivée
█ = mur

S . . . . . . . . .
. . . █ █ █ █ . . .
. . . █ . . . . . .
. . . █ . . . . . .
. . . . . . █ . . .
. . . . . . █ . . .
. . . . . . █ . . .
. . █ █ █ █ █ . . .
. . . . . . . . . .
. . . . . . . . . E
```

### Questions
- Lequel trouve le chemin le plus court?
- Lequel est le plus efficace?
- Comment se comporte DFS?

---

## 🎯 Exercice 6: Analyser les Statistiques

### Objectif
Comprendre les métriques de performance

### Instructions
1. Créer différents labyrinthes
2. Pour chacun, utiliser `Espace` pour comparer
3. Noter les résultats dans un tableau

### Tableau à remplir:

| Labyrinthe | Algo | Nœuds | Longueur | Temps |
|------------|------|-------|----------|-------|
| Simple     | BFS  |       |          |       |
| Simple     | DFS  |       |          |       |
| Simple     | A*   |       |          |       |
| Complexe   | BFS  |       |          |       |
| Complexe   | DFS  |       |          |       |
| Complexe   | A*   |       |          |       |

### Questions
- Y a-t-il une corrélation entre nœuds explorés et temps?
- A* explore-t-il toujours moins de nœuds?
- Quel algorithme préférez-vous et pourquoi?

---

## 🎯 Exercice 7: Cas Extrême - Pas de Solution

### Objectif
Voir comment les algorithmes réagissent sans solution

### Instructions
1. Placer départ et arrivée
2. Entourer complètement l'arrivée de murs
3. Tester chaque algorithme

### Questions
- Les algorithmes se terminent-ils?
- Combien de nœuds explorent-ils avant d'abandonner?
- Lequel est le plus rapide pour détecter l'absence de solution?

---

## 🎯 Exercice 8: Corridor Étroit

### Objectif
Tester l'efficacité dans un passage étroit

### Instructions
Créer ce labyrinthe:
```
S █ █ █ █ █ █ █ █ █
. █ . . . . . . . █
. █ . █ █ █ █ █ . █
. █ . █ . . . █ . █
. . . █ . E . █ . █
█ █ █ █ █ █ . █ . █
. . . . . . . █ . .
. █ █ █ █ █ █ █ . .
. . . . . . . . . .
```

### Questions
- A* explore-t-il moins dans le couloir?
- DFS suit-il le couloir jusqu'au bout?
- Quel algorithme est le plus efficace ici?

---

## 🎯 Exercice 9: Optimisation de l'Heuristique

### Objectif
Comprendre l'importance de l'heuristique

### Réflexion
Dans le code `pathfinding.py`, la fonction heuristique est:
```python
def heuristic(node1, node2):
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()
    return abs(x1 - x2) + abs(y1 - y2)  # Manhattan
```

### Questions
1. Pourquoi utiliser la distance de Manhattan?
2. Que se passerait-il avec la distance Euclidienne?
   ```python
   return math.sqrt((x1-x2)**2 + (y1-y2)**2)
   ```
3. Que se passerait-il si on multipliait par 2?
   ```python
   return 2 * (abs(x1 - x2) + abs(y1 - y2))
   ```
4. Serait-ce toujours optimal?

---

## 🎯 Exercice 10: Projet Personnel

### Objectif
Créer votre propre labyrinthe et analyser

### Instructions
1. Dessinez sur papier un labyrinthe intéressant
2. Recréez-le dans le programme
3. Prédisez quel algorithme sera le meilleur
4. Testez et comparez avec votre prédiction
5. Expliquez les résultats

### Bonus
Photographiez votre labyrinthe papier et vos résultats!

---

## 📊 Défis Avancés

### Défi 1: Spirale
Créez un labyrinthe en spirale. Quel algorithme gère-t-il le mieux?

### Défi 2: Damier
Alternez murs et espaces en damier. Comment les algorithmes s'adaptent-ils?

### Défi 3: Multiples Chemins
Créez plusieurs chemins possibles. DFS et BFS trouvent-ils le même?

### Défi 4: Tunnel Long
Un seul chemin très long et tortueux. Qui est le plus rapide?

---

## 💡 Questions de Réflexion

### Théorie
1. Pourquoi BFS garantit-il l'optimalité?
2. Dans quel cas DFS serait-il préférable à BFS?
3. Qu'est-ce qu'une heuristique "admissible"?
4. A* devient-il équivalent à Dijkstra si h(n) = 0?

### Pratique
1. Comment adapteriez-vous ces algorithmes pour un graphe pondéré?
2. Comment gérer les mouvements en diagonale?
3. Comment implémenter une animation plus lente?
4. Comment sauvegarder un labyrinthe?

---

## 🎓 Pour Aller Plus Loin

### Modifications du Code

#### 1. Ajouter les Diagonales
Modifier `update_neighbors()` pour inclure les 4 diagonales

#### 2. Coûts Variables
Certaines cases coûtent plus cher à traverser (terrain difficile)

#### 3. Plusieurs Arrivées
Trouver le chemin vers la destination la plus proche parmi plusieurs

#### 4. Animation Contrôlée
Ajouter un curseur pour contrôler la vitesse d'animation

#### 5. Sauvegarde/Chargement
Sauvegarder des labyrinthes en fichiers JSON

---

## 📝 Rapport de Projet Suggéré

### Structure Recommandée

1. **Introduction**
   - Présentation des algorithmes
   - Objectifs du projet

2. **Méthodologie**
   - Implémentation technique
   - Choix de design

3. **Résultats**
   - Tableaux comparatifs
   - Screenshots des différents cas

4. **Analyse**
   - Interprétation des résultats
   - Forces et faiblesses de chaque algorithme

5. **Conclusion**
   - Apprentissages clés
   - Recommandations

6. **Annexes**
   - Code source
   - Labyrinthes de test

---

## ✅ Checklist de Compréhension

Vous avez maîtrisé le sujet si vous pouvez:

- [ ] Expliquer la différence entre BFS et DFS
- [ ] Décrire comment fonctionne l'heuristique d'A*
- [ ] Prédire quel algorithme sera le meilleur dans un cas donné
- [ ] Identifier les cas où DFS n'est pas optimal
- [ ] Expliquer pourquoi A* est généralement préféré
- [ ] Comprendre la complexité temporelle de chaque algorithme
- [ ] Créer et analyser vos propres labyrinthes
- [ ] Modifier le code pour ajouter des fonctionnalités

---

## 🎉 Félicitations!

Vous avez maintenant une compréhension approfondie des algorithmes de pathfinding!

**Prochaines étapes:**
- Implémenter Dijkstra
- Découvrir Jump Point Search
- Étudier les variantes bidirectionnelles
- Explorer l'application en robotique

**Bon courage! 🚀**

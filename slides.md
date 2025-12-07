# 🎯 Pathfinding: BFS, DFS, A*
## Présentation des Algorithmes de Recherche de Chemin

---

## 📋 Sommaire

1. Introduction au Pathfinding
2. BFS (Breadth-First Search)
3. DFS (Depth-First Search)
4. A* (A-Star)
5. Comparaison
6. Démonstration

---

## 🔍 Qu'est-ce que le Pathfinding?

**Définition:** Trouver le chemin optimal entre deux points dans un graphe/grille

**Applications:**
- 🎮 Jeux vidéo (déplacement des PNJ)
- 🗺️ GPS et navigation
- 🤖 Robotique
- 🌐 Routage réseau

**Problème:** Comment explorer efficacement l'espace de recherche?

---

## 🌊 BFS (Breadth-First Search)

### Principe
- Explore **niveau par niveau**
- Utilise une **file (FIFO)**
- Garantit le **chemin le plus court**

### Algorithme
```
1. Ajouter le départ à la file
2. Tant que la file n'est pas vide:
   a. Retirer le premier élément
   b. Si c'est l'arrivée → Terminé!
   c. Ajouter tous les voisins non visités
```

### Caractéristiques
- ✅ **Optimal:** Trouve le chemin le plus court
- ✅ **Complet:** Trouve toujours une solution si elle existe
- ❌ **Coûteux:** Explore beaucoup de nœuds
- 📊 **Complexité:** O(V + E)

---

## 🌲 DFS (Depth-First Search)

### Principe
- Explore **en profondeur** d'abord
- Utilise une **pile (LIFO)**
- **Ne garantit PAS** le chemin optimal

### Algorithme
```
1. Ajouter le départ à la pile
2. Tant que la pile n'est pas vide:
   a. Retirer le dernier élément
   b. Si c'est l'arrivée → Terminé!
   c. Ajouter tous les voisins non visités
```

### Caractéristiques
- ❌ **Non-optimal:** Peut trouver un long chemin
- ✅ **Complet:** Trouve une solution (graphes finis)
- ✅ **Économe:** Moins de mémoire que BFS
- 📊 **Complexité:** O(V + E)

---

## ⭐ A* (A-Star)

### Principe
- Utilise une **heuristique** pour guider la recherche
- Combine coût réel + estimation
- **Optimal ET efficace**

### Formule
```
f(n) = g(n) + h(n)

où:
- g(n) = coût depuis le départ
- h(n) = estimation vers l'arrivée (heuristique)
- f(n) = score total
```

### Heuristique: Distance de Manhattan
```
h(n) = |x₁ - x₂| + |y₁ - y₂|
```

### Caractéristiques
- ✅ **Optimal:** Avec heuristique admissible
- ✅ **Efficace:** Explore moins de nœuds
- ✅ **Intelligent:** Guidé par l'heuristique
- 📊 **Complexité:** O(E) dans le meilleur cas

---

## 📊 Comparaison

| Critère | BFS | DFS | A* |
|---------|-----|-----|----|
| **Optimalité** | ✅ Oui | ❌ Non | ✅ Oui |
| **Complétude** | ✅ Oui | ✅ Oui* | ✅ Oui |
| **Mémoire** | 😐 Moyenne | 😊 Faible | 😐 Moyenne |
| **Vitesse** | 😐 Moyenne | 😊 Rapide | 😊 Très rapide |
| **Nœuds explorés** | 😔 Beaucoup | 😔 Beaucoup | 😊 Peu |
| **Heuristique** | ❌ Non | ❌ Non | ✅ Oui |

*DFS est complet pour les graphes finis

---

## 🎨 Visualisation

### Couleurs dans la démo

| Couleur | Signification |
|---------|---------------|
| 🟢 Vert | Point de départ |
| 🔴 Rouge | Point d'arrivée |
| ⬛ Noir | Murs (obstacles) |
| 🟡 Jaune | Nœuds en attente |
| 🔵 Turquoise | Nœuds visités |
| 🟣 Violet | Chemin final |

---

## 🧮 Exemple: Labyrinthe 10x10

### Résultats typiques

**BFS:**
- Nœuds explorés: 45
- Longueur du chemin: 18
- Temps: 0.023s
- ✅ Chemin optimal

**DFS:**
- Nœuds explorés: 52
- Longueur du chemin: 34
- Temps: 0.018s
- ❌ Chemin non-optimal

**A*:**
- Nœuds explorés: 23
- Longueur du chemin: 18
- Temps: 0.015s
- ✅ Chemin optimal + **le plus efficace!**

---

## 🎯 Quand utiliser quel algorithme?

### BFS
- 📍 Graphes non pondérés
- 📍 Garantie d'optimalité requise
- 📍 Espace de recherche petit

### DFS
- 📍 Recherche de solutions (pas forcément optimales)
- 📍 Mémoire limitée
- 📍 Problèmes de génération de labyrinthes

### A*
- 📍 **Meilleur choix général pour pathfinding**
- 📍 Heuristique disponible
- 📍 Besoin d'optimalité ET d'efficacité
- 📍 Jeux vidéo, robotique, GPS

---

## 🔬 Concepts Avancés

### Heuristiques admissibles
Une heuristique h(n) est **admissible** si:
```
h(n) ≤ coût_réel(n, arrivée)
```

**Exemples:**
- ✅ Distance de Manhattan (grilles 4-directions)
- ✅ Distance Euclidienne
- ❌ Distance × 2 (surestimation)

### Grille vs Graphe
```
Grille 2D → Graphe

[X][X][X]     A-B-C
[X][X][X]  →  D-E-F
[X][X][X]     G-H-I
```

---

## 💡 Points Clés à Retenir

1. **BFS** = Simple, optimal, mais lent
2. **DFS** = Rapide, économe, mais non-optimal
3. **A*** = **Le meilleur des deux mondes** 🏆

4. L'heuristique fait toute la différence
5. Le choix dépend du problème spécifique

---

## 🎮 Démonstration Live

### Étapes
1. Créer un labyrinthe (touche M)
2. Placer départ et arrivée
3. Comparer les 3 algorithmes (Espace)
4. Observer les différences!

### Ce qu'on observe:
- 🔵 BFS explore en cercles concentriques
- 🔴 DFS plonge dans une direction
- ⭐ A* fonce vers l'objectif

---

## 📚 Ressources

### Pour aller plus loin
- Dijkstra (A* sans heuristique)
- Jump Point Search (optimisation d'A*)
- Theta* (pathfinding avec angles)
- D* (pathfinding dynamique)

### Applications pratiques
- Navigation dans les jeux (Starcraft, DOTA)
- Planification de trajectoires robotiques
- Optimisation de livraisons
- Intelligence artificielle

---

## ❓ Questions?

### Démonstration interactive disponible!

**Commandes:**
- `python pathfinding.py`

**Fichiers:**
- 📄 `pathfinding.py` - Code complet
- 📖 `README.md` - Documentation
- 📊 `slides.md` - Cette présentation

---

## 🎓 Conclusion

### Ce que nous avons appris

1. ✅ Trois approches du pathfinding
2. ✅ Compromis entre optimalité et performance
3. ✅ Importance des heuristiques
4. ✅ Visualisation et comparaison pratique

### Résultat
**A* est généralement le meilleur choix** pour les problèmes de pathfinding réels! 🏆

---

## 🙏 Merci!

**Temps de présentation:** 8-12 minutes

**Questions?**

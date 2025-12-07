# 🎮 Projet Pathfinding: BFS, DFS et A*

## 📋 Description

Ce projet implémente et compare trois algorithmes classiques de recherche de chemin:
- **BFS (Breadth-First Search)** - Recherche en largeur
- **DFS (Depth-First Search)** - Recherche en profondeur  
- **A*** - Algorithme heuristique optimal

## 🎯 Objectif

Comprendre les différences entre ces algorithmes en termes de:
- **Vitesse d'exécution**
- **Optimalité du chemin** (longueur)
- **Nombre de nœuds explorés**
- **Comportement visuel**

## 🚀 Installation

### Prérequis
- Python 3.7 ou supérieur

### Étapes

1. **Installer les dépendances:**
```bash
pip install -r requirements.txt
```

2. **Lancer le programme:**
```bash
python pathfinding.py
```

## 🎮 Utilisation

### Contrôles

| Action | Touche/Souris |
|--------|---------------|
| Placer le point de départ (vert) | Premier clic gauche |
| Placer le point d'arrivée (rouge) | Deuxième clic gauche |
| Dessiner des murs (noir) | Clics gauches suivants |
| Effacer une case | Clic droit |
| Exécuter BFS | Touche `1` |
| Exécuter DFS | Touche `2` |
| Exécuter A* | Touche `3` |
| Comparer les 3 algorithmes | Touche `Espace` |
| Créer un labyrinthe | Touche `M` |
| Réinitialiser la grille | Touche `C` |

### Couleurs

- 🟢 **Vert** : Point de départ
- 🔴 **Rouge** : Point d'arrivée
- ⬛ **Noir** : Murs (obstacles)
- 🟡 **Jaune** : Nœuds dans la file d'attente (à explorer)
- 🔵 **Turquoise** : Nœuds déjà visités
- 🟣 **Violet** : Chemin final trouvé

## 📊 Comparaison des Algorithmes

### BFS (Breadth-First Search)
- ✅ **Garantit le chemin le plus court** (en nombre de cases)
- ✅ Explore de manière systématique niveau par niveau
- ❌ Peut explorer beaucoup de nœuds
- 🎯 **Coût:** O(V + E) où V = nœuds, E = arêtes
- 📈 **Heuristique:** Aucune

### DFS (Depth-First Search)
- ❌ **Ne garantit PAS le chemin optimal**
- ✅ Utilise moins de mémoire (pile)
- ❌ Peut explorer beaucoup de nœuds inutiles
- 🎯 **Coût:** O(V + E)
- 📈 **Heuristique:** Aucune

### A* (A-Star)
- ✅ **Garantit le chemin optimal**
- ✅ **Plus efficace** grâce à l'heuristique
- ✅ Explore moins de nœuds que BFS/DFS
- 🎯 **Coût:** O(E) avec une bonne heuristique
- 📈 **Heuristique:** Distance de Manhattan

## 🧮 Détails Techniques

### Heuristique (A*)
La distance de Manhattan est utilisée:
```
h(n) = |x₁ - x₂| + |y₁ - y₂|
```

### Grille vs Graphe
- **Grille:** Représentation visuelle 2D (20×30 cases)
- **Graphe:** Chaque case = nœud, adjacence = arête

## 📈 Résultats Attendus

Sur un labyrinthe typique:

| Algorithme | Nœuds Explorés | Longueur Chemin | Vitesse |
|------------|----------------|-----------------|---------|
| BFS | ~150-200 | **Optimal** ✅ | Moyen |
| DFS | ~200-300 | Non-optimal ❌ | Rapide |
| A* | ~50-100 | **Optimal** ✅ | **Le plus rapide** 🏆 |

## 📚 Concepts Importants

### 1. **Coûts et Heuristiques**
- `g(n)`: Coût depuis le départ
- `h(n)`: Heuristique (estimation vers l'arrivée)
- `f(n) = g(n) + h(n)`: Score total (A*)

### 2. **Grille vs Graphe**
- Une grille 2D est un cas particulier de graphe
- Chaque case peut avoir jusqu'à 4 voisins (haut, bas, gauche, droite)

### 3. **Optimalité**
- BFS et A* garantissent le chemin optimal
- DFS peut trouver un chemin, mais pas forcément le plus court

## 🎓 Livrables (selon cahier des charges)

✅ **Code des 3 algorithmes** - Implémenté dans `pathfinding.py`
✅ **Comparaison (vitesse, optimalité)** - Affichée en console et à l'écran
✅ **Visualisation du labyrinthe** - Interface graphique Pygame
✅ **Nœuds visités en direct** - Coloration en temps réel

## 🕐 Durée

- **Installation:** 2 minutes
- **Prise en main:** 3-5 minutes
- **Démonstration complète:** 8-12 minutes

## 🐛 Dépannage

### Erreur: "No module named 'pygame'"
```bash
pip install pygame
```

### L'application ne se lance pas
Vérifier que Python 3.7+ est installé:
```bash
python --version
```

## 👨‍💻 Auteur

Projet réalisé dans le cadre de l'étude des algorithmes de pathfinding.

## 📝 License

Ce projet est à usage éducatif.

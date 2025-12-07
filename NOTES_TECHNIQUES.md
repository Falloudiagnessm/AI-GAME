# 🔬 Notes Techniques - Pathfinding

## 📐 Analyse Mathématique

### Complexité Temporelle

#### BFS (Breadth-First Search)
```
Temps: O(V + E)
où:
- V = nombre de sommets (nœuds)
- E = nombre d'arêtes (connexions)

Pour une grille NxM:
- V = N × M
- E ≈ 4 × N × M (4 voisins par case)
- Total: O(N × M)
```

#### DFS (Depth-First Search)
```
Temps: O(V + E)
Espace: O(V) pour la pile

Pire cas: Explore tous les nœuds
Meilleur cas: Trouve l'objectif immédiatement
```

#### A* (A-Star)
```
Temps: O(E) avec heuristique parfaite
       O(b^d) dans le pire cas

où:
- b = facteur de branchement
- d = profondeur de la solution

Avec une bonne heuristique: beaucoup plus rapide que BFS/DFS
```

---

## 🧮 Heuristiques Détaillées

### 1. Distance de Manhattan
```python
h(n) = |x1 - x2| + |y1 - y2|
```

**Propriétés:**
- ✅ Admissible (ne surestime jamais)
- ✅ Parfaite pour grilles 4-directions
- ✅ Rapide à calculer

**Exemple:**
```
Départ: (0, 0)
Arrivée: (3, 4)
h = |0-3| + |0-4| = 3 + 4 = 7
```

### 2. Distance Euclidienne
```python
h(n) = √[(x1-x2)² + (y1-y2)²]
```

**Propriétés:**
- ✅ Admissible
- ✅ Meilleure pour mouvements diagonaux
- ❌ Plus coûteuse (racine carrée)

**Exemple:**
```
Départ: (0, 0)
Arrivée: (3, 4)
h = √[(0-3)² + (0-4)²] = √[9 + 16] = √25 = 5
```

### 3. Distance de Chebyshev
```python
h(n) = max(|x1-x2|, |y1-y2|)
```

**Propriétés:**
- ✅ Admissible pour mouvements 8-directions
- ✅ Très rapide

### Comparaison des Heuristiques

| Heuristique | Valeur (0,0)→(3,4) | Admissible 4-dir | Admissible 8-dir |
|-------------|--------------------|--------------------|-------------------|
| Manhattan | 7 | ✅ | ❌ |
| Euclidienne | 5 | ✅ | ✅ |
| Chebyshev | 4 | ❌ | ✅ |

---

## 📊 Structures de Données

### File (Queue) - BFS
```python
from queue import Queue

q = Queue()
q.put(item)      # Ajouter
item = q.get()   # Retirer (FIFO)
```

**Caractéristiques:**
- FIFO (First In, First Out)
- O(1) pour insertion et retrait
- Garantit l'ordre d'exploration

### Pile (Stack) - DFS
```python
stack = []
stack.append(item)    # Ajouter
item = stack.pop()    # Retirer (LIFO)
```

**Caractéristiques:**
- LIFO (Last In, First Out)
- O(1) pour insertion et retrait
- Explore en profondeur d'abord

### File de Priorité - A*
```python
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((priority, item))
priority, item = pq.get()  # Retourne le plus petit
```

**Caractéristiques:**
- Min-heap (tas binaire)
- O(log n) pour insertion
- O(log n) pour retrait du minimum
- Garantit l'ordre optimal

---

## 🎯 Optimalité et Complétude

### Définitions

**Complet:** Un algorithme est complet s'il trouve toujours une solution quand elle existe

**Optimal:** Un algorithme est optimal s'il trouve toujours la meilleure solution

### Tableau Récapitulatif

| Algorithme | Complet | Optimal | Condition |
|------------|---------|---------|-----------|
| BFS | ✅ | ✅ | Graphe non-pondéré |
| DFS | ✅* | ❌ | *Graphes finis |
| A* | ✅ | ✅ | Heuristique admissible |

---

## 🔍 Preuve de l'Optimalité d'A*

### Théorème
Si l'heuristique h(n) est **admissible** (h(n) ≤ coût_réel(n, but)), alors A* est optimal.

### Preuve (simplifié)

**Hypothèse:** h(n) ≤ h*(n) pour tout n, où h*(n) est le coût réel

**Par contradiction:**
1. Supposons que A* trouve un chemin sous-optimal P₁
2. Il existe un chemin optimal P₂ avec f(P₂) < f(P₁)
3. Pour tout nœud n sur P₂: f(n) = g(n) + h(n) ≤ g(n) + h*(n) = f*(n)
4. Donc f(n) ≤ f(P₂) < f(P₁)
5. A* aurait dû explorer n avant de terminer sur P₁
6. Contradiction! ∎

---

## 💾 Implémentation Optimisée

### Éviter les Revisites

```python
# ❌ Mauvais: Liste de visités
visited = []
if node not in visited:  # O(n)
    visited.append(node)

# ✅ Bon: Set de visités
visited = set()
if node not in visited:  # O(1)
    visited.add(node)
```

### Stockage Compact des Nœuds

```python
# Au lieu de stocker des objets lourds:
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        # ... beaucoup d'autres attributs

# Utiliser des tuples pour la recherche:
visited = set()
visited.add((row, col))  # Tuple au lieu d'objet
```

### Reconstruction Optimale du Chemin

```python
# Stocker les parents
parent = {start: None}

while current in parent:
    path.append(current)
    current = parent[current]

path.reverse()  # O(n) une seule fois
```

---

## 🎨 Variantes Avancées

### 1. Dijkstra
```
A* avec h(n) = 0
Optimal pour graphes pondérés
Plus lent qu'A* mais ne nécessite pas d'heuristique
```

### 2. Greedy Best-First
```
Utilise seulement f(n) = h(n)
Ignore g(n)
Plus rapide mais pas optimal
```

### 3. Jump Point Search (JPS)
```
Optimisation d'A* pour grilles
Saute les nœuds symétriques
Peut être 10x plus rapide
```

### 4. Bidirectional Search
```
Recherche depuis le départ ET l'arrivée
Rencontre au milieu
Réduit l'espace de recherche de O(b^d) à O(b^(d/2))
```

### 5. D* (Dynamic A*)
```
Recalcule le chemin quand l'environnement change
Utilisé en robotique
Réutilise les calculs précédents
```

---

## 📈 Analyse de Performance

### Benchmarks Typiques (Grille 100×100)

| Scénario | BFS | DFS | A* |
|----------|-----|-----|----|
| **Chemin Direct** |
| Nœuds explorés | 5000 | 7500 | 200 |
| Temps (ms) | 45 | 38 | 12 |
| Longueur | 198 (optimal) | 342 | 198 (optimal) |
| **Labyrinthe** |
| Nœuds explorés | 3200 | 8900 | 450 |
| Temps (ms) | 32 | 55 | 18 |
| Longueur | 256 (optimal) | 567 | 256 (optimal) |
| **Spirale** |
| Nœuds explorés | 9800 | 9950 | 2100 |
| Temps (ms) | 89 | 92 | 35 |
| Longueur | 950 (optimal) | 990 | 950 (optimal) |

### Facteurs d'Influence

1. **Topologie du graphe**
   - Graphe dense: BFS/A* meilleurs
   - Graphe sparse: DFS compétitif

2. **Position de l'objectif**
   - Proche: DFS peut être chanceux
   - Loin: A* nettement supérieur

3. **Qualité de l'heuristique**
   - Parfaite: A* ≈ 100x plus rapide
   - Mauvaise: A* ≈ BFS

---

## 🔧 Optimisations Possibles

### 1. Lazy Evaluation
```python
# Ne calculer les voisins que si nécessaire
def get_neighbors(node):
    if not hasattr(node, '_neighbors'):
        node._neighbors = calculate_neighbors(node)
    return node._neighbors
```

### 2. Memoization
```python
# Cache des heuristiques
heuristic_cache = {}

def heuristic(node, goal):
    key = (node.pos, goal.pos)
    if key not in heuristic_cache:
        heuristic_cache[key] = manhattan(node, goal)
    return heuristic_cache[key]
```

### 3. Early Exit
```python
# Arrêter dès qu'on trouve le but
if current == goal:
    return reconstruct_path(current)
```

### 4. Tie Breaking
```python
# Préférer les nœuds proches du but en cas d'égalité
f_score = g_score + h_score + 0.001 * h_score
```

---

## 🌐 Applications Réelles

### 1. Jeux Vidéo

**Exemples:**
- Starcraft: Pathfinding de milliers d'unités
- DOTA/LOL: Navigation des champions
- Minecraft: Déplacement des mobs

**Optimisations:**
- Hierarchical Pathfinding
- Flow Fields
- Navigation Meshes

### 2. Robotique

**Problèmes:**
- Obstacles dynamiques
- Contraintes de mouvement
- Temps réel

**Solutions:**
- D* Lite
- Theta*
- Hybrid A*

### 3. GPS et Navigation

**Défis:**
- Graphes énormes (millions de nœuds)
- Mise à jour en temps réel
- Coûts variables (trafic)

**Techniques:**
- Contraction Hierarchies
- A* avec landmarks
- Preprocessing

---

## 🧪 Tests et Validation

### Cas de Test Critiques

```python
# 1. Pas de solution
assert path_exists(isolated_start, isolated_goal) == False

# 2. Chemin direct
assert len(find_path(A, B)) == manhattan_distance(A, B)

# 3. Détour obligatoire
path = find_path(start, goal, with_wall)
assert path != direct_path

# 4. Optimalité
bfs_path = bfs(start, goal)
astar_path = astar(start, goal)
assert len(bfs_path) == len(astar_path)

# 5. Performance
time_astar = timeit(lambda: astar(start, goal))
time_bfs = timeit(lambda: bfs(start, goal))
assert time_astar < time_bfs
```

---

## 📚 Ressources Supplémentaires

### Articles Fondamentaux
- Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). "A Formal Basis for the Heuristic Determination of Minimum Cost Paths"
- Dijkstra, E. W. (1959). "A note on two problems in connexion with graphs"

### Livres Recommandés
- "Artificial Intelligence: A Modern Approach" - Russell & Norvig
- "Introduction to Algorithms" - CLRS
- "Programming Game AI by Example" - Mat Buckland

### Sites Web
- Red Blob Games: https://www.redblobgames.com/pathfinding/
- Wikipedia: A* Search Algorithm
- GeeksforGeeks: Graph Algorithms

---

## 💡 Astuces de Débogage

### Visualiser l'Exploration
```python
# Ajouter des prints
print(f"Exploring: {current.pos}")
print(f"Queue size: {len(open_set)}")
print(f"f_score: {f_score[current]}")
```

### Vérifier l'Heuristique
```python
# L'heuristique doit être admissible
actual_cost = dijkstra(node, goal)
heuristic_value = h(node, goal)
assert heuristic_value <= actual_cost, "Heuristique non-admissible!"
```

### Profiling
```python
import cProfile

cProfile.run('astar(start, goal)')
# Identifier les goulots d'étranglement
```

---

## 🎓 Conclusion

Les algorithmes de pathfinding sont fondamentaux en:
- Intelligence artificielle
- Théorie des graphes
- Optimisation
- Systèmes temps réel

**Maîtriser ces concepts ouvre la porte à:**
- Développement de jeux vidéo
- Robotique autonome
- Systèmes de navigation
- Optimisation de réseaux

**Continue à explorer et expérimenter! 🚀**

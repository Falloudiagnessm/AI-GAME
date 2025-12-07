"""
Projet: Algorithmes de Recherche de Chemin (Pathfinding)
Implémentation de BFS, DFS et A*
Avec visualisation et comparaison des performances
"""

import pygame
import math
from queue import Queue, PriorityQueue
from collections import deque
import time

# Constantes
WIDTH = 800
HEIGHT = 600
ROWS = 20
COLS = 30
CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    """Représente une cellule dans la grille"""
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * CELL_WIDTH
        self.y = row * CELL_HEIGHT
        self.color = WHITE
        self.neighbors = []
        self.parent = None
        
    def get_pos(self):
        return self.row, self.col
    
    def is_wall(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == GREEN
    
    def is_end(self):
        return self.color == RED
    
    def reset(self):
        self.color = WHITE
        self.parent = None
        
    def make_start(self):
        self.color = GREEN
        
    def make_end(self):
        self.color = RED
        
    def make_wall(self):
        self.color = BLACK
        
    def make_visited(self):
        self.color = TURQUOISE
        
    def make_open(self):
        self.color = YELLOW
        
    def make_path(self):
        self.color = PURPLE
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, CELL_WIDTH, CELL_HEIGHT))
        
    def update_neighbors(self, grid):
        """Met à jour la liste des voisins accessibles"""
        self.neighbors = []
        
        # Bas
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_wall():
            self.neighbors.append(grid[self.row + 1][self.col])
            
        # Haut
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
            self.neighbors.append(grid[self.row - 1][self.col])
            
        # Droite
        if self.col < COLS - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbors.append(grid[self.row][self.col + 1])
            
        # Gauche
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            self.neighbors.append(grid[self.row][self.col - 1])
    
    def __lt__(self, other):
        return False


def heuristic(node1, node2):
    """Fonction heuristique pour A* (distance de Manhattan)"""
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(current, start, draw):
    """Reconstruit et dessine le chemin trouvé"""
    path = []
    while current.parent:
        path.append(current)
        current = current.parent
        if current != start:
            current.make_path()
        draw()
    return len(path)


def bfs(draw, grid, start, end):
    """
    Breadth-First Search (BFS)
    - Explore tous les voisins au même niveau avant d'aller plus profond
    - Garantit le chemin le plus court en nombre de nœuds
    """
    start_time = time.time()
    count = 0
    queue = Queue()
    queue.put(start)
    visited = {start}
    nodes_explored = 0
    
    while not queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        current = queue.get()
        nodes_explored += 1
        
        if current == end:
            path_length = reconstruct_path(end, start, draw)
            end.make_end()
            start.make_start()
            elapsed_time = time.time() - start_time
            return True, nodes_explored, path_length, elapsed_time
        
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor.parent = current
                queue.put(neighbor)
                if neighbor != end:
                    neighbor.make_open()
        
        draw()
        
        if current != start:
            current.make_visited()
    
    elapsed_time = time.time() - start_time
    return False, nodes_explored, 0, elapsed_time


def dfs(draw, grid, start, end):
    """
    Depth-First Search (DFS)
    - Explore en profondeur avant d'explorer en largeur
    - Ne garantit pas le chemin le plus court
    """
    start_time = time.time()
    stack = [start]
    visited = {start}
    nodes_explored = 0
    
    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        current = stack.pop()
        nodes_explored += 1
        
        if current == end:
            path_length = reconstruct_path(end, start, draw)
            end.make_end()
            start.make_start()
            elapsed_time = time.time() - start_time
            return True, nodes_explored, path_length, elapsed_time
        
        if current != start:
            current.make_visited()
        
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor.parent = current
                stack.append(neighbor)
                if neighbor != end:
                    neighbor.make_open()
        
        draw()
    
    elapsed_time = time.time() - start_time
    return False, nodes_explored, 0, elapsed_time


def astar(draw, grid, start, end):
    """
    A* Algorithm
    - Utilise une heuristique pour guider la recherche
    - Garantit le chemin optimal
    - Plus efficace que BFS/DFS avec une bonne heuristique
    """
    start_time = time.time()
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    open_set_hash = {start}
    
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = heuristic(start, end)
    
    nodes_explored = 0
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        current = open_set.get()[2]
        open_set_hash.remove(current)
        nodes_explored += 1
        
        if current == end:
            path_length = reconstruct_path(end, start, draw)
            end.make_end()
            start.make_start()
            elapsed_time = time.time() - start_time
            return True, nodes_explored, path_length, elapsed_time
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            
            if temp_g_score < g_score[neighbor]:
                neighbor.parent = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, end)
                
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    if neighbor != end:
                        neighbor.make_open()
        
        draw()
        
        if current != start:
            current.make_visited()
    
    elapsed_time = time.time() - start_time
    return False, nodes_explored, 0, elapsed_time


def make_grid():
    """Crée la grille de nœuds"""
    grid = []
    for i in range(ROWS):
        grid.append([])
        for j in range(COLS):
            node = Node(i, j)
            grid[i].append(node)
    return grid


def draw_grid_lines(win):
    """Dessine les lignes de la grille"""
    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i * CELL_HEIGHT), (WIDTH, i * CELL_HEIGHT))
    for j in range(COLS):
        pygame.draw.line(win, GREY, (j * CELL_WIDTH, 0), (j * CELL_WIDTH, HEIGHT))


def draw(win, grid, stats_text=""):
    """Dessine tout à l'écran"""
    win.fill(WHITE)
    
    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_grid_lines(win)
    
    # Afficher les statistiques
    if stats_text:
        font = pygame.font.Font(None, 24)
        lines = stats_text.split('\n')
        for i, line in enumerate(lines):
            text = font.render(line, True, BLACK)
            win.blit(text, (10, HEIGHT + 10 + i * 25))
    
    pygame.display.update()


def get_clicked_pos(pos):
    """Convertit la position de la souris en position de grille"""
    x, y = pos
    row = y // CELL_HEIGHT
    col = x // CELL_WIDTH
    
    if row >= ROWS:
        row = ROWS - 1
    if col >= COLS:
        col = COLS - 1
        
    return row, col


def reset_grid_colors(grid, start, end):
    """Réinitialise les couleurs de la grille (garde les murs)"""
    for row in grid:
        for node in row:
            if not node.is_wall() and node != start and node != end:
                node.reset()


def create_maze(grid, start, end):
    """Crée un labyrinthe simple"""
    # Réinitialiser d'abord
    for row in grid:
        for node in row:
            if node != start and node != end:
                node.reset()
    
    # Créer quelques murs
    # Murs horizontaux
    for col in range(5, 25):
        if col != 10:  # Laisser un passage
            grid[5][col].make_wall()
    
    for col in range(5, 25):
        if col != 15:
            grid[10][col].make_wall()
            
    for col in range(5, 25):
        if col != 20:
            grid[15][col].make_wall()
    
    # Murs verticaux
    for row in range(5, 15):
        if row != 10:
            grid[row][10].make_wall()
            
    for row in range(5, 15):
        if row != 8:
            grid[row][20].make_wall()


def main():
    """Fonction principale"""
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT + 150))
    pygame.display.set_caption("Pathfinding: BFS vs DFS vs A*")
    
    grid = make_grid()
    
    start = None
    end = None
    
    run = True
    started = False
    stats_text = ""
    
    print("=" * 60)
    print("CONTRÔLES:")
    print("=" * 60)
    print("• Clic gauche: Placer départ (vert), arrivée (rouge), puis murs (noir)")
    print("• Clic droit: Effacer")
    print("• Touche 1: Exécuter BFS")
    print("• Touche 2: Exécuter DFS")
    print("• Touche 3: Exécuter A*")
    print("• Touche M: Créer un labyrinthe")
    print("• Touche C: Réinitialiser")
    print("• Touche ESPACE: Comparer les 3 algorithmes")
    print("=" * 60)
    
    while run:
        draw(win, grid, stats_text)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if started:
                continue
                
            # Clic gauche - placer start/end/murs
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[1] < HEIGHT:  # Ne pas cliquer sur la zone de stats
                    row, col = get_clicked_pos(pos)
                    node = grid[row][col]
                    
                    if not start and node != end:
                        start = node
                        start.make_start()
                        
                    elif not end and node != start:
                        end = node
                        end.make_end()
                        
                    elif node != start and node != end:
                        node.make_wall()
            
            # Clic droit - effacer
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                if pos[1] < HEIGHT:
                    row, col = get_clicked_pos(pos)
                    node = grid[row][col]
                    node.reset()
                    
                    if node == start:
                        start = None
                    elif node == end:
                        end = None
            
            if event.type == pygame.KEYDOWN:
                # BFS
                if event.key == pygame.K_1 and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    reset_grid_colors(grid, start, end)
                    print("\n🔵 Exécution de BFS...")
                    found, nodes, path_len, time_taken = bfs(lambda: draw(win, grid), grid, start, end)
                    
                    if found:
                        stats_text = f"BFS - Chemin trouvé!\nNœuds explorés: {nodes}\nLongueur: {path_len}\nTemps: {time_taken:.4f}s"
                        print(f"✓ Chemin trouvé! Nœuds: {nodes}, Longueur: {path_len}, Temps: {time_taken:.4f}s")
                    else:
                        stats_text = "BFS - Aucun chemin trouvé"
                        print("✗ Aucun chemin trouvé")
                
                # DFS
                if event.key == pygame.K_2 and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    reset_grid_colors(grid, start, end)
                    print("\n🔴 Exécution de DFS...")
                    found, nodes, path_len, time_taken = dfs(lambda: draw(win, grid), grid, start, end)
                    
                    if found:
                        stats_text = f"DFS - Chemin trouvé!\nNœuds explorés: {nodes}\nLongueur: {path_len}\nTemps: {time_taken:.4f}s"
                        print(f"✓ Chemin trouvé! Nœuds: {nodes}, Longueur: {path_len}, Temps: {time_taken:.4f}s")
                    else:
                        stats_text = "DFS - Aucun chemin trouvé"
                        print("✗ Aucun chemin trouvé")
                
                # A*
                if event.key == pygame.K_3 and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    reset_grid_colors(grid, start, end)
                    print("\n⭐ Exécution de A*...")
                    found, nodes, path_len, time_taken = astar(lambda: draw(win, grid), grid, start, end)
                    
                    if found:
                        stats_text = f"A* - Chemin trouvé!\nNœuds explorés: {nodes}\nLongueur: {path_len}\nTemps: {time_taken:.4f}s"
                        print(f"✓ Chemin trouvé! Nœuds: {nodes}, Longueur: {path_len}, Temps: {time_taken:.4f}s")
                    else:
                        stats_text = "A* - Aucun chemin trouvé"
                        print("✗ Aucun chemin trouvé")
                
                # Comparer tous les algorithmes
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    print("\n" + "=" * 60)
                    print("COMPARAISON DES ALGORITHMES")
                    print("=" * 60)
                    
                    results = []
                    
                    # BFS
                    reset_grid_colors(grid, start, end)
                    found, nodes, path_len, time_taken = bfs(lambda: draw(win, grid), grid, start, end)
                    results.append(("BFS", found, nodes, path_len, time_taken))
                    print(f"BFS: Nœuds={nodes}, Longueur={path_len}, Temps={time_taken:.4f}s")
                    pygame.time.wait(1000)
                    
                    # DFS
                    reset_grid_colors(grid, start, end)
                    found, nodes, path_len, time_taken = dfs(lambda: draw(win, grid), grid, start, end)
                    results.append(("DFS", found, nodes, path_len, time_taken))
                    print(f"DFS: Nœuds={nodes}, Longueur={path_len}, Temps={time_taken:.4f}s")
                    pygame.time.wait(1000)
                    
                    # A*
                    reset_grid_colors(grid, start, end)
                    found, nodes, path_len, time_taken = astar(lambda: draw(win, grid), grid, start, end)
                    results.append(("A*", found, nodes, path_len, time_taken))
                    print(f"A*: Nœuds={nodes}, Longueur={path_len}, Temps={time_taken:.4f}s")
                    
                    # Afficher le meilleur
                    print("=" * 60)
                    print("RÉSULTATS:")
                    successful = [r for r in results if r[1]]
                    if successful:
                        best_nodes = min(successful, key=lambda x: x[2])
                        best_path = min(successful, key=lambda x: x[3])
                        best_time = min(successful, key=lambda x: x[4])
                        
                        print(f"✓ Moins de nœuds explorés: {best_nodes[0]} ({best_nodes[2]} nœuds)")
                        print(f"✓ Chemin le plus court: {best_path[0]} ({best_path[3]} cases)")
                        print(f"✓ Plus rapide: {best_time[0]} ({best_time[4]:.4f}s)")
                    print("=" * 60)
                    
                    stats_text = "Comparaison terminée! Voir console"
                
                # Créer un labyrinthe
                if event.key == pygame.K_m:
                    create_maze(grid, start, end)
                    print("Labyrinthe créé!")
                
                # Réinitialiser
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid()
                    stats_text = ""
                    print("Grille réinitialisée")
    
    pygame.quit()


if __name__ == "__main__":
    main()

from PIL import Image
from math import sqrt
from random import shuffle, randrange
import os 

class Cell:
    def __init__(self):
        self.left = True
        self.right = True
        self.bottom = True
        self.top = True
        self.visited = False
        self.wall = False

    @property
    def path_count(self):
        c = 0
        if not self.left:
            c += 1
        if not self.right:
            c += 1
        if not self.bottom:
            c += 1
        if not self.top:
            c += 1
        return c

def euclidian_distance(x1,y1,x2,y2):
    return sqrt((x2-x1) ** 2 + (y2-y1) ** 2)

def manhattan_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def get_neighbors_wo_wall(x,y, grid):
    p = []
    if x > 0:
        if not grid[y][x-1].right:
            p.append((x-1, y))
    if y > 0:
        if not grid[y-1][x].top:
            p.append((x, y-1))
    if x < len(grid[0]) - 1:
        if not grid[y][x+1].left:
            p.append((x+1, y))
    if y < len(grid) - 1:
        if not grid[y+1][x].bottom:
            p.append((x, y+1))
    return p

def get_any_neighbors(x,y, grid):
    p = []
    if x > 0:
        p.append((x-1, y))
    if y > 0:
        p.append((x, y-1))
    if x < len(grid[0]) - 1:
        p.append((x+1, y))
    if y < len(grid) - 1:
        p.append((x, y+1))
    return p

def get_neighbors(x,y, grid):
    p = []
    if x > 0:
        p.append((x-1, y))
    if y > 0:
        p.append((x, y-1))
    if x < len(grid[0]) - 1:
        p.append((x+1, y))
    if y < len(grid) - 1:
        p.append((x, y+1))
    p = list(filter(lambda point: not grid[point[1]][point[0]].visited, p))
    return p

def get_neighbors_wall(x,y, grid):
    p = []
    if x > 0:
        p.append((x-1, y))
    if y > 0:
        p.append((x, y-1))
    if x < len(grid[0]) - 1:
        p.append((x+1, y))
    if y < len(grid) - 1:
        p.append((x, y+1))
    p = list(filter(lambda point: grid[point[1]][point[0]].wall, p))
    return p

def get_isolated_neighbor(x,y, grid):
    p = []
    if x > 0:
        p.append((x-1, y))
    if y > 0:
        p.append((x, y-1))
    if x < len(grid[0]) - 1:
        p.append((x+1, y))
    if y < len(grid) - 1:
        p.append((x, y+1))
    p = list(filter(lambda point: grid[point[1]][point[0]].path_count == 0, p))
    return p

def render_grid(grid, filename):
    w = 2*len(grid[0]) + 1
    h = 2*len(grid) + 1
    im = Image.new("L", (w,h))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            cell = grid[i][j]
            x = 2*j + 1
            y = 2*i + 1
            im.putpixel((x,y), 255)
            if not cell.top:
                im.putpixel((x,y-1), 255)
            if not cell.left:
                im.putpixel((x-1,y), 255)
            if not cell.right:
                im.putpixel((x+1,y), 255)
            if not cell.bottom:
                im.putpixel((x,y+1), 255)
            im.putpixel((x+1,y+1), 0)
            im.putpixel((x+1,y-1), 0)
            im.putpixel((x-1,y-1), 0)
            im.putpixel((x-1,y+1), 0)

    im = im.convert("RGB")
    im.putpixel((1,1), (255,0,0))
    im.putpixel((w-2,h-2), (255,0,0))
    im.save(filename, "PNG")

def has_path_to_end(cx, cy, ex, ey, grid, sx, sy):
    visited = [[cell.visited for cell in row] for row in grid]

    q = [(cx, cy)]
    while len(q) > 0:
        (cx, cy) = q.pop(0)
        if cx == ex and cy == ey:
            return True
        for point in get_neighbors(cx,cy, grid):
            px = point[0]
            py = point[1]
            if px == sx and py == sy:
                 continue
            if visited[py][px]:
                continue
            visited[py][px] = True
            q.append(point)

    return False

def has_path_to_end2(cx, cy, ex, ey, grid):
    visited = [[cell.visited for cell in row] for row in grid]

    q = [(cx, cy)]
    while len(q) > 0:
        (cx, cy) = q.pop(0)
        if cx == ex and cy == ey:
            return True
        for point in get_neighbors_wo_wall(cx,cy, grid):
            px = point[0]
            py = point[1]
            if visited[py][px]:
                continue
            visited[py][px] = True
            q.append(point)

    return False

def gen_letter_mazes():
    directory = "letters"
    for filename in os.listdir(directory):
        im = Image.open(f"{directory}/{filename}")
        im = im.convert("L")
        w, h = im.size

        grid = [[Cell() for x in range(w)] for y in range(h)]

        for i in range(h):
            for j in range(w):
                x = j
                y = i
                if not im.getpixel((x, y)):
                    grid[i][j].visited = True
                    grid[i][j].wall = True

        start_x = 0
        start_y = h-1
        grid[start_y][start_x].left = False
        if start_x > 0:
            grid[start_y][start_x - 1].right = False
        while not im.getpixel((start_x,start_y)):
            start_x += 1
            grid[start_y][start_x].left = False
            if start_x > 0:
                grid[start_y][start_x-1].right = False

        end_x = w -1
        end_y  = h - 1

        grid[end_y][end_x].right = False
        if end_x < len(grid[0]) - 1:
            grid[end_y][end_x + 1].left = False
        while not im.getpixel((end_x,end_y)):
            end_x -= 1
            grid[end_y][end_x].right = False
            if end_x < len(grid[0]) - 1:
                grid[end_y][end_x+1].left = False

        current_x = start_x
        current_y = start_y

        while current_x != end_x or current_y != end_y:
            grid[current_y][current_x].visited = True
            farthest_point = None
            farthest_distance = -1
            neighbors = get_neighbors(current_x, current_y, grid)
            for point in neighbors:
                px = point[0]
                py = point[1]
                dist = manhattan_distance(px, py, end_x, end_y)
                if dist > farthest_distance:
                    if not has_path_to_end(px, py, end_x, end_y, grid, current_x, current_y):
                        continue
                    farthest_point = point
                    farthest_distance = dist
            if not farthest_point:
                print("fuck")
                break
            dx = farthest_point[0] - current_x
            dy = farthest_point[1] - current_y
            if dx == 1:
                grid[current_y][current_x].right = False
                grid[farthest_point[1]][farthest_point[0]].left = False
            if dx == -1:
                grid[current_y][current_x].left = False
                grid[farthest_point[1]][farthest_point[0]].right = False
            if dy == 1:
                grid[current_y][current_x].bottom = False
                grid[farthest_point[1]][farthest_point[0]].top = False
            if dy == -1:
                grid[current_y][current_x].top = False
                grid[farthest_point[1]][farthest_point[0]].bottom = False

            current_x = farthest_point[0]
            current_y = farthest_point[1]

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                gen_maze(grid, j, i)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if not has_path_to_end2(cell[0], cell[1], end_x, end_y, grid):
                    n = get_any_neighbors(j, i, grid)
                    shuffle(n)
                    px, py = n[0]
                    dx = px - j
                    dy = py - i
                    if dx == -1:
                        grid[i][j].right = False
                        grid[py][px].left = False
                    if dx == 1:
                        grid[i][j].left = False
                        grid[py][px].right = False
                    if dy == -1:
                        grid[i][j].bottom = False
                        grid[py][px].top = False
                    if dy == 1:
                        grid[i][j].top = False
                        grid[py][px].bottom = False

        render_grid(grid, f"solutions/{filename}")


def gen_maze(grid, sx=0, sy=0):
    d = (0,0)
    stack = [(sx, sy, d)]
    while len(stack) > 0:
        cx, cy, d = stack.pop()
        if not grid[cy][cx].path_count == 0:
            continue
        dx = d[0]
        dy = d[1]
        if d != (0,0):
            px = cx - dx
            py = cy - dy
            if dx == -1:
                grid[cy][cx].right = False
                grid[py][px].left = False
            if dx == 1:
                grid[cy][cx].left = False
                grid[py][px].right = False
            if dy == -1:
                grid[cy][cx].bottom = False
                grid[py][px].top = False
            if dy == 1:
                grid[cy][cx].top = False
                grid[py][px].bottom = False

        neighbors = get_isolated_neighbor(cx, cy, grid)
        shuffle(neighbors)
        for n in neighbors:
            dx = n[0] - cx
            dy = n[1] - cy
            stack.append((n[0], n[1], (dx, dy)))

w = 100
h = 100
grid = [[Cell() for x in range(w)] for y in range(h)]
gen_maze(grid)
render_grid(grid, "map.png")

from PIL import Image
import json

im = Image.open("map.png")
im = im.convert('L')
w, h = im.size

start = (1,1)
end = (h-2, w-2)

def get_directions(i,j):
    dirs = []
    if i > 0 and im.getpixel((i-1, j)):
        dirs.append((-1, 0))
    if j > 0 and im.getpixel((i, j-1)):
        dirs.append((0, -1))
    if i < h - 1 and im.getpixel((i+1, j)):
        dirs.append((1, 0))
    if j < w - 1 and im.getpixel((i, j+1)):
        dirs.append((0, 1))
    return dirs

def solve():
    q = [start]
    visited = [[False for j in range(w)] for i in range(h)]
    path_grid = [[None for j in range(w)] for i in range(h)]
    while len(q) > 0:
        p = q.pop(0)
        if p == end:
            break
        for direction in get_directions(p[0], p[1]):
            next_point = (p[0] + direction[0], p[1] + direction[1], p)
            if visited[next_point[0]][next_point[1]]:
                continue
            path_grid[next_point[0]][next_point[1]] = next_point
            q.append(next_point)
        visited[p[0]][p[1]] = True

    path = [path_grid[end[0]][end[1]]]
    while True:
        try:
            i,j, prev = path[-1]
            path.append(prev)
        except:
            break

    path.reverse()
    # im2 = im.convert('RGB')
    # for p in path:
    #     im2.putpixel((p[0], p[1]), (255,0,0))

    # im2.save("path.png")
    return path

def get_solution():
    path = solve()
    output = []
    for i in range(len(path) - 1):
        p = path[i]
        n = path[i+1]

        x = (p[0]-n[0], p[1]-n[1])
        if x == (-1, 0):
            output.append("right")
        if x == (1, 0):
            output.append("left")
        if x == (0, -1):
            output.append("down")
        if x == (0, 1):
            output.append("up")
    return output

def render_solution():
    directions = get_solution()
    im_solution = im.convert("RGB")
    x = 1
    y = 1
    while len(directions) > 0:
        im_solution.putpixel((x,y), (255,0,0))
        d = directions.pop(0)
        if d == "left":
            x -= 1
        if d == "right":
            x += 1
        if d == "up":
            y -= 1
        if d == "down":
            y += 1
    im_solution.putpixel((w-2,h-2), (255,0,0))

    im_solution.save("solution.png")



if __name__ == "__main__":
    solution = get_solution()
    print(json.dumps(solution))

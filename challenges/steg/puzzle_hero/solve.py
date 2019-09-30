from PIL import Image
import numpy as np
import os
import pygame
import sys
from random import randrange

class Piece:
    def __init__(self, image, filename, sides):
        self.image = image
        self.filename = filename
        self.sides = sides
        # for color proximity
        self.top_line = image.crop((24,24,173,25))
        self.right_line = image.crop((173,24,174,123))
        self.bottom_line = image.crop((24,123,173,124))
        self.left_line = image.crop((24,24,25,123))
    @property
    def top(self):
        return self.sides[0]
    @property
    def right(self):
        return self.sides[1]
    @property
    def bottom(self):
        return self.sides[2]
    @property
    def left(self):
        return self.sides[3]

    def color_distance(self, top_piece, left_piece):
        distance = 0
        if top_piece:
            width, _ = self.top_line.size
            for x in range(width):
                r,g,b,a = self.top_line.getpixel((x, 0))
                r2,g2,b2,a2 = top_piece.bottom_line.getpixel((x, 0))
                distance += abs(r-r2)
                distance += abs(g-g2)
                distance += abs(b-b2)
        if left_piece:
            _, height = self.left_line.size
            for y in range(height):
                r,g,b,a = self.left_line.getpixel((0, y))
                r2,g2,b2,a2 = left_piece.right_line.getpixel((0, y))
                distance += abs(r-r2)
                distance += abs(g-g2)
                distance += abs(b-b2)

        return distance


markers = { # x,y
    "male_top" : (100,10),
    "male_left" : (12, 74),
    "male_bottom" : (101, 134),
    "male_right" : (183, 69),
    "female_top" : (99, 31),
    "female_left" : (37, 71),
    "female_bottom" : (100, 109),
    "female_right" : (159, 72)
}
side_types = {
    "FLAT": 0,
    "FEMALE": 1,
    "MALE": 2
}

pieces = []
width = 20
height = 20
grid = [[None for j in range(width)] for i in range(height)]

for file in os.listdir("pieces"):
    im = Image.open(f"pieces/{file}")
    sides = [None, None, None, None] # top-right-bottom-left

    # good enough
    is_male_top = im.getpixel(markers["male_top"])[3] == 255
    is_male_left = im.getpixel(markers["male_left"])[3] == 255
    is_male_bottom = im.getpixel(markers["male_bottom"])[3] == 255
    is_male_right = im.getpixel(markers["male_right"])[3] == 255

    is_female_top = im.getpixel(markers["female_top"])[3] == 0
    is_female_left = im.getpixel(markers["female_left"])[3] == 0
    is_female_bottom = im.getpixel(markers["female_bottom"])[3] == 0
    is_female_right = im.getpixel(markers["female_right"])[3] == 0

    if is_male_top:
        sides[0] = side_types["MALE"]
    elif is_female_top:
        sides[0] = side_types["FEMALE"]
    else:
        sides[0] = side_types["FLAT"]

    if is_male_right:
        sides[1] = side_types["MALE"]
    elif is_female_right:
        sides[1] = side_types["FEMALE"]
    else:
        sides[1] = side_types["FLAT"]

    if is_male_bottom:
        sides[2] = side_types["MALE"]
    elif is_female_bottom:
        sides[2] = side_types["FEMALE"]
    else:
        sides[2] = side_types["FLAT"]

    if is_male_left:
        sides[3] = side_types["MALE"]
    elif is_female_left:
        sides[3] = side_types["FEMALE"]
    else:
        sides[3] = side_types["FLAT"]

    piece = Piece(im, file, sides)
    pieces.append(piece)

def pieces_that_fit(i, j):
    fitting = []
    for piece in pieces:
        if i == 0:
            if piece.top != side_types["FLAT"]:
                continue
        elif grid[i-1][j]:
            if piece.top != opposite(grid[i-1][j].bottom):
                continue
        else:
            if piece.top == side_types["FLAT"]:
                continue

        if j == 0:
            if piece.left != side_types["FLAT"]:
                continue
        elif grid[i][j-1]:
            if piece.left != opposite(grid[i][j-1].right):
                continue
        else:
            if piece.left == side_types["FLAT"]:
                continue

        if i == height - 1:
            if piece.bottom != side_types["FLAT"]:
                continue
        else:
            if piece.bottom == side_types["FLAT"]:
                continue

        if j == width - 1:
            if piece.right != side_types["FLAT"]:
                continue
        else:
            if piece.right == side_types["FLAT"]:
                continue
        fitting.append(piece)
    top = None
    left = None
    if i > 0:
        top = grid[i-1][j]
    if j > 0:
        left = grid[i][j-1]
    fitting = list(map(lambda x: (x, x.color_distance(top, left)), fitting))
    fitting.sort(key=lambda x: x[1])
    return fitting

def opposite(side_type):
    if side_type == side_types["MALE"]:
        return side_types["FEMALE"]
    if side_type == side_types["FEMALE"]:
        return side_types["MALE"]
    raise Exception("No opposite for given side type")

ret = 0
def solve_backtrack():
    global ret
    for i, j in np.ndindex((width,height)):
        if not grid[i][j]:
            fitting = pieces_that_fit(i,j)
            if not fitting:
                return False
            print(f"{len(fitting)} fitting pieces found.")
            distances = list(map(lambda x: x[1], fitting))
            print(f"Distances: {distances}")
            for piece, _ in fitting:
                grid[i][j] = piece
                pieces.remove(piece)
                print("Press Enter to accept piece, n to try next piece, an integer i to remove i pieces")
                show_grid()
                inp = input()
                solved = False
                if inp == "":
                    solved = solve_backtrack()
                elif inp != "n":
                    ret = int(inp)
                pieces.append(piece)
                if solved:
                    print("Solution found! Please enter how many pieces to remove, or press enter to accept solution.")
                    show_grid()
                    inp = input()
                    if inp == "":
                        save_solved()
                        sys.exit()
                    ret = int(inp)
                grid[i][j] = None
                if ret != 0:
                    ret -= 1
                    return False
            return False
    return True

def save_solved():
    im = Image.new("RGBA", (3100,2100))

    piece_width = 150
    piece_height = 100
    cnt = save_solved.cnt
    for i, row in enumerate(grid):
        for j, piece in enumerate(row):
            im.paste(piece.image, (piece_width*j, piece_height*i), piece.image)
    im.save(f"solutions/solved_{cnt}.png")
    print(f"Solution n.{cnt} saved!")
    save_solved.cnt += 1
save_solved.cnt = 0

def show_grid():
    im = Image.new("RGBA", (3100,2100))

    piece_width = 150
    piece_height = 100
    for i, row in enumerate(grid):
        for j, piece in enumerate(row):
            if piece:
                im.paste(piece.image, (piece_width*j, piece_height*i), piece.image)
    im.thumbnail((1920, 1080))
    mode = im.mode
    size = im.size
    data = im.tobytes()
    this_image = pygame.image.fromstring(data,size,mode)
    gameDisplay.fill((0,0,0))
    gameDisplay.blit(this_image, (0,0))
    pygame.display.update()



print("Starting Puzzle solver!")
pygame.init()
display_width = 1920
display_height = 1080

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('puzzle viewer')
solve_backtrack()

from PIL import Image, ImageDraw
import numpy as np
from random import randrange
import uuid

class Board:
    WIDTH = 20
    HEIGHT = 20

    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.pix = np.array(self.image)
        self.pixel_height, self.pixel_width, _ = self.pix.shape
        h, w, _ = self.pix.shape
        if w % self.WIDTH != 0 or h % self.HEIGHT != 0:
            raise Exception("Image dimensions are not a multiple of board dimensions")

        self.piece_width = w // self.WIDTH
        self.piece_height = h // self.HEIGHT
        Piece.resize_handle((self.piece_width//2, self.piece_height//2))
        self.board = self.init_board()

    def init_board(self):
        board = []

        for i in range(self.WIDTH):
            row = []
            for j in range(self.HEIGHT):
                origin_x = j * self.piece_width
                origin_y = i * self.piece_height
                region = self.image.crop((origin_x, origin_y, origin_x+self.piece_width, origin_y+self.piece_height))
                row.append(Piece(region))
            board.append(row)

        for i, row in enumerate(board):
            for j, piece in enumerate(row):
                if j < len(row) - 1:
                    right = randrange(1,3)
                    piece.set_side(1, right)
                    row[j+1].set_opposite_side(1, right)

                if i < len(board)-1:
                    down = randrange(1,3)
                    piece.set_side(2, down)
                    board[i+1][j].set_opposite_side(2, down)
        return board

    def generate_image(self):
        im = Image.new("RGBA", (self.pixel_width, self.pixel_height))
        draw = ImageDraw.Draw(im)
        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                origin_x = j * self.piece_width
                origin_y = i * self.piece_height
                region = piece.image_region
                im.paste(region, (origin_x, origin_y))
                draw.rectangle((origin_x, origin_y, origin_x+self.piece_width, origin_y+self.piece_height), outline=(255,0 ,0))

        im.save("board.png")

    def generate_pieces(self):
        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                origin_x = j * self.piece_width
                origin_y = i * self.piece_height
                mask = piece.generate_mask()
                im = Image.new("RGBA", mask.size)
                w,h = mask.size
                left_offset = (w - self.piece_width) // 2
                top_offset = (h - self.piece_height) // 2
                mask_origin_x = origin_x - left_offset
                mask_origin_y = origin_y - top_offset
                region = self.image.crop((mask_origin_x, mask_origin_y, mask_origin_x + w, mask_origin_y + h))
                im.paste(region, mask=mask)
                random_name = uuid.uuid4().hex
                im.save(f"pieces/{random_name}.png")



class Piece:
    SIDE_TYPES = {
        "FLAT": 0,
        "FEMALE": 1,
        "MALE": 2
    }
    HANDLE_MASK = Image.open("mask.png") # TODO resize this dude in proportion to piece size
    HANDLE_MASK_90 = HANDLE_MASK.rotate(90, expand=1)
    HANDLE_MASK_180 = HANDLE_MASK.rotate(180, expand=1)
    HANDLE_MASK_270 = HANDLE_MASK.rotate(270, expand=1)

    HANDLE_MASK_2 = Image.open("mask2.png")
    HANDLE_MASK_2_90 = HANDLE_MASK_2.rotate(90, expand=1)
    HANDLE_MASK_2_180 = HANDLE_MASK_2.rotate(180, expand=1)
    HANDLE_MASK_2_270 = HANDLE_MASK_2.rotate(270, expand=1)

    def __init__(self, image_region):
        self.sides = [self.SIDE_TYPES["FLAT"] for _ in range(4)] # top-right-down-left
        self.image_region = image_region

    @staticmethod
    def resize_handle(size):
        Piece.HANDLE_MASK.thumbnail(size)
        Piece.HANDLE_MASK_90 = Piece.HANDLE_MASK.rotate(90, expand=1)
        Piece.HANDLE_MASK_180 = Piece.HANDLE_MASK.rotate(180, expand=1)
        Piece.HANDLE_MASK_270 = Piece.HANDLE_MASK.rotate(270, expand=1)

        Piece.HANDLE_MASK_2.thumbnail(size)
        Piece.HANDLE_MASK_2_90 = Piece.HANDLE_MASK_2.rotate(90, expand=1)
        Piece.HANDLE_MASK_2_180 = Piece.HANDLE_MASK_2.rotate(180, expand=1)
        Piece.HANDLE_MASK_2_270 = Piece.HANDLE_MASK_2.rotate(270, expand=1)

    def set_side(self, side, side_type):
        self.sides[side] = side_type

    def  set_opposite_side(self, side, side_type):
        side = (side + 2) % 4
        if side_type == self.SIDE_TYPES["MALE"]:
            side_type = self.SIDE_TYPES["FEMALE"]
        elif side_type == self.SIDE_TYPES["FEMALE"]:
            side_type = self.SIDE_TYPES["MALE"]

        self.set_side(side, side_type)

    def generate_mask(self):
        w,h = self.image_region.size
        handle_width, handle_height = self.HANDLE_MASK.size
        mask_width, mask_height = w+2*handle_width, h+2*handle_width
        left_offset = handle_width
        top_offset = handle_width
        piece_mask = Image.new("RGBA", (mask_width, mask_height))
        draw = ImageDraw.Draw(piece_mask)
        draw.rectangle((left_offset, top_offset, left_offset+w-1, top_offset+h-1), (255,255,255))

        if self.sides[0] == self.SIDE_TYPES["MALE"]:
            left = left_offset + (w-handle_height) // 2
            top = 0
            piece_mask.paste(self.HANDLE_MASK_90, (left,top))
        if self.sides[1] == self.SIDE_TYPES["MALE"]:
            top_handle_offset = top_offset + ((h-handle_height) // 2)
            left_handle_offset = left_offset + w
            piece_mask.paste(self.HANDLE_MASK, (left_handle_offset, top_handle_offset))
        if self.sides[2] == self.SIDE_TYPES["MALE"]:
            left = left_offset + (w-handle_height) // 2
            top = top_offset + h
            piece_mask.paste(self.HANDLE_MASK_270, (left,top))
        if self.sides[3] == self.SIDE_TYPES["MALE"]:
            left = 0
            top = top_offset + ((h-handle_height) // 2)
            piece_mask.paste(self.HANDLE_MASK_180, (left,top))

        if self.sides[0] == self.SIDE_TYPES["FEMALE"]:
            left = left_offset + (w-handle_height) // 2
            top = top_offset
            piece_mask.paste(self.HANDLE_MASK_2_270, (left,top))
        if self.sides[1] == self.SIDE_TYPES["FEMALE"]:
            left = left_offset + w - handle_width
            top = top_offset + ((h-handle_height) // 2)
            piece_mask.paste(self.HANDLE_MASK_2_180, (left,top))
        if self.sides[2] == self.SIDE_TYPES["FEMALE"]:
            left = left_offset + (w-handle_height) // 2
            top = top_offset + h - handle_width
            piece_mask.paste(self.HANDLE_MASK_2_90, (left,top))
        if self.sides[3] == self.SIDE_TYPES["FEMALE"]:
            top_handle_offset = top_offset + ((h-handle_height) // 2)
            left_handle_offset = left_offset
            piece_mask.paste(self.HANDLE_MASK_2, (left_handle_offset, top_handle_offset))
        return piece_mask


if __name__ == "__main__":
    board = Board("stego.png")
    board.generate_pieces()

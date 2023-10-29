# tetrispiece.py
import pygame
from random import randrange

pieces = [
    # 3x3 T piece - Index 0
    [
        [ 0, 1, 0 ],
        [ 1, 1, 1 ],
        [ 0, 0, 0 ]
    ],
    # 2x2 O (Square) piece - Index 1
    [
        [ 1, 1 ],
        [ 1, 1 ]
    ],
    # 3x3 S piece - Index 2
    [
        [ 0, 1, 1],
        [ 1, 1, 0],
        [ 0, 0, 0]
    ],
    # 3x3 Z piece - Index 3
    [
        [ 1, 1, 0],
        [ 0, 1, 1],
        [ 0, 0, 0]
    ],
    # 3x3 L piece - Index 4
    [
        [ 1, 0, 0],
        [ 1, 0, 0],
        [ 1, 1, 0]
    ],
    # 3x3 J piece (Reverse L) - Index 5
    [
        [ 0, 0, 1],
        [ 0, 0, 1],
        [ 0, 1, 1]
    ],
    # 4x3 I piece - Index 6
    [
        [ 0, 1, 0],
        [ 0, 1, 0],
        [ 0, 1, 0],
        [ 0, 1, 0]
    ],
]

# Set RGB Colours for each of the pieces
piece_colours = [(128, 0, 128), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 165, 0), (255, 0, 0)]
black_colour  = (0, 0, 0) # Black RGB Colour
grey_colour   = (169, 169, 169) # Grey RGB Colour
white_colour  = (255, 255, 255) # White RGB Colour

blocksize = 30
bevel_size = 1
grid_width = 10 * blocksize
grid_height = 20 * blocksize

screen_width = 800
screen_height = 700
grid_top_left_x = (screen_width - grid_width) // 2
grid_top_left_y = (screen_height - grid_height)

class Piece(object):
    # def __init__(self, x_pos=grid_top_left_x + grid_width / 2 - blocksize / 2, y_pos=grid_top_left_y + 0):
    def __init__(self, x_pos=grid_width / 2 - blocksize / 2, y_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.prev_pos = None
         # Assign a random piece list index for the list of 7 pieces
        self.piece_index = randrange(7)
        self.shape = pieces[self.piece_index]
        self.colour = piece_colours[self.piece_index]
        # Calculate width & height of allocated piece
        self.piece_width = self.get_piece_width()
        self.piece_height = self.get_piece_height()
        # Create a surface to replace background when moving 
        self.backup = pygame.Surface((self.piece_width, self.piece_height))

    def get_piece_width(self):
        return blocksize * len(self.shape[0])
    
    def get_piece_height(self):
        return blocksize * len(self.shape)

    def rotate(self):
        # Rotate lists 90 degrees
        self.shape = list(zip(*reversed(self.shape)))
        # Recalculate width & height of allocated piece
        self.piece_width = self.get_piece_width()
        self.piece_height = self.get_piece_height()
        return
    
    def move_left(self):
        if self.x_pos > 0:
            self.x_pos = self.x_pos - blocksize
        return
    
    def move_right(self):
        if self.x_pos < grid_width:
            self.x_pos = self.x_pos + blocksize
        return
    
    def move_down(self):
        if self.y_pos < grid_height - (blocksize * 3):
            self.y_pos = self.y_pos + blocksize
        return
    
    def draw(self, screen):
        if self.prev_pos:
            screen.blit(self.backup, self.prev_pos)
        self.prev_pos = (self.x_pos + grid_top_left_x, self.y_pos + grid_top_left_y)
        self.backup.blit(screen, (0, 0), (*self.prev_pos, self.piece_width, self.piece_height))
        # pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10))
        for i, row in enumerate(self.shape):
            for j, col in enumerate(row):
                cell = pygame.Rect( self.x_pos + grid_top_left_x + (i * blocksize),
                                    self.y_pos + grid_top_left_y + (j * blocksize),
                                    blocksize,
                                    blocksize) # X Pos, Y Pos, Width, Height
                if col == 1:
                    pygame.draw.rect(screen, self.colour, cell)
                    pygame.draw.rect(screen, black_colour, cell, bevel_size)
                else:
                    pygame.draw.rect(screen, grey_colour, cell)

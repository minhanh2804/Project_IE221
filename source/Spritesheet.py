import pygame as pg

class Spritesheet:
    """This class make the regulation for loading image as a basic object class"""
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        """The purpose when create this function is breaking up image into small components (shots) by coordinate"""
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))

        return image

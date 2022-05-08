import pygame as pg
from source import Game
game = Game.Game()

while game.running:
    game.run()

pg.quit()

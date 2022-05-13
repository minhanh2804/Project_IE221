import pygame as pg

WIDTH = 640
HEIGHT = 480
VALUE_MAX = 255

class Shot(pg.sprite.Sprite):          # Shot Class
    """
        This class is designed to manage the shot operation (color, mode, direction, speed)
    """
    def __init__(self, game, color, mode, direction, speed):      #color(WBDR) mode(DRUL) direction(DRUL)
        """This function initializes variables for operating process"""
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.color = color
        self.mode = mode
        self.direction = direction
        self.speed = speed
        self.alpha = VALUE_MAX
        self.correct_code = [1, 2, 3, 4]
        self.correct = 0
        image = self.game.spr_shot.get_image((color - 1) * 45, 0, 45, 61)

        if self.mode == 0:
            self.image = pg.transform.rotate(image, 270)
            self.touch_coord = (round(- self.image.get_width() / 2), round(23 - self.image.get_height() / 2))
        elif self.mode == 90:
            self.image = image
            self.touch_coord = (round(23 - self.image.get_width() / 2), round(- self.image.get_height() / 2))
        elif self.mode == 180:
            self.image = pg.transform.rotate(image, 90)
            self.touch_coord = (round(- self.image.get_width() / 2), round(-23 - self.image.get_height() / 2))
        else:
            self.image = pg.transform.rotate(image, 180)
            self.touch_coord = (round(-23 - self.image.get_width() / 2), round(- self.image.get_height() / 2))

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = round(WIDTH  / 2), round(HEIGHT / 2)

        if self.direction == 0:
            self.rect.y += round(WIDTH / 2 + 100)
        elif self.direction == 90:
            self.rect.x += round(WIDTH / 2 + 100)
        elif self.direction == 180:
            self.rect.y -= round(WIDTH / 2 + 100)
        else:
            self.rect.x -= round(WIDTH / 2 + 100)

        self.rect.x += self.touch_coord[0]
        self.rect.y += self.touch_coord[1]

    def update(self):
        """
            This function is used for updating the shot status when the screen value has changed.
            Moreover it responds for play the animation sound of shot when user playing
        """
        self.image.set_alpha(self.alpha)

        if self.alpha > 0:
            if self.correct == 1:
                self.alpha -= VALUE_MAX / 5
            else:
                if self.correct == -1:
                    self.alpha -= VALUE_MAX / 85

                if self.direction == 0:
                    self.rect.y -= self.speed
                elif self.direction == 90:
                    self.rect.x -= self.speed
                elif self.direction == 180:
                    self.rect.y += self.speed
                else:
                    self.rect.x += self.speed

            if self.rect.x > WIDTH * 2 or self.rect.x < -WIDTH or self.rect.y > HEIGHT * 2 or self.rect.y < -HEIGHT:
                self.kill()
        else:
            self.kill()

        if self.correct == 0 and self.rect.x == round(WIDTH / 2) + self.touch_coord[0] and self.rect.y == round(HEIGHT / 2) + self.touch_coord[1]:
            if self.game.circle_dir == self.correct_code[round(self.mode / 90 - self.color + 1)]:
                self.game.score += 100
                self.correct = 1

                if self.color == 1:
                    self.game.sound_drum1.play()
                elif self.color == 2:
                    self.game.sound_drum2.play()
                elif self.color == 3:
                    self.game.sound_drum3.play()
                else:
                    self.game.sound_drum4.play()
            else:
                self.correct = -1

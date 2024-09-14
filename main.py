import pygame
from time import sleep

pygame.init()

ENDGAME = False
TIMER = 400
TIMER_cn = 0
width = 800
height = 600
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load("images/LUCK_BLOCK1.png"))
pygame.display.set_caption("Super Mario Copy")
pygame.mixer.init()

FONT = pygame.font.Font("images/Super_Mario_Font.ttf", 25)

soundJUMP = pygame.mixer.Sound("sounds/soundJUMP_small.ogg")
soundJUMP.set_volume(0.2)
soundLEVEL01 = pygame.mixer.Sound("sounds/soundLEVEL01.ogg")
soundLEVEL01.set_volume(0.3)
soundPAUSE = pygame.mixer.Sound("sounds/soundPAUSE.ogg")
soundPAUSE.set_volume(0.5)
soundMENU = pygame.mixer.Sound("sounds/soundMENU.ogg")
soundMENU.set_volume(0.3)
soundCOIN = pygame.mixer.Sound("sounds/soundCOINtake.ogg")
soundCOIN.set_volume(0.3)
soundDEAD = pygame.mixer.Sound("sounds/soundDEAD.ogg")
soundDEAD.set_volume(0.5)
soundHIT = pygame.mixer.Sound("sounds/soundHIT.ogg")
soundHIT.set_volume(0.5)
soundBLOCK = pygame.mixer.Sound("sounds/soundBLOCKbreak.ogg")
soundBLOCK.set_volume(0.5)
soundWIN = pygame.mixer.Sound("sounds/soundLEVELfinish.ogg")
soundWIN.set_volume(0.5)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, w, h, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Text:
    def __init__(self, text, font_size, font_color, position, font_name):
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.position = position
        self.font_name = font_name
        self.font = font_name
        self.rendered_text = self.font.render(self.text, True, self.font_color)
        self.rect = self.rendered_text.get_rect(topleft=self.position)

    def draw(self, screen):
        screen.blit(self.rendered_text, self.rect)

    def update_text(self, new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, self.font_color)
        self.rect = self.rendered_text.get_rect(topleft=self.position)


class LuckBlock(GameSprite):
    def __init__(self, x, y, loot_type, coin):
        super().__init__("images/LUCK_BLOCK1.png", x, y, 40, 40, 0)
        self.image = pygame.transform.scale(pygame.image.load("images/LUCK_BLOCK1.png"), (40, 40))
        self.rect.x = x
        self.rect.y = y
        self.block_count = 0
        self.loot_type = loot_type
        self.isLoot = True
        self.wantLoot = False
        self.coin_animation = False
        self.COIN = coin

    def working(self, luigi):
        if self.isLoot:
            self.block_count += 1
            if 20 > self.block_count >= 0:
                self.image = pygame.transform.scale(pygame.image.load("images/LUCK_BLOCK1.png"), (40, 40))
            if 30 > self.block_count >= 20:
                self.image = pygame.transform.scale(pygame.image.load("images/LUCK_BLOCK2.png"), (40, 40))
            if 40 > self.block_count >= 30:
                self.image = pygame.transform.scale(pygame.image.load("images/LUCK_BLOCK3.png"), (40, 40))
            if self.block_count > 40:
                self.block_count = 0

        if not self.isLoot:
            self.image = pygame.transform.scale(pygame.image.load("images/LUCK_BLOCK_used.png"), (40, 40))

        if self.wantLoot:
            if self.isLoot:
                if self.loot_type == "coin":
                    soundCOIN.play()
                    luigi.coins += 1
                    luigi.score += 200
                    self.block_count = 0
                    self.coin_animation = True
                    self.wantLoot = False
                    self.isLoot = False

        if self.coin_animation:
            if self.block_count == 0:
                self.COIN.rect.x = self.rect.x
                self.COIN.rect.y = self.rect.y - 152.5
            self.block_count += 1
            if 3 > self.block_count >= 0:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN1.png"), (40, 152.5))
            if 6 > self.block_count >= 3:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN2.png"), (40, 152.5))
            if 9 > self.block_count >= 6:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN3.png"), (40, 152.5))
            if 12 > self.block_count >= 9:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN4.png"), (40, 152.5))
            if 15 > self.block_count >= 12:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN5.png"), (40, 152.5))
            if 18 > self.block_count >= 15:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN6.png"), (40, 152.5))
            if 21 > self.block_count >= 18:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN7.png"), (40, 152.5))
            if 24 > self.block_count >= 21:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN8.png"), (40, 152.5))
            if 27 > self.block_count >= 24:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN7.png"), (40, 152.5))
            if 30 > self.block_count >= 27:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN6.png"), (40, 152.5))
            if 33 > self.block_count >= 30:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN5.png"), (40, 152.5))
            if 36 > self.block_count >= 33:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN4.png"), (40, 152.5))
            if 39 > self.block_count >= 36:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN3.png"), (40, 152.5))
            if 42 > self.block_count >= 39:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN2.png"), (40, 152.5))
            if 45 > self.block_count >= 42:
                self.COIN.image = pygame.transform.scale(pygame.image.load("images/COIN1.png"), (40, 152.5))
            if self.block_count > 45:
                self.coin_animation = False
                self.block_count = 0
                self.COIN.rect.x = -100


class Block(GameSprite):
    def __init__(self, x, y):
        super().__init__("images/D_BLOCK.png", x, y, 40, 40, 0)
        self.image = pygame.transform.scale(pygame.image.load("images/D_BLOCK.png"), (40, 40))
        self.rect.x = x
        self.rect.y = y
        self.block_count = 0
        self.wantLoot = False


class Enemy(GameSprite):
    def __init__(self, x, y, start_side):
        super().__init__("images/GRYB_wolking1.png", x, y, 40, 40, 0)
        self.rect.x = x
        self.rect.y = y
        self.live = True
        self.side = start_side
        self.enemy_count = 0
        self.dead_start = False
        self.delete = False

    def wolking(self, collision_list, luigi):
        if self.live:
            self.enemy_gravity(collision_list)
            if self.dead_start:
                self.dead(luigi)
            if self.side == "right":
                if not self.enemy_check(self.rect.x + 2, self.rect.y, collision_list):
                    self.enemy_count += 1

                    if not self.hero_check(self.rect.x + 2, self.rect.y, luigi):
                        self.rect.x += 2
                    if self.hero_check(self.rect.x + 2, self.rect.y, luigi):
                        self.rect.x += 2
                        if not luigi.itfall:
                            if not self.dead_start:
                                luigi.live = False
                        if luigi.itfall:
                            self.dead_start = True

                    if 10 > self.enemy_count >= 0:
                        self.image = pygame.transform.scale(pygame.image.load("images/GRYB_wolking1.png"), (40, 40))
                    if 20 > self.enemy_count >= 10:
                        self.image = pygame.transform.scale(pygame.image.load("images/GRYB_wolking2.png"), (40, 40))
                    if self.enemy_count > 20:
                        self.enemy_count = 0

                if self.enemy_check(self.rect.x + 2, self.rect.y, collision_list):
                    self.side = "left"

            if self.side == "left":
                if not self.enemy_check(self.rect.x - 2, self.rect.y, collision_list):
                    self.enemy_count += 1

                    if not self.hero_check(self.rect.x - 2, self.rect.y, luigi):
                        self.rect.x -= 2
                    if self.hero_check(self.rect.x - 2, self.rect.y, luigi):
                        self.rect.x -= 4
                        if not luigi.itfall:
                            if not self.dead_start:
                                luigi.live = False
                        if luigi.itfall:
                            self.dead_start = True
                    if 10 > self.enemy_count >= 0:
                        self.image = pygame.transform.scale(pygame.image.load("images/GRYB_wolking1.png"), (40, 40))
                    if 20 > self.enemy_count >= 10:
                        self.image = pygame.transform.scale(pygame.image.load("images/GRYB_wolking2.png"), (40, 40))
                    if self.enemy_count > 20:
                        self.enemy_count = 0

                if self.enemy_check(self.rect.x - 2, self.rect.y, collision_list):
                    self.side = "right"

        if not self.live:
            self.enemy_count += 1
            if self.enemy_count < 20:
                self.image = pygame.transform.scale(pygame.image.load("images/GRYB_KAPEZ.png"), (40, 40))
                luigi.rect.y -= 10
            if self.enemy_count > 20:
                self.delete = True

    def hero_check(self, x, y,  luigi):
        hero_touch = []
        tmp_area = pygame.Rect(x, y, self.w, self.h)
        luigi.reset()
        luigi_rect = luigi.rect
        hero_touch.append(luigi_rect.colliderect(tmp_area))

        return True in hero_touch

    def enemy_check(self, x, y,  collision_list):
        object_touch = []
        tmp_area = pygame.Rect(x, y, self.w, self.h)
        for collision in collision_list:
            collision_rect = collision.rect
            object_touch.append(collision_rect.colliderect(tmp_area))

        return True in object_touch

    def enemy_gravity(self, collision_list):
        if not self.enemy_check(self.rect.x, self.rect.y + 8, collision_list):
            self.rect.y += 8
        if self.enemy_check(self.rect.x, self.rect.y + 8, collision_list):
            if not self.enemy_check(self.rect.x, self.rect.y + 2, collision_list):
                self.rect.y += 2
            if self.enemy_check(self.rect.x, self.rect.y + 2, collision_list):
                pass

    def dead(self, luigi):
        soundHIT.play()
        luigi.score += 100
        self.enemy_count = 0
        self.live = False


class Hero(GameSprite):
    def __init__(self, filename, x, y, w, h, speed):
        GameSprite.__init__(self, filename, x, y, w, h, speed)
        self.counter = 0
        self.itrun = False
        self.side = "right"
        self.isJumping = False
        self.jumpCount = 17
        self.jumpDel = 0
        self.itfall = False
        self.health = 3
        self.coins = 0
        self.score = 0
        self.live = True
        self.dead_mus = 0

    def move(self, collision_list, move_list):
        keys = pygame.key.get_pressed()
        if self.jumpDel != 0:
            self.jumpDel -= 1
        if self.jumpDel == 0:
            pass
        if keys[pygame.K_SPACE]:
            if self.jumpDel == 0:
                if not self.itfall:
                    self.isJumping = True
                    self.counter = 0
        if keys[pygame.K_a]:
            self.side = "left"
            if not self.check(self.rect.x - self.speed, self.rect.y, collision_list):
                self.level_scroll(move_list)
                self.animation("go_left")
        if keys[pygame.K_d]:
            self.side = "right"
            if not self.check(self.rect.x + self.speed, self.rect.y, collision_list):
                self.level_scroll(move_list)
                self.animation("go_right")
        if keys[pygame.K_LSHIFT]:
            self.speed = 6
            self.itrun = True
        elif not keys[pygame.K_LSHIFT]:
            self.speed = 4
            self.itrun = False

        if not any(keys):
            self.counter = 0
            if self.side == "right":
                self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_STOP_right.png"), (30, 40))
            elif self.side == "left":
                self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_STOP_left.png"), (30, 40))

        if self.isJumping:
            if self.jumpCount == 17:
                soundJUMP.play()
            self.animation("jump")
            if self.jumpCount > 0:
                if not self.check(self.rect.x, self.rect.y - self.jumpCount, collision_list):
                    self.rect.y -= self.jumpCount
                    self.jumpCount -= 1
                if self.check(self.rect.x, self.rect.y - self.jumpCount, collision_list):
                    self.jumpCount = 0
            if self.jumpCount <= 0:
                if not self.check(self.rect.x, self.rect.y + 8, collision_list):
                    self.rect.y += 8
                    self.itfall = True
                if self.check(self.rect.x, self.rect.y + 8, collision_list):
                    if not self.check(self.rect.x, self.rect.y + 2, collision_list):
                        self.rect.y += 2
                        self.itfall = True
                    if self.check(self.rect.x, self.rect.y + 2, collision_list):
                        self.jumpCount = 17
                        self.itfall = False
                        self.isJumping = False
                        self.jumpDel = 15
                        if self.side == "right":
                            self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_STOP_right.png"), (30, 40))
                        elif self.side == "left":
                            self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_STOP_left.png"), (30, 40))

    def level_scroll(self, move_list):
        if self.side == "left":
            if self.rect.x <= 0:
                pass
            elif self.rect.x > 0:
                self.rect.x -= self.speed
        if self.side == "right":
            if self.rect.x >= 385:
                for mov in move_list:
                    mov.rect.x -= self.speed
            elif self.rect.x < 385:
                self.rect.x += self.speed

    def check(self, x, y,  collision_list):
        object_touch = []
        tmp_area = pygame.Rect(x, y, self.w, self.h)
        for collision in collision_list:
            collision.reset()
            collision_rect = collision.rect
            object_touch.append(collision_rect.colliderect(tmp_area))
            if collision_rect.colliderect(tmp_area):
                if y > collision_rect.y:
                    collision.wantLoot = True

        return True in object_touch

    def animation(self, types):
        if types == "jump":
            if self.side == "right":
                self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_jump_right.png"), (40, 40))
            if self.side == "left":
                self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_jump_left.png"), (40, 40))
        if types == "go_right":
            if not self.itrun:
                self.counter += 1
                if 20 > self.counter >= 0:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_right1.png"), (37.5, 40))
                elif 40 > self.counter >= 20:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_right2.png"), (30, 37.5))
                elif 60 > self.counter >= 40:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_right3.png"), (27.5, 40))
                elif self.counter > 60:
                    self.counter = 0

            if self.itrun:
                self.counter += 1
                if 10 > self.counter >= 0:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_right1.png"), (37.5, 40))
                elif 20 > self.counter >= 10:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_right2.png"), (30, 37.5))
                elif 30 > self.counter >= 20:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_right3.png"), (27.5, 40))
                elif self.counter > 30:
                    self.counter = 0

        if types == "go_left":
            if not self.itrun:
                self.counter += 1
                if 20 > self.counter >= 0:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_left1.png"), (37.5, 40))
                elif 40 > self.counter >= 20:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_left2.png"), (30, 37.5))
                elif 60 > self.counter >= 40:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_left3.png"), (27.5, 40))
                elif self.counter > 60:
                    self.counter = 0

            if self.itrun:
                self.counter += 1
                if 10 > self.counter >= 0:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_left1.png"), (37.5, 40))
                elif 20 > self.counter >= 10:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_left2.png"), (30, 37.5))
                elif 30 > self.counter >= 20:
                    self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_wolk_left3.png"), (27.5, 40))
                elif self.counter > 30:
                    self.counter = 0

    def gravity(self, collision_list):
        if not self.isJumping:
            if not self.check(self.rect.x, self.rect.y + 8, collision_list):
                self.rect.y += 8
                self.animation("jump")
                self.itfall = True
            if self.check(self.rect.x, self.rect.y + 8, collision_list):
                if not self.check(self.rect.x, self.rect.y + 2, collision_list):
                    self.rect.y += 2
                    self.itfall = True
                if self.check(self.rect.x, self.rect.y + 2, collision_list):
                    self.itfall = False
        if self.isJumping:
            pass

    def death_chek(self):
        if not self.live:
            if self.dead_mus == 0:
                soundDEAD.play()
                sleep(0.8)
                self.counter = 0
            self.dead_mus = + 1
            self.image = pygame.transform.scale(pygame.image.load("images/LUIGI_DEATH.png"), (35, 35))
            if self.health > 0:
                self.health -= 1
            if self.health <= 0:
                pass
            self.counter += 1
            if 25 > self.counter >= 0:
                self.rect.y -= 7
            if 100 > self.counter >= 25:
                self.rect.y += 5
            if self.counter > 150:
                pygame.quit()


PAUSE = GameSprite("images/pause.png", 0, 0, 800, 600, 0)
MENU = GameSprite("images/main_menu.png", 0, 0, 800, 600, 0)
LUIGI = Hero("images/LUIGI_STOP_right.png", 80, 440, 30, 40, 4)
EARTH1 = GameSprite("images/earth1.png", 0, 480, 2760, 120, 0)
EARTH2 = GameSprite("images/earth2.png", 2860, 480, 600, 120, 0)
EARTH3 = GameSprite("images/earth3.png", 3610, 480, 2560, 120, 0)
EARTH4 = GameSprite("images/earth4.png", 6270, 480, 2240, 120, 0)
CASTLE = GameSprite("images/CASTLE_final.png", 6270, 280, 200, 200, 0)
CLOUDS = GameSprite("images/CLAUDS.png", 650, 20, 6332.5, 172.5, 0)


def Castle_chek(CASTLE, x, y):
    castle_touch = []
    tmp_area = pygame.Rect(x, y, LUIGI.w, LUIGI.h)
    CASTLE.reset()
    collision_rect = CASTLE.rect
    castle_touch.append(collision_rect.colliderect(tmp_area))

    return True in castle_touch


STAIR_block1 = GameSprite("images/STAIR_BLOCK.png", 6130, 440, 40, 40, 0)
STAIR_block2 = GameSprite("images/STAIR_BLOCK.png", 6130, 400, 40, 40, 0)
STAIR_block3 = GameSprite("images/STAIR_BLOCK.png", 6090, 440, 40, 40, 0)
STAIR_block4 = GameSprite("images/STAIR_BLOCK.png", 5810, 440, 40, 40, 0)
STAIR_block5 = GameSprite("images/STAIR_BLOCK.png", 5810, 400, 40, 40, 0)
STAIR_block6 = GameSprite("images/STAIR_BLOCK.png", 5530, 400, 40, 40, 0)
STAIR_block7 = GameSprite("images/STAIR_BLOCK.png", 5530, 440, 40, 40, 0)
STAIR_block8 = GameSprite("images/STAIR_BLOCK.png", 3610, 440, 40, 40, 0)

coin1 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock1 = LuckBlock(640, 360, "coin", coin1)
coin2 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock2 = LuckBlock(5250, 200, "coin", coin2)
coin3 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock3 = LuckBlock(5210, 200, "coin", coin3)
coin4 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock4 = LuckBlock(4530, 200, "coin", coin4)
coin5 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock5 = LuckBlock(4530, 360, "coin", coin5)
coin6 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock6 = LuckBlock(4410, 360, "coin", coin6)
coin7 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock7 = LuckBlock(4650, 360, "coin", coin7)
coin8 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock8 = LuckBlock(3930, 200, "coin", coin8)
coin9 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock9 = LuckBlock(3140, 360, "coin", coin9)
coin10 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock10 = LuckBlock(840, 360, "coin", coin10)
coin11 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock11 = LuckBlock(920, 360, "coin", coin11)
coin12 = GameSprite("images/COIN1.png", -100, 0, 40, 152.5, 0)
luckBlock12 = LuckBlock(880, 200, "coin", coin12)

TUBE1 = GameSprite("images/Tube_1.png", 1300, 383, 80, 97.5, 0)
TUBE2 = GameSprite("images/Tube_2.png", 1620, 343, 80, 137, 0)
TUBE3 = GameSprite("images/Tube_2.png", 2000, 343, 80, 137, 0)
TUBE4 = GameSprite("images/Tube_2.png", 2420, 343, 80, 137, 0)

D_Block1 = Block(440, 1000)
D_Block2 = Block(5250, 360)
D_Block3 = Block(5210, 360)
D_Block4 = Block(5290, 200)
D_Block5 = Block(5170, 200)
D_Block6 = Block(4210, 360)
D_Block7 = Block(4170, 360)
D_Block8 = Block(3930, 360)
D_Block9 = Block(3100, 360)
D_Block10 = Block(3180, 360)
D_Block11 = Block(800, 360)
D_Block12 = Block(880, 360)
D_Block13 = Block(960, 360)

LOGO = GameSprite("images/LOGO.png", 75, 50, 440, 242.5, 0)

GRYB1 = Enemy(500, 440, "left")                             #Гриби тут
GRYB2 = Enemy(4530, 160, "right")
GRYB3 = Enemy(4210, 320, "left")
GRYB4 = Enemy(1500, 440, "right")
GRYB5 = Enemy(2200, 440, "left")
GRYB6 = Enemy(5700, 440, "right")

SCORE_pc = GameSprite("images/SCORE.png", 25, 5, 130, 23, 0)
COINS_pc = GameSprite("images/COINS_LIK.png", 175, 5, 130, 23, 0)
WORLD_pc = GameSprite("images/WORLD.png", 325, 5, 130, 23, 0)
TIME_pc = GameSprite("images/TIMER.png", 475, 5, 100, 23, 0)
LIVES_pc = GameSprite("images/LIVES.png", 625, 5, 126, 23, 0)

SCORE = Text(f"{LUIGI.score}", 45, (255, 255, 255), (55, 30), FONT)
COINS = Text(f"{LUIGI.coins}", 30, (255, 255, 255), (230, 30), FONT)
TIME = Text(f"{TIMER}", 50, (255, 255, 255), (490, 30), FONT)
LIVES = Text(f"{LUIGI.health}", 30, (255, 255, 255), (675, 30), FONT)
WORLD = Text("1-1", 30, (255, 255, 255), (350, 30), FONT)

text_list = [SCORE, COINS, TIME, LIVES, WORLD]
hud_list = [SCORE_pc, COINS_pc, WORLD_pc, TIME_pc, LIVES_pc]

blocks_list = [D_Block1, D_Block2, D_Block3, D_Block4, D_Block5, D_Block6, D_Block7, D_Block8, D_Block9, D_Block10,
               D_Block11, D_Block12, D_Block13]

move_list = [EARTH1, EARTH2, EARTH3, EARTH4, luckBlock1, LOGO, GRYB1, D_Block1, STAIR_block1, CASTLE, STAIR_block2,
             STAIR_block3, CLOUDS, STAIR_block4, STAIR_block5, STAIR_block6, STAIR_block7, D_Block2, D_Block3,
             D_Block4, D_Block5, luckBlock2, luckBlock3, luckBlock4, luckBlock5, luckBlock6, luckBlock7, D_Block6,
             D_Block7, D_Block8, STAIR_block8, luckBlock8, D_Block9, D_Block10, luckBlock9, D_Block11, D_Block12,
             D_Block13, luckBlock10, luckBlock11, luckBlock12, TUBE1, TUBE2, TUBE3, TUBE4, GRYB4, GRYB2, GRYB3,
             GRYB5, GRYB6, coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12]

collision_list = [EARTH1, EARTH2, EARTH3, EARTH4, luckBlock1, D_Block1, STAIR_block1,
                  STAIR_block2, STAIR_block3, STAIR_block4, STAIR_block5, STAIR_block6, STAIR_block7, D_Block2, D_Block3,
                  D_Block4, D_Block5, luckBlock2, luckBlock3, luckBlock4, luckBlock5, luckBlock6, luckBlock7, D_Block6,
                  D_Block7, D_Block8, STAIR_block8, luckBlock8, D_Block9, D_Block10, luckBlock9, D_Block11, D_Block12,
                  D_Block13, luckBlock10, luckBlock11, luckBlock12, TUBE1, TUBE2, TUBE3, TUBE4]

enemy_collision_list = [TUBE1, TUBE2, TUBE3, TUBE4, STAIR_block4, STAIR_block3, STAIR_block7, STAIR_block8, EARTH1,
                        EARTH2, EARTH3, EARTH4]

ememy_list = [GRYB1, GRYB2, GRYB3, GRYB4, GRYB5, GRYB6]
lucky_blocks = [luckBlock1, luckBlock2, luckBlock3, luckBlock4, luckBlock5, luckBlock6, luckBlock7, luckBlock8,
                luckBlock9, luckBlock10, luckBlock11, luckBlock12]

coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12]

screen = "menu"
fin_mus = 0

soundMENU.play(-1)

game = True
while game:
    if screen == "menu":
        MENU.reset()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if any(keys):
            soundPAUSE.play()
            sleep(0.5)
            soundLEVEL01.play(-1)
            soundMENU.stop()
            screen = "game_lvl01"
        clock.tick(60)
        pygame.display.update()

    if screen == "pause":
        PAUSE.reset()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if any(keys):
            soundPAUSE.play()
            sleep(0.5)
            soundLEVEL01.play(-1)
            soundMENU.stop()
            screen = "game_lvl01"

        clock.tick(60)
        pygame.display.update()

    if screen == "game_lvl01":
        window.fill((92, 148, 252))

        if LUIGI.live:
            CLOUDS.reset()
            LOGO.reset()
            CASTLE.reset()
            LUIGI.reset()

        for luck in lucky_blocks:
           luck.working(LUIGI)

        for coin in coins:
            coin.reset()

        for hud in hud_list:
            hud.reset()

        LUIGI.death_chek()

        for enemy in ememy_list:
            enemy.reset()
            if enemy.delete:
                ememy_list.remove(enemy)
            enemy.wolking(enemy_collision_list, LUIGI)

        for block in blocks_list:
            block.reset()
            if block.wantLoot:
                if block.block_count == 0:
                    soundBLOCK.play()
                block.block_count += 1
                blocks_list.remove(block)
                move_list.remove(block)
                collision_list.remove(block)

        if LUIGI.rect.y > 600:
            LUIGI.live = False
            EARTH1.reset()
            EARTH2.reset()
            EARTH3.reset()
            EARTH4.reset()

        for text in text_list:
            text.draw(window)
            if text == SCORE:
                text.update_text(str(LUIGI.score))
            if text == COINS:
                text.update_text(str(LUIGI.coins))
            if text == TIME:
                text.update_text(str(TIMER))
            if text == LIVES:
                text.update_text(str(LUIGI.health))

        if LUIGI.live and not ENDGAME:
            LUIGI.move(collision_list, move_list)
            LUIGI.gravity(collision_list)
        if not LUIGI.live:
            soundLEVEL01.stop()
            for move in move_list:
                move.reset()
            for hud in hud_list:
                hud.reset()
            for text in text_list:
                text.draw(window)
                if text == SCORE:
                    text.update_text(str(LUIGI.score))
                if text == COINS:
                    text.update_text(str(LUIGI.coins))
                if text == TIME:
                    text.update_text(str(TIMER))
                if text == LIVES:
                    text.update_text(str(LUIGI.health))

        if Castle_chek(EARTH4, LUIGI.rect.x, LUIGI.rect.y + 2):
            ENDGAME = True
            soundLEVEL01.stop()
            if fin_mus == 0:
                soundWIN.play()
            fin_mus += 1
            sleep(5.5)
            pygame.quit()

        TIMER_cn += 1
        if TIMER_cn == 30:
            if TIMER > 0:
                TIMER -= 1
            TIMER_cn = 0
        if TIMER == 100:
            if TIMER_cn == 0:
                soundLEVEL01.stop()
                soundLEVEL01 = pygame.mixer.Sound("sounds/soundLEVEL01lowtime.ogg")
                soundLEVEL01.play()
        if TIMER == 0:
            LUIGI.live = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            screen = "pause"
            soundPAUSE.play()
            sleep(0.5)
            soundLEVEL01.stop()
            soundMENU.play(-1)

        clock.tick(60)

        pygame.display.update()
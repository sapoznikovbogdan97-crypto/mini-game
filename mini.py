import arcade
import random

from pymunk.examples.colors_pyglet_batch import reset

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(arcade.Sprite):
  def __init__(self):
    super().__init__(":resources:/images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
    self.center_x = SCREEN_WIDTH / 2
    self.center_y = SCREEN_HEIGHT / 2
    self.speed = 4

class Enemy(arcade.Sprite):
  # 1 - вправо, -1 - влево
  def __init__(self, player_list, wall_list, x, y, direction = 1):
    super().__init__(":resources:/images/alien/alienBlue_front.png", 0.75)
    self.center_x = x
    self.center_y = y
    self.speed = 2
    self.direction = direction
    self.wall_list = wall_list

  def update(self, delta_time):
    self.center_x += self.speed * self.direction

    hits = arcade.check_for_collision_with_list(self, self.wall_list)
    for wall in hits:
        if self.direction == 1:
            self.direction = -1
        elif self.direction == -1:
            self.direction = 1




class MyGame(arcade.Window):
  def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "мини игра")
    arcade.set_background_color(arcade.color.AMAZON)

    self.player = Player()
    self.player_list = arcade.SpriteList()
    self.player_list.append(self.player)


    self.wall_list = arcade.SpriteList(use_spatial_hash=True)
    self.coins_list = arcade.SpriteList(use_spatial_hash=True)

    self.enemy = Enemy(self.wall_list, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    self.enemy_list = arcade.SpriteList(use_spatial_hash=True)
    self.enemy_list.append(self.enemy)

    self.create_walls()
    self.create_coins()


    self.score = 0

  def create_walls(self):
    walls_position = [
      # снизу
      (SCREEN_WIDTH / 2 - 125, 12.5),
      (SCREEN_WIDTH / 2 - 250, 12.5),
      (25, 12.5),
      (SCREEN_WIDTH / 2, 12.5),
      (SCREEN_WIDTH / 2 + 125, 12.5),
      (SCREEN_WIDTH / 2 + 250, 12.5),
      (SCREEN_WIDTH - 25, 12.5),
      # верх
      (SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT - 12.5),
      (SCREEN_WIDTH / 2 - 250, SCREEN_HEIGHT - 12.5),
      (25, SCREEN_HEIGHT - 12.5),
      (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 12.5),
      (SCREEN_WIDTH / 2 + 125, SCREEN_HEIGHT - 12.5),
      (SCREEN_WIDTH / 2 + 250, SCREEN_HEIGHT - 12.5),
      (SCREEN_WIDTH - 25, SCREEN_HEIGHT - 12.5),
      # слева
      (12.5, SCREEN_HEIGHT / 2 - 125),
      (12.5, SCREEN_HEIGHT / 2 - 250),
      (12.5, SCREEN_HEIGHT / 2),
      (12.5, SCREEN_HEIGHT / 2 + 125),
      (12.5, SCREEN_HEIGHT / 2 + 250),
      # справа
      (SCREEN_WIDTH - 12.5, SCREEN_HEIGHT / 2 - 125),
      (SCREEN_WIDTH - 12.5, SCREEN_HEIGHT / 2 - 250),
      (SCREEN_WIDTH - 12.5, SCREEN_HEIGHT / 2),
      (SCREEN_WIDTH - 12.5, SCREEN_HEIGHT / 2 + 125),
      (SCREEN_WIDTH - 12.5, SCREEN_HEIGHT / 2 + 250),
    ]


    for x, y in walls_position:
      wall = arcade.Sprite(":resources:/images/tiles/boxCrate.png")
      wall.center_x = x
      wall.center_y = y
      self.wall_list.append(wall)

  def create_coins(self):
    coins_position = [(90, 450),
                      (450, 100),
                      (200, 300)]

    for x, y in coins_position:
      coin = arcade.Sprite(":resources:images/items/coinGold.png")
      coin.center_x = x
      coin.center_y = y
      self.coins_list.append(coin)

  def on_draw(self):
    self.clear()
    self.player_list.draw()
    self.wall_list.draw()
    self.coins_list.draw()
    self.enemy_list.draw()

    arcade.draw_text(
      f"Счёт: {self.score}",
      10, SCREEN_HEIGHT - 30,
      arcade.color.BLACK, 18, bold=True
    )

  def on_update(self, delta_time):
    self.enemy_list.update()

    self.player.center_x += self.player.change_x
    hits = arcade.check_for_collision_with_list(self.player, self.wall_list)
    for wall in hits:
      if self.player.change_x > 0:
        self.player.right = wall.left
      elif self.player.change_x < 0:
        self.player.left = wall.right

    self.player.center_y += self.player.change_y
    hits = arcade.check_for_collision_with_list(self.player, self.wall_list)
    for wall in hits:
      if self.player.change_y > 0:
        self.player.top = wall.bottom
      elif self.player.change_y < 0:
        self.player.bottom = wall.top


    hit_coins = arcade.check_for_collision_with_list(self.player, self.coins_list)
    for coin in hit_coins:
      coin.remove_from_sprite_lists()
      self.score += 1
      arcade.play_sound(arcade.load_sound(":resources:sounds/coin1.wav"))

  def on_key_press(self, key, modifiers):
    match key:
      case arcade.key.A:
        self.player.change_x = -self.player.speed
      case arcade.key.D:
        self.player.change_x = self.player.speed
      case arcade.key.W:
        self.player.change_y = self.player.speed
      case arcade.key.S:
        self.player.change_y = -self.player.speed

  def on_key_release(self, key, modifiers):
    match key:
      case arcade.key.A | arcade.key.D:
        self.player.change_x = 0
      case arcade.key.W | arcade.key.S:
        self.player.change_y = 0

window = MyGame()
arcade.run()
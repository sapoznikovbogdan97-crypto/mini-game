import arcade
import random

TILE_SCALING = 2
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Монетки и стены"


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.75)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.speed = 4


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.ASH_GREY)

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        self.player = Player()
        self.player_list.append(self.player)

        self.score = 0

        self.create_walls()
        self.create_coins()

    def create_walls(self):
        """Создаем стены по периметру экрана"""
        with open('wall.txt') as f:
            for line in f:
                arcade.Sprite(":resources:/images/tiles/boxCrate_double.png")
                wall = arcade.Sprite(":resources:/images/tiles/boxCrate_double.png")
                my_x, my_y = map(int, line.split())
                wall.center_x = my_x
                wall.center_y = my_y
                self.wall_list.append(wall)


    def create_coins(self):
        """Добавляем несколько монет в случайных местах"""
        for i in range(10):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
            coin.center_x = random.randint(50, SCREEN_WIDTH - 50)
            coin.center_y = random.randint(50, SCREEN_HEIGHT - 50)

            # Чтобы монета не была внутри стены
            if not arcade.check_for_collision_with_list(coin, self.wall_list):
                self.coin_list.append(coin)

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Отображаем счёт
        arcade.draw_text(
            f"Счёт: {self.score}",
            10, SCREEN_HEIGHT - 30,
            arcade.color.BLACK, 18, bold=True
        )

    def on_update(self, delta_time):
        # Двигаем игрока
        self.player.center_x += self.player.change_x
        hit_walls = arcade.check_for_collision_with_list(self.player, self.wall_list)
        for wall in hit_walls:
            if self.player.change_x > 0:
                self.player.right = wall.left
            elif self.player.change_x < 0:
                self.player.left = wall.right
        self.player.change_x = 0 if hit_walls else self.player.change_x

        self.player.center_y += self.player.change_y
        hit_walls = arcade.check_for_collision_with_list(self.player, self.wall_list)
        for wall in hit_walls:
            if self.player.change_y > 0:
                self.player.top = wall.bottom
            elif self.player.change_y < 0:
                self.player.bottom = wall.top
        self.player.change_y = 0 if hit_walls else self.player.change_y

        # Проверяем сбор монет
        hit_coins = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in hit_coins:
            # coin_list.remove(coin)
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(arcade.load_sound(":resources:sounds/coin1.wav"))

    def on_key_press(self, key, modifiers):
        match key:
            case arcade.key.LEFT:
                self.player.change_x = -self.player.speed
            case arcade.key.RIGHT:
                self.player.change_x = self.player.speed
            case arcade.key.DOWN:
                self.player.change_y = -self.player.speed
            case arcade.key.UP:
                self.player.change_y = self.player.speed

    def on_key_release(self, key, modifiers):
        match key:
            case arcade.key.LEFT | arcade.key.RIGHT:
                self.player.change_x = 0
            case arcade.key.UP | arcade.key.DOWN:
                self.player.change_y = 0



game = MyGame()
arcade.run()
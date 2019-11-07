import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada or Potato"
GAME_SPEED = 1/60

IMAGE_ADA = arcade.load_texture("images/ada.png")
IMAGE_POTATO = arcade.load_texture("images/potato.png")


class Ada_or_potato(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None
        self.score = 0
        self.timer = 0

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(ada())
        self.logo_list.append(potato())
        self.score = 0

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.logo_list.draw()
        score = str(self.score)
        arcade.draw_text("Your score:" + score, 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.logo_list.update()
        self.timer += 1/60

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if 1 <= self.timer % 2 < 2:
            self.score += 1
        else:
            self.score -= 1


class ada(arcade.Sprite):
    def __init__(self):
        super().__init__("images/ada.png")
        self.timer = 0
        self.center_x = WINDOW_WIDTH/2
        self.center_y = WINDOW_HEIGHT/2

    def update(self):
        self.timer += 1 / 60
        if 1 <= self.timer % 2 < 2:
            self.alpha = 255
        else:
            self.alpha = 0

class potato(arcade.Sprite):
    def __init__(self):
        super().__init__("images/potato.png", scale = 0.15)
        self.timer = 0
        self.center_x = WINDOW_WIDTH/2
        self.center_y = WINDOW_HEIGHT/2

    def update(self):
        self.timer += 1/60
        if 0 <= self.timer % 2 < 1:
            self.alpha = 255
        else:
            self.alpha = 0






def main():
    window = Ada_or_potato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

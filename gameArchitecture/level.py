from typing import Callable
import arcade
from data_classes.level_data import level_data
from entities.enemy import enemy
from entities.route import route
from entities.tower import tower

# extend my view_state instead.
class level(arcade.View):
    def __init__(self, data: level_data, on_exit_callback: Callable[[dict], None]):
        super().__init__()
        self.level_id = data.level_id
        self.route_data = data.route
        self.towers_data = data.towers
        self.enemies_data = data.enemies
        self.word_data = data.word_data
        self.resources : int = 0

        # Populate this once you have something to save, such as a high score.
        self.save_data = dict()
        # Use this to tell the Game entity that you're done and ready to close.
        self.on_exit_callback = on_exit_callback

        self.can_run_gameplay: bool = False

    def on_show_view(self):
        pass

    def on_hide_view(self):
        pass

    def setup(self):
        self.route = route(self.route_data)
        self.towers = tower.getListFromData(self.towers_data)
        self.enemies = enemy.getListFromData(self.enemies_data)
        tower.all_enemies = self.enemies

        self.can_run_gameplay = True

    def on_update(self, delta_time: float):
        if self.can_run_gameplay:
            self.towers.on_update(delta_time)
            self.enemies.on_update(delta_time)
        #run menu stuff here, or ui stuff, or whatever.

    def on_draw(self):
        arcade.start_render()
        if self.can_run_gameplay:
            self.towers.draw()
            self.enemies.draw()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.SPACE:
            self.exit_level()

    def exit_level(self):
        self.on_exit_callback(self.save_data)

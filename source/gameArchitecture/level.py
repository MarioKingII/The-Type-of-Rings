from typing import Callable
import arcade

from ..entities.bullet import Bullet
from ..data_classes.level_data import level_data
# from entities.enemy import Enemy
from .enemy_manager import EnemyManager
from ..entities.route import Route
from ..entities.tower import Tower

# extend my view_state instead.
class Level(arcade.View):
    active_word_index = 0
    active_letter_index = 0

    def __init__(self, data: level_data, on_exit_callback: Callable[[dict], None]):
        super().__init__()
        self.level_id = data.level_id
        self.route_data = data.route
        self.towers_data = data.towers
        self.enemies_data = data.enemies
        self.word_data = data.word_data
        self.resources : int = 0
        self.get_word()
        self.currentWord = arcade.Text(self.active_word, 660, 30, arcade.color.WHITE, 18, 10, 'right')
        self.wordLocation = 660
        self.onWord = arcade.draw_rectangle_filled(self.wordLocation, 30, 50, 50, arcade.color.GRAY)

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
        self.route = Route(self.route_data)
        self.towers = Tower.getListFromData(self.towers_data)
        self.enemy_mgr = EnemyManager(self.on_enemy_mgr_close,self.route,self.enemies_data,enemy_speed=100)
        self.enemy_mgr.start()

        # self.enemies = Enemy.getListFromData(self.enemies_data)
        # Tower.all_enemies = self.enemies

        self.can_run_gameplay = True

    def on_update(self, delta_time: float):
        if self.can_run_gameplay:
            self.towers.on_update(delta_time)
            self.enemy_mgr.on_update(delta_time)
            Bullet.all_bullets.on_update(delta_time=delta_time)
            # self.enemies.on_update(delta_time)
        #run menu stuff here, or ui stuff, or whatever.

        print(self.currentWord)

        
    def on_draw(self):
        arcade.start_render()
        if self.can_run_gameplay:
            self.towers.draw()
            if len(Bullet.all_bullets) > 0:
                Bullet.all_bullets.draw()
            self.enemy_mgr.on_draw()
            # self.enemies.draw()
            
            self.onWord.draw()
            self.currentWord.draw()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.SPACE:
            self.exit_level()
            
        self.Validate_Word(key)

    def exit_level(self):
        self.on_exit_callback(self.save_data)
    
    def on_enemy_mgr_close(self, EnemyManager):
        self.exit_level()

    def get_word(self):
        self.active_word = self.word_data[Level.active_word_index]
        self.active_letter = self.active_word[Level.active_letter_index]

    def Validate_Word(self, keystroke): #Keystroke has to be defined
        if keystroke == self.active_letter:          
            Level.active_letter_index += 1           
            if len(self.active_word) == Level.active_letter_index:
                self.resources += 100 # Needs work
                Level.active_letter_index = 0
                Level.active_word_index += 1
        else:
            Level.active_letter_index = 0

    

    

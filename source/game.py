import arcade
from .data_classes.game_data import game_data
from .data_classes.level_data import level_data
from .gameArchitecture.dataManager import data_manager
from .gameArchitecture.level import Level


class Game:
    def __init__(self):

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.gameWindow = arcade.Window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.data_manager = data_manager()
        self.gameData: game_data = self.data_manager.load_game_data()


        # self.active_level: level = level(
        #     self.data_manager.level_dummy_data(), self.on_level_exit
        # )
        # self.active_level.setup()

        # # arcade.set_background_color()
        # self.gameWindow.show_view(self.active_level)

        self.load_new_level(0)

        arcade.run()

    # Use this to save data when a level closes.
    def on_level_exit(self, save_data: dict = None):
        #self.gameWindow.close()
        if (save_data is not None):
            self.data_manager.save_data(save_data)

        currentIndex = self.gameData.level_ids.index(self.active_level.level_id)

        if (currentIndex == len(self.gameData.level_ids) - 1):
            self.gameWindow.close()
            arcade.exit()
            return
        
        self.load_new_level(currentIndex + 1)
        
    def load_new_level(self, level_index : int):
        #Garbage collection probably handles this fine, but I'm not 100% certain. Should come back to this.
        #del self.active_level
        self.active_level = Level(
            self.data_manager.load_level_data(self.gameData.level_ids[level_index]), self.on_level_exit
        )
        self.active_level.setup()
        self.gameWindow.show_view(self.active_level)
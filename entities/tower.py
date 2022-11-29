import arcade
from arcade import SpriteList
from entities.entity import entity

class tower(entity):

    all_enemies : SpriteList = None

    # TODO: make filepath be data-driven. Different tower types can have a different filepath. I guess this would be filepath_data? Or something like that.
    def __init__(
        self,
        filename: str = "images/towerImg.png",
        position: tuple[float, float] = (0, 0),
    ):
        super().__init__(filename=filename, position=position)
        # initialization logic goes here.
        #Sets up when the tower last fired.
        self.time_since_last_firing = 0.0
        #Sets up the firing rate/
        self.firing_rate = 2.0
        #Sets up damage multiplier.
        self.damage_multiplier = 1
        #Sets up damage level.
        self.current_tower_lv = 1
        #Temporary resource value
        self.resources_value = 10
        #Value of the range a tower can shoot.
        self.range = 50


    def on_update(self, delta_time: float = 1 / 60):
        super().on_update(delta_time)
        # implement logic
        #Tracks rate of fire.
        def towerShoot():
            self.time_since_last_firing += delta_time
            
            if self.time_since_last_firing >= self.firing_rate:

                self.time_since_last_firing = 0
                #print("Bang")
                #Bullet spawn positon to tower goes here. 

        #If the resources and tower level are correct, then the tower is upgraded. If the player does not have
        #the correct number of resources, then every value stays the same and the user is told they don't have
        #enough resources.
        def upgrade(resources, damage, tower_level):
            if resources >= 30 and tower_level == 3:
                resources -= 30
                damage = 4
                tower_level = 4
                return resources, damage, tower_level
            if resources >= 20 and tower_level == 2:
                resources -= 20
                damage = 3
                tower_level = 3
                return resources, damage, tower_level
            if resources >= 10 and tower_level == 1:
                resources -= 10
                damage = 2
                tower_level = 2
                return resources, damage, tower_level
            else:
                resources = resources
                damage = damage
                tower_level = tower_level
                print("Not enough resources.")
                return resources, damage, tower_level
                
        targetedEnemy = arcade.get_closest_sprite(self, tower.all_enemies)

        targetDistance = targetedEnemy[1]

        if targetDistance <= self.range:
            towerShoot()

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        super().draw(filter=filter, pixelated=pixelated, blend_function=blend_function)
        # implement any sprite-specific rendering you'd want.

    def getListFromData(positions: list[tuple[float, float]]):
        towers = SpriteList()
        for a in positions:
            towers.append(tower(position=a))
        return towers
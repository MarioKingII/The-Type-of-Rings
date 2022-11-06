from arcade import SpriteList
from entities.entity import entity
from entities.enemy import enemy



class tower(entity):

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
        #Testing code for upgrade() to make sure it works.
        # upgrade_results = upgrade(self.resources_value, self.damage_multiplier, self.current_tower_lv)
        # resources_value = upgrade_results[0]
        # damage_multiplier = upgrade_results[1]
        # current_tower_lv = upgrade_results[2]
        # print(f"Rsources Left: {resources_value}\nCurrent Damage: {damage_multiplier}\nTower Level: {current_tower_lv}")
        
        # 
        def check_resources(resources):
            if resources == 0:
                print("No resources")
                upgrade_results = "None"
                return upgrade_results
            else:
                upgrade_results = upgrade(self.resources_value, self.damage_multiplier, self.current_tower_lv)
                return upgrade_results

        # Test code for checking resources.
        # resource_check = check_resources(self.resources_value)
        # print(resource_check)

        

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        super().draw(filter=filter, pixelated=pixelated, blend_function=blend_function)
        # implement any sprite-specific rendering you'd want.

    def getListFromData(positions: list[tuple[float, float]]):
        towers = SpriteList()
        for a in positions:
            towers.append(tower(position=a))
        return towers

from arcade import Point, SpriteList
from .entity import Entity
from .route import Route
from .ephemerals import Ephemeral
from typing import Callable


class Enemy(Entity,Ephemeral):

    

    all_enemies = SpriteList()
    __atk_callback = None
    
    

    @classmethod
    def _get_atk_callback(cls) -> Callable[['Enemy'],None]:
        return cls.__atk_callback



    @classmethod
    def _set_atk_callback(cls,callback :Callable[['Enemy'],None]) -> None:
        cls.__atk_callback = callback

    atk_callback = property(fget=_get_atk_callback,fset=_set_atk_callback)
    
    __destroyed_enemies = []
    total_destroyed = 0
    
    @classmethod
    @property
    def destroyed_entities(cls):
        return cls.__destroyed_enemies


    # TODO: make filepath be data-driven. Different tower types can have a different filepath. I guess this would be filepath_data? Or something like that.
    def __init__(
        self,
        filename : str = "images/enemyImg.png",
        position : tuple[float, float] = (0, 0),
        route : Route = None,
        speed : float = 1
    ):
        if Enemy.atk_callback is None:
            raise NotImplementedError("Please assign a function to Enemy.atk_callback")
        super().__init__(filename=filename, position=position)
        self.route = route
        self.speed = speed
        
        Enemy.all_enemies.append(self)
        # initialization logic goes here.


    def on_update(self, delta_time: float = 1/ 60):
        super().on_update(delta_time)
        if (not self.is_active):
            return
        
        self.delta_time = delta_time

        
        self.followRoute()
        
        
        # implement logic

    def _on_spawn(self, **kwargs):
        self.position = (self.route.path[0][0],self.route.path[0][1])
        self.target_pos = self.route.path[1]
        self.route_iterator = 1
        self.alpha = 255
        self.is_active = True

    def _on_despawn(self):
        self.is_active = False
        Enemy.total_destroyed += 1
        self.alpha = 0
        self.set_position(-100,-100)
        
    
    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        super().draw(filter=filter, pixelated=pixelated, blend_function=blend_function)
        # implement any sprite-specific rendering you'd want.

# # TODO: Deprecate. This should be moved into a different place. A manager or something.
#     def getListFromData(num_enemies : int,route : Route):
#         enemies = SpriteList()
#         for a in range(num_enemies):
#             enemies.append(Enemy(route))
#         return enemies
    
    def followRoute(self):
        if self.route is None:
            print("why is there no route?")
            return
        
        #self.forward(self.speed * self.delta_time)
        self.move_toward_point(self.target_pos,self.speed * self.delta_time)
        if self.collides_with_point(self.target_pos):
            self.route_iterator += 1
            if self.route_iterator == len(self.route.path):
                self.attack_player()
                return
            self.target_pos = self.route.path[self.route_iterator]       
            # print(f"route_iterator: {self.route_iterator}, target_position = {self.target_pos}")
            #self.face_point(self.target_pos)
    
    def attack_player(self):
        Enemy.atk_callback(self)
        Enemy.despawn(self)
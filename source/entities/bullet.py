from arcade import SpriteList
from .entity import Entity
from .enemy import Enemy
from .ephemerals import Ephemeral

class Bullet(Entity,Ephemeral):

    all_bullets = SpriteList()
    __destroyed_bullets = []
    total_destroyed = 0

    @classmethod
    @property
    def destroyed_entities(cls):
        return cls.__destroyed_bullets

    def __init__(self, **kwargs):
        super().__init__("images/bulletImg.png",(-100,-100))
        Bullet.all_bullets.append(self)


    def _on_spawn(self,**kwargs):
        self.position = kwargs["position"]
        self.target : Entity = kwargs["target"]
        self.damage = kwargs["damage"]
        self.speed = kwargs["speed"]
        self.is_active = True
        self.alpha = 255
    

    def _on_despawn(self,):
        self.is_active = False
        Bullet.total_destroyed += 1
        self.alpha = 0
        self.set_position(-200,-100)
    
    def on_update(self, delta_time: float = 1 / 60):
        super().on_update(delta_time)
        if not self.is_active:
            return
        self.move_toward_point(self.target.position, self.speed * delta_time)
        hits = self.collides_with_list(Enemy.all_enemies)
        if hits is not None and len(hits) > 0:
            for x in hits:
                self.hit(x)
            Bullet.despawn(self)
    
    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        super().draw(filter=filter, pixelated=pixelated, blend_function=blend_function)
    
    def hit(self,target : Entity):
        pass
        

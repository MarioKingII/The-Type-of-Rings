from ..entities.enemy import Enemy
from ..entities.route import Route
from typing import Callable

class EnemyManager:

    def __init__(self, enemies_dead_callback : Callable[["EnemyManager"],None], route : Route, num_of_enemies, time_between_spawns = 1.0, enemy_speed = 1.0):
        self.enemies_dead_callback = enemies_dead_callback
        self.route = route
        self.num_of_enemies = num_of_enemies
        self.time_between_spawns = time_between_spawns
        self.enemy_speed = enemy_speed

        self.enemies_spawned = 0
        self.time_since_last_spawn = 0.0
        self.delta_time = 0
        self.is_active = False

    def start(self):
        Enemy.atk_callback = self._handle_atk
        self.is_active = True
    
    def close(self):
            if Enemy.atk_callback is self._handle_atk:
                Enemy.atk_callback = None
            self.enemies_dead_callback(self)
            self.is_active = False
    
    def on_update(self, delta_time: float) -> None:
        if Enemy.total_destroyed >= self.num_of_enemies:
            self.close()
        if not self.is_active:
            return
        self.delta_time = delta_time
        self._handle_spawn()
        Enemy.all_enemies.on_update(delta_time)
 
    def on_draw(self):
        Enemy.all_enemies.draw()

    def _handle_spawn(self): 
        self.time_since_last_spawn += self.delta_time
        if self.time_since_last_spawn > self.time_between_spawns and self.enemies_spawned < self.num_of_enemies:
            self.time_since_last_spawn = 0.0
            self.enemies_spawned += 1
            Enemy.spawn(route=self.route,speed=self.enemy_speed)
    
    # TODO: Implement Attack Handler.
    def _handle_atk(self,enemy : Enemy):
        pass
    
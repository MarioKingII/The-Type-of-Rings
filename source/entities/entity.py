import math
from xml.etree.ElementTree import tostring
import arcade

class Entity(arcade.Sprite):
    eIdCounter: int = 0
    # destroyed_entities = dict()

    def __init__(self, filename: str, position: tuple[float, float], **args):
        super().__init__(filename=filename, hit_box_algorithm="Detailed", **args)

        self.eID: str = str(Entity.eIdCounter)
        self.set_position(position[0], position[1])

        Entity.eIdCounter += 1

        self.IMAGE_ROTATION = 0
        self.is_active = False
    
    def move_toward_point(self,position,speed):
        
        start_x = self.center_x
        start_y = self.center_y
        
        dest_x = position[0]
        dest_y = position[1]

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        target_angle_radians = math.atan2(y_diff, x_diff)
        degrees= math.degrees(target_angle_radians)
        # if target_angle_radians < 0:
        #     target_angle_radians += 2 * math.pi

        self.angle = target_angle_radians
        self.change_x = math.cos(target_angle_radians) * speed
        self.change_y = math.sin(target_angle_radians) * speed

        self.center_x += self.change_x
        self.center_y += self.change_y

    
    # def on_spawn(self,position: tuple[float,float]):
    #     self.set_position(position[0],position[1])
    #     self.is_active = True
    
    # def on_despawn(self):
    #     self.is_active = False

    # @classmethod
    # def spawn(cls):

    
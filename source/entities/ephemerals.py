from abc import ABC,abstractmethod
class Ephemeral(ABC):



    @classmethod
    def spawn(cls, **kwargs):
        new_entity = None
        if len(cls.destroyed_entities) > 0:
            new_entity = cls.destroyed_entities.pop()
        else:
            new_entity = cls(**kwargs)
        
        new_entity._on_spawn(**kwargs)
    
    
    @classmethod
    def despawn(cls,target : "Ephemeral"):
        cls.destroyed_entities.append(target)
        print("Entity despawning.")
        target._on_despawn()
    
    @abstractmethod
    def _on_spawn(self, **kwargs):
        pass
    
    @abstractmethod
    def _on_despawn(self):
        pass

    @classmethod
    @property
    @abstractmethod
    def destroyed_entities(cls) -> list:
        pass
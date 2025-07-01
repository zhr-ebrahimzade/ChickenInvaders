from dataclasses import dataclass

@dataclass
class PlayerDataClass:
    image: str = "./"
    rocket_size: tuple = (0, 0)
    position: tuple = (0, 0)
    speed: int = 2
from dataclasses import dataclass

@dataclass
class WindowDataClass:
    width: int = 0
    height: int = 0
    title: str = "Welcome"
    location: str = "./"
    position: tuple = (0, 0)


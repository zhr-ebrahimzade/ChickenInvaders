

class Player:
    def __init__(self, image, position, speed):
        self.image = image
        self.position = position
        self.speed = speed

    def move(self, direction):
        self.position += self.speed * direction
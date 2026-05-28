class Cat:
    AVATAR_HAPPY = 'cat/img/happy.jfif'
    AVATAR_NEUTRAL = 'cat/img/normal.webp'
    AVATAR_SAD = 'cat/img/sad.png'

    def __init__(self, name):
        self.name = name
        self.age = 1
        self.satiety = 40
        self.happiness = 40
        self.is_sleeping = False

    def feed(self):
        if self.is_sleeping:
            return  # нельзя кормить спящего
        self.satiety += 15
        if self.satiety > 100:
            self.satiety = 100
            self.happiness = max(0, self.happiness - 30)
        else:
            self.happiness = min(100, self.happiness + 5)

    def play(self):
        import random
        if self.is_sleeping:
            self.is_sleeping = False
            self.happiness = max(0, self.happiness - 5)
            return
        self.happiness = min(100, self.happiness + 15)
        self.satiety = max(0, self.satiety - 10)
        if random.randint(1, 3) == 1:
            self.happiness = 0  # впадает в ярость

    def sleep(self):
        self.is_sleeping = True

    def get_avatar(self):
        if self.happiness >= 60:
            return self.AVATAR_HAPPY
        elif self.happiness >= 30:
            return self.AVATAR_NEUTRAL
        else:
            return self.AVATAR_SAD

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'satiety': self.satiety,
            'happiness': self.happiness,
            'is_sleeping': self.is_sleeping,
        }

    @classmethod
    def from_dict(cls, data):
        cat = cls(data['name'])
        cat.age = data['age']
        cat.satiety = data['satiety']
        cat.happiness = data['happiness']
        cat.is_sleeping = data['is_sleeping']
        return cat

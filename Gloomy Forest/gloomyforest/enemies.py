class Enemy:
    """A base class for all enemies"""
    def __init__(self, name, hp, damage):
        """Creates a new enemy
        :param name: the name of the enemy
        :param hp: the hit points of the enemy
        :param damage: the damage the enemy does with each attack
        """
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Wasp(Enemy):
    def __init__(self):
        super().__init__(name="Wasp", hp=10, damage=2)


class Mantis(Enemy):
    def __init__(self):
        super().__init__(name="Mantis", hp=30, damage=15)
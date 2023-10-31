import random


class Creature:
    p_death = 0.2
    p_reproduce = 0.2
    alive = True

    def natural_selection(self):
        if random.random() <= self.p_death:
            self.alive = False


class Population:
    def __init__(self, size=100):
        self.speciemen = {Creature() for _ in range(size)}

    def count_alive(self):
        return len({creature for creature in self.speciemen if creature.alive})

    def perform_natural_selection(self):
        for creature in self.speciemen:
            creature.natural_selection()


p1 = Population()

print(p1.count_alive())
p1.perform_natural_selection()
print(p1.count_alive())

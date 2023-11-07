import random
import matplotlib.pyplot as plt


class Creature:
    p_death = 0.2
    p_reproduce = 0.2
    alive = True

    def natural_selection(self):
        if random.random() <= self.p_death:
            self.alive = False

    def reproduce(self):
        if random.random() <= self.p_reproduce:
            return Creature()


class Population:
    def __init__(self, size=100):
        self.speciemen = {Creature() for _ in range(size)}
        self.history = []

    def count_alive(self):
        return len({creature for creature in self.speciemen if creature.alive})

    def perform_natural_selection(self):
        for creature in self.speciemen:
            creature.natural_selection()

    def simulate(self, generations):
        for _ in range(generations):
            self.history.append(self.count_alive())
            self.perform_natural_selection()
            self.reproduce()

    def reproduce(self):
        new_creatures = {creature.reproduce() for creature in self.speciemen if creature.alive}
        new_creatures -= {None}
        self.speciemen |= new_creatures

    def plot(self):
        plt.plot(self.history)
        plt.title("Plot of population")
        plt.show()


p1 = Population()

print(p1.count_alive())
p1.simulate(150)
print(p1.count_alive())
print(p1.history)
p1.plot()

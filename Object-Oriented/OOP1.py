import random
import matplotlib.pyplot as plt

SIGMA = 0.02


class Creature:
    alive = True

    def __init__(self, p_death=0.2, p_reproduce=0.2):
        self.p_death = p_death
        self.p_reproduce = p_reproduce

    def natural_selection(self):
        if random.random() <= self.p_death:
            self.alive = False

    def reproduce(self):
        if random.random() <= self.p_reproduce:
            return Creature(self.p_death + random.normalvariate(sigma=SIGMA),
                            self.p_reproduce + random.normalvariate(sigma=SIGMA))

    @property
    def p_death(self):
        return self.p_death

    @p_death.setter
    def p_death(self, value):
        if value < 0:
            self._p_death = 0
        else:
            self._p_death = value


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

    def plot_attribute(self, attribute='p_death'):
        values = [getattr(creature, attribute) for creature in self.speciemen]
        plt.hist(values)
        plt.show()


p1 = Population()

print(p1.count_alive())
p1.simulate(75)
print(p1.count_alive())
print(p1.history)
# p1.plot()
p1.plot_attribute('p_reproduce')

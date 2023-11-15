import random
import matplotlib.pyplot as plt

SIGMA = 0.02


class Probability:
    """Descriptor for probability (forces probability to be between 0 and 1"""

    def __set_name__(self, owner, name):  # name = 'p_death' lub 'p_reproduce'
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, max(0.0, min(1.0, value)))


class Creature:
    """
    Model of living creature

    Attributes:
        alive(bool): indicator if the creature is alive
        p_death(float): probability of death
        p_reproduce(float): probability of reproduction

    Methods:
        natural_selection: kills the creature with probability p_death
        reproduce: returns new creature with attributes similar to its parent
    """

    alive = True
    p_death = Probability()
    p_reproduce = Probability()

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

    # @property
    # def p_death(self):
    #     return self._p_death
    #
    # @property
    # def p_reproduce(self):
    #     return self._p_reproduce
    #
    # @p_death.setter
    # def p_death(self, value):
    #     self._p_death = max(0.0, min(1.0, value))
    #
    # @p_reproduce.setter
    # def p_reproduce(self, value):
    #     self._p_death = max(0.0, min(1.0, value))


class Population:

    """
    Model of population

    Attributes:
        specimen(set): contains objects representing creatures
        history(list): list containing previous counts of the population

    Methods:
        count_alive: returns number of alive creatures that are alive
        natural_selection: applies natural_selection to each creature in the population
        reproduce: creates new creatures by allowing creatures that are alive to reproduce
        simulate: runs simulation for the given number of generations
    """

    def __init__(self, size=100):
        self.specimen = {Creature() for _ in range(size)}
        self.history = []

    def count_alive(self):
        return len({creature for creature in self.specimen if creature.alive})

    def perform_natural_selection(self):
        for creature in self.specimen:
            creature.natural_selection()

    def simulate(self, generations):
        for _ in range(generations):
            self.history.append(self.count_alive())
            self.perform_natural_selection()
            self.reproduce()

    def reproduce(self):
        new_creatures = {creature.reproduce() for creature in self.specimen if creature.alive}
        new_creatures -= {None}
        self.specimen |= new_creatures

    def plot(self):
        plt.plot(self.history)
        plt.title("Plot of population")
        plt.show()

    def plot_attribute(self, attribute='p_death'):
        values = [getattr(creature, attribute) for creature in self.specimen]
        plt.hist(values)
        plt.show()


p1 = Population(1000)
print(p1.count_alive())
p1.simulate(50)
print(p1.count_alive())
print(p1.history)
# p1.plot()
p1.plot_attribute('p_reproduce')

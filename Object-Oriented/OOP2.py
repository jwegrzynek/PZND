import random
import matplotlib.pyplot as plt
from collections import namedtuple

SIGMA = 0.02
P_DEATH_IF_HUNGRY = 0.5
P_DEATH_IF_FED = 0.05

State = namedtuple('State', ['victims', 'predators'])
State(victims=100, predators=200)


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
            return type(self)()


class Victim(Creature):
    p_escape = Probability()

    def __init__(self, p_death=0.2, p_reproduce=0.2, p_escape=0.8):
        super().__init__(p_death, p_reproduce)
        self.p_escape = p_escape

    def escape(self):
        if random.random() <= self.p_escape:
            return True
        else:
            return False


class Predator(Creature):

    def __init__(self, p_death=P_DEATH_IF_HUNGRY, p_reproduce=0.2):
        super().__init__(p_death, p_reproduce)
        self.p_death = p_death
        self.p_reproduce = p_reproduce

    def hunt(self, victim):
        if not victim.escape():
            self.p_death = P_DEATH_IF_FED
            victim.alive = False
        else:
            self.p_death = P_DEATH_IF_HUNGRY


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

    def __init__(self, victims=100, predators=100):
        self.victims = {Victim() for _ in range(victims)}
        self.predators = {Predator() for _ in range(predators)}
        self.history = []

    def count_alive(self):
        victims = len({creature for creature in self.victims if creature.alive})
        predators = len({creature for creature in self.predators if creature.alive})

        return State(victims=victims, predators=predators)

    def perform_natural_selection(self):
        for creature in self.victims | self.predators:
            creature.natural_selection()

    def simulate(self, generations):
        for _ in range(generations):
            self.history.append(self.count_alive())
            self.perform_natural_selection()
            self.reproduce()

    @staticmethod
    def _reproduce(subset):
        """Returns set of new creatures reproduced from the subset"""
        new_creatures = {creature.reproduce() for creature in subset if creature.alive}
        new_creatures -= {None}
        return new_creatures

    def reproduce(self):
        self.victims |= Population._reproduce(self.victims)
        self.predators |= Population._reproduce(self.predators)

    def plot(self):
        plt.plot(self.history)
        plt.title("Plot of population")
        plt.show()

    def plot_attribute(self, attribute='p_death'):
        values = [getattr(creature, attribute) for creature in self.specimen]
        plt.hist(values)
        plt.show()


pred1 = Predator()
victim1 = Victim()

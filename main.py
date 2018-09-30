__author__ = 'David T. Pocock'


from hill_climbing import HillClimbing
from random_search import RandomSearch
from genetic_algorithm import GeneticAlgorithm


def main():
    ga = GeneticAlgorithm("Hello World!", 1000, 0.8, 0.03, True, 0.05, 0.65)
    ga.run()
    hc = HillClimbing("Hello World!", 10)
    hc.run()
    rs = RandomSearch("Hel", 1)
    rs.run()


if __name__ == "__main__":
    main()
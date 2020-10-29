from random import randint

class City:
    def __init__(self):
        self.name: str = ''
        self.id: int = -1
        self.distance: list = []

    def __repr__(self):
        return str(self.id)
    
    def set_name(self, name: str):
        self.name = name

    def set_id(self, id: int):
        self.id = id

    def add_distance(self, distance: int):
        self.distance.append(distance)
    
class CityGroup:
    def __init__(self):
        self.array_city:list = []
    
    def add_city(self, newCity: City):
        self.array_city.append(newCity)
        newCity.set_id(len(self.array_city) - 1)

    def remove_city(self, city: City):
        self.array_city.append(city)
    
    def get_cities(self):
        return self.array_city

class Generator:
    def __init__(self, size: int):
        self.cities = CityGroup()
        self.size: int = size

    def generate_cities(self):
        for i in range(self.size):
            self.cities.add_city(City())

    def generate_distances(self, max_distance: int):
        cities = self.cities.get_cities()

        # percorre cada cidade colocando uma distancia aleatoria entre as cidades
        for i in range(self.size):
            for j in range(i, self.size):
                if (i == j):
                    cities[i].add_distance(0)
                else:
                    distance = randint(0, max_distance) + 1
                    cities[i].add_distance(distance)
                    cities[j].add_distance(distance)
    
    def get_cities(self): 
        return self.cities

class PopulationGenerator:
    def __init__(self, cities: CityGroup, population_size: int):
        self.cities = cities.get_cities()
        self.population_size = population_size
        self.population: list = []

    def generate_populations(self):
        for i in range(self.population_size):
            self.population.append(self.generate_individual())

    def generate_individual(self):
        individual = []
        cities = list(self.cities)
        while(len(cities) > 0):
            random_city_index = randint(0, len(cities) - 1)
            individual.append(cities.pop(random_city_index))
        return individual
    
    def get_population(self):
        return self.population

class FitnessCalculator:
    def __init__(self, population: list):
        self.population = population
        self.distances: list = []
        self.fitness: list = []
        self.distance_sum: int = 0
    
    def calulate_total_distances(self):
        for individual in self.population:
            actual_distance = 0
            for i in range(len(individual) - 1):
                actual_city = individual[i]
                next_city = individual[i+1]
                actual_distance += actual_city.distance[next_city.id]
            self.distances.append(actual_distance)
            self.distance_sum += actual_distance
        self.distances.sort()

    # toDo: calcular a função fitness
    def calculate_fitness(self):
        for distance in self.distances:
            fitness = self.distance_sum // distance
            self.fitness.append(fitness)

    def get_population_distances(self):
        return self.distances

    def get_population_fitness(self):
        return self.fitness

class Roulette:
    def __init__(self, fitness: list):
        self.fitness = fitness
        self.intervals: list = []
        self.selected_index: list = []
        self.min_value: int = 0
        self.max_value: int = 0

    def set_intervals(self):
        begin: int = 0
        for fitness_value in self.fitness:
            interval = {
                "begin": begin,
                "end": begin + fitness_value
            }
            self.intervals.append(interval)
            begin = interval["end"] + 1
        self.min_value = self.intervals[0]["begin"]
        self.max_value = self.intervals[len(self.intervals) - 1]["end"]

    def select_index(self, how_many: int):
        self.set_intervals()
        while len(self.selected_index) < how_many:
            number_selected = randint(self.min_value, self.max_value)
            for index, interval in enumerate(self.intervals):
                if(number_selected>interval["begin"] and number_selected<interval["end"] and not(self.selected_index.count(index))):
                    self.selected_index.append(index)
        self.selected_index.sort()
    
    def get_selected_index(self):
        return self.selected_index
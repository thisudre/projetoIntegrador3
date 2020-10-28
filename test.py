from models import Generator, PopulationGenerator, FitnessCalculator

quant_cidades = 5
distancia_maxima = 30
tamanho_populacao = 4

gen = Generator(quant_cidades)
gen.generate_cities()
gen.generate_distances(distancia_maxima)
print ("Distancias: ")
for i in range(quant_cidades):
    print (gen.get_cities().get_cities()[i].distance)


pop_gen = PopulationGenerator(gen.get_cities(), tamanho_populacao)
pop_gen.generate_populations()

population = pop_gen.get_population()

fit = FitnessCalculator(population)
fit.calulate_total_distances()
fit.calculate_fitness()

print("População: ")
print(population)

print("Distancia percorrida por cromossomo: ")
print(fit.get_population_distances())

print("Porcentagem de escolha de cada cromossomo:")
print(fit.get_population_fitness())
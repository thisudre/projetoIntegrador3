from models import Generator, PopulationGenerator, FitnessCalculator, Roulette

quant_cidades = 30
distancia_maxima = 50
tamanho_populacao = 100
quant_sorteada = 20

gen = Generator(quant_cidades)
gen.generate_cities()
gen.generate_distances(distancia_maxima)

pop_gen = PopulationGenerator(gen.get_cities(), tamanho_populacao)
pop_gen.generate_populations()

population = pop_gen.get_population()

fit = FitnessCalculator(population)
fit.calulate_total_distances()
fit.calculate_fitness()

roulette = Roulette(fit.get_population_fitness())
roulette.select_index(quant_sorteada)

# print ("Distancias: ")
# for i in range(quant_cidades):
#     print (gen.get_cities().get_cities()[i].distance)

# print("População: ")
# print(population)

# print("Distancia percorrida por indivíduo: ")
# print(fit.get_population_distances())

# print("Valor da função fitness de cada indivíduo: ")
# print(fit.get_population_fitness())

print("Indices selecionados pela roleta: ")
print(roulette.get_selected_index())
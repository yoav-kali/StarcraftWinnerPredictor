import pandas as pd
from genetic.genetic import Genetic
from network.networkgenerator import NetworkGenerator
import pickle
data = pd.read_csv('data/aggregate_data.csv')
X = data[[x for x in data if x != 'result']]
for x in X:
    X[x] = (X[x] - min(X[x]))/(max(X[x] - min(X[x])))

y = data[['result']]

netGenerator = NetworkGenerator(num_layers=4, num_inputs=11, num_neurons=5)
networks = [netGenerator.generate() for _ in range(10)]

for gen in range(40):
    genetic = Genetic(networks, X, numgens=120)
    networks = genetic.begin(X, y).items
    for i in range(10):
        with open('network{}.pickle'.format((gen * 10) + i + 100), 'wb') as handle:
            pickle.dump(networks[i], handle, protocol=pickle.HIGHEST_PROTOCOL)


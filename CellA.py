import random
import numpy as np
import matplotlib.pyplot as plt

class cell_world:
	rulebook_184 = {'[1, 1, 1]' : 1,
	                '[1, 1, 0]' : 0,
	                '[1, 0, 1]' : 1,
	                '[1, 0, 0]' : 1,
	                '[0, 1, 1]' : 1,
	                '[0, 1, 0]' : 0,
	                '[0, 0, 1]' : 0,
	                '[0, 0, 0]' : 0,}

	rulebook_110 = {'[1, 1, 1]' : 0,
	                '[1, 1, 0]' : 1,
	                '[1, 0, 1]' : 1,
	                '[1, 0, 0]' : 0,
	                '[0, 1, 1]' : 1,
	                '[0, 1, 0]' : 1,
	                '[0, 0, 1]' : 1,
	                '[0, 0, 0]' : 0,}


	def __init__(self, worldsize = 100, rule = '110'):
		self.cells = np.random.randint(0, 2, size = worldsize)
		self.rule = rule

		if self.rule == '184':
			self.rulebook = self.rulebook_184
		else:
			self.rulebook = self.rulebook_110

	def update(self):
		newgen = np.array(np.zeros(len(self.cells)), dtype = int)
		
		for i in range(1, len(self.cells) - 1):
			newgen[i] = self.rulebook[str(self.cells[i - 1 : i + 2].tolist())]

		newgen[0] = self.rulebook[str([0] + self.cells[0 : 2].tolist())]
		newgen[-1] = self.rulebook[str(self.cells[-2 : ].tolist() + [0])]

		self.cells = newgen

	def live_cells(self):
		return np.sum(self.cells > 0)


class Simulation:
	def __init__(self, simrule, simsize = 100):
		self.instance = cell_world(worldsize = simsize, rule = simrule)
		self.steps = []

	def run(self, timesteps = 100):
		for i in range(timesteps):
			self.instance.update()
			self.steps.append(self.instance.cells)

	def plot(self):
		final = np.array(self.steps, dtype = bool)
		plt.matshow(np.invert(final), cmap = plt.cm.gray)
		plt.xlabel('Cell Number [-]')
		plt.ylabel('Time Step [-]')
		plt.title('Cell Automata - ' + self.instance.rule)
		plt.savefig('simresults' + self.instance.rule + '.png')


if __name__ == "__main__":
    Sim = Simulation('110')
    Sim.run()
    Sim.plot()






import random

class EpsilonGreed():
	def __init__(self, epsilon, counts, values):
		self.epsilon = epsilon
		self.counts = counts
		self.values = values
		return
	
	def initialize(self, n_arms):
		self.counts = [0 for col in range(n_arms)]
		self.values = [0.0 for col in range(n_arms)]
		return

	def ind_max(x):
		m = max(x)
		return x.index(m)

	def select_arm(self):
		if random.random() > self.epsilon:
			return ind_max(self.values)
		else:
			return random.randrange(len(self.values))


	def update(self, chosen_arm, reward):
		self.counts[chosen_arm]+=1
		n = self.counts[chosen_arm]

		value = self.values[chosen_arm]
		new_value = ((n-1)/float(n))*value + (1/float(n))*reward
		self.values[chosen_arm] = new_value
		return

class BernoulliArm():
	def __init__(self, p):
		self.p=p

	def draw(self):
		if random.random()>self.p:
			return 0.0
		else:
			return 1.0
means = [0.1, 0.1, 0.1, 0.1, 0.9]
n_arms = len(means)
random.shuffle(means)
arms = list(map(lambda mu: BernoulliArm(mu), means))
print(arms[0].draw())
print(arms[1].draw())
print(arms[2].draw())
print(arms[3].draw())
print(arms[2].draw())









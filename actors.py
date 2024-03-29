import random

class Creature:
	def __init__(self, name, the_level):
		self.name = name
		self.level = the_level

	def __repr__(self):
		return "Creature - {} of lvl {}".format(self.name, self.level)

	def get_defensive_role(self):
		return random.randint(1,12) * self.level

class Wizard(Creature):

	def attack(self, creature):
		print("The {} attacks {}!".format(self.name, creature.name))

		my_roll = random.randint(1,12) * self.level
		creature_roll = creature.get_defensive_role()

		print("You roll {}!!".format(my_roll))
		print("The {} rolls {}!!".format(creature.name, creature_roll))

		if my_roll >= creature_roll:
			print("The {} has TRIUMPHED over {}!!".format(self.name, creature.name))
			return True
		else:
			print("{} was DEFEATED by {}!!".format(self.name, creature.name))
			return False


class SmallAnimal(Creature):
	def get_defensive_role(self):
		base_roll = super().get_defensive_role()
		return base_roll / 2


class Dragon(Creature):
	def __init__(self, name, level, scaliness, breaths_fire):
		super().__init__(name, level)
		self.scaliness = scaliness
		self.breaths_fire = breaths_fire

	def get_defensive_role(self):
		base_roll = super().get_defensive_role()
		## variable = VALUE_IF_TRUE if SOME_TEST else VALUE_IF_FALSE
		fire_modifier = 5 if self.breaths_fire else 1
		scaliness_modifier = self.scaliness / 10

		return base_roll * fire_modifier * scaliness_modifier
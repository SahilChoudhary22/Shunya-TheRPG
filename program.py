from actors import Wizard, Creature, SmallAnimal, Dragon
import random
import time 


def main():
	print_header()
	game_loop()


def print_header():
	print("---------------------------------")
	print("-------SHUNYA - THE RPG ---------")
	print("---------------------------------")
	print()


def game_loop():
	
	creatures = [ SmallAnimal('Toad', 1),
				  Creature('Tiger', 12),
				  SmallAnimal('Bat', 3),
				  Dragon('Dragon', 50, 30, True),
				  Wizard('Evil Tantrik', 1000),
				  Creature('Ramu Kaka', 15),
				  Creature('Simar from \'Sasural Simar ka\' as Makhi', 2000),
				  Creature('Naagin', 40)
				]
	
	hero = Wizard('Baahubali', 75)


	while True:

		active_creature = random.choice(creatures)
		print("A {} of lvl {} has appeared from a dark and foggy forest...".format(active_creature.name, active_creature.level))

		cmd = input("Do you [a]ttack, [r]un away or [l]ook around?")
		if cmd == 'a':
			if hero.attack(active_creature):
				creatures.remove(active_creature)
			else:
				print("{} runs and hides...recovering...".format(hero.name))
				time.sleep(5)
				print("{} is BACK!!".format(hero.name))
		elif cmd == 'r':
			print("Running Away!")
		elif cmd == 'l':
			print("{} looks around and sees: ".format(hero.name))
			for c in creatures:
				print(' * A {} of lvl {}'.format(c.name, c.level))
		else:
			print("Okay, exiting game...")
			break

		if not creatures:
			print("You've defeated all the creatures!!")
			break

		print("")


if __name__ == "__main__":
	main()
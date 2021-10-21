import time
import numpy as np
import sys
import movesDict

def delay_print(s):
	# print 1 char at a time
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)

class Pokemon:
	def __init__(self, name, types, moves, health):
		self.name = name
		self.types = types
		self.moves = moves
		# self.attack = EVs['ATTACK']
		# self.defense = EVs['DEFENSE']
		self.health = health


	def fight(self, P2):
		# Print fight info
		print("-----POKEMON BATTLE-----")
		print(f"\n{self.name}")
		print("TYPE/",self.types)
		# print("ATTACK/", self.attack)
		# print("DEFENSE/", self.defense)
		print("\nVS")
		print(f"\n{P2.name}")
		print("TYPE/",P2.types)
		# print("ATTACK/", P2.attack)
		# print("DEFENSE/", P2.defense)
		time.sleep(2)

		while (self.health > 0) and (P2.health > 0):
			# Print the health of each pokemon
			print(f"\n{self.name}\t\tHLTH\t{self.health}")
			print(f"{P2.name}\t\tHLTH\t{P2.health}\n")       	

			# 1st Pokemon's turn          
			print(f"\nLet's Go {self.name}!")
			for i,x in enumerate(self.moves):
				print(f"{i+1}.",x)
			index = int(input('Pick a move: '))
			delay_print(f"\n{self.name} used {self.moves[index-1]}!")
			time.sleep(1)

			P2.health -= movesDict.movelist[self.moves[index-1]]['give'] #give damage
			self.health += self.health*movesDict.movelist[self.moves[index-1]]['get'] #heals

			time.sleep(1)
			print(f"\n{self.name}\t\tHLTH\t{self.health}")
			print(f"{P2.name}\t\tHLTH\t{P2.health}\n")
			time.sleep(.5)

			#see whether P2 is fainted
			if P2.health <= 0:
				delay_print("\n..."+P2.name+" fainted.")
				break

			# 2nd Pokemon's turn          
			print(f"\nLet's Go {P2.name}!")
			for i, x in enumerate(P2.moves):
				print(f"{i+1}.",x)
			index = int(input('Pick a move: '))
			delay_print(f"\n{P2.name} used {P2.moves[index-1]}!")
			time.sleep(1)

			self.health -= movesDict.movelist[P2.moves[index-1]]['give']
			P2.health += P2.health*movesDict.movelist[P2.moves[index-1]]['get']

			time.sleep(1)
			print(f"\n{self.name}\t\tHLTH\t{self.health}")
			print(f"{P2.name}\t\tHLTH\t{P2.health}\n")  
			time.sleep(.5)

			#see whether self is fainted
			if self.health <= 0:
				delay_print("\n..."+self.name+" fainted.")
				break

		#end of the battle
		money = np.random.choice(5000)
		delay_print(f"\nOpponent paid you ${money}.\n")


if __name__ == '__main__':
	#Create Pokemon object
	Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Fire Blast', 'Fire Punch'],120)
	Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],100)
	Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],100)


	Charizard.fight(Blastoise)

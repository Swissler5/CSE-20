#Shea Wissler
#Assignment 10.1: Your Own Class
#This code will implement a demo program with a new class that I create


class Character():
	def __init__(self, race, health=100, attack=100, speed=100, armor=None, level=1):
		self.__race = race
		self.__health = health
		self.__attack = attack
		self.__speed = speed
		self.__armor = armor

	def set_items(self, armor=None, level=1):
		return("Your character needs to set a class before setting items.")

	def get_items(self, armor=None, level=1):
		return("Your character currently has no items, pick a class and an assosiated held item.")

	def set_stats(self, armor=None, level=1):
		return("Base character's base stats don't change, pick a class before getting bonus stats.")

	def get_stats(self, armor=None, level=1):
		return("Base character's stats: \nHealth-100 \nAttack-100 \nSpeed-100 \nAttack Range-0")

	def characteristics(self, race, armor=None, level=None):
		self.__race = str(self.__race)
		self.__armor = str(self.__armor)
		if self.__armor == "None":
			return "Your character is of race " + race + ", and has no armor."
		elif self.__armor == "Cloak":
			return "Your character is of race " + race + ", and wears a cloak instead of armor."
		else:
			return "Your character is of race " + race + ", and has " + self.__armor + " armor."
	def inventory(self, race=None, armor=None, level=None):
		self.__armor = str(self.__armor)
		if self.__armor == "None":
			return "Your character has an empty inventory with an empty armor slot. 20 inventory slots and 1 armor slot left."
		elif self.__armor == "Cloak":
			return "Your character has an empty inventory with a cloak in the armor slot. 20 inventory slots left."
		else:
			return "Your character has an empty inventory and has a " + self. __armor + " armor in the armor slot. 20 inventory slots left."

class Brawler(Character):
	def __init__(self, race, health=100, attack=100, speed=100, armor=None, potion_type=None, level=1):
		Character.__init__(self, race, health=100, attack=100, speed=100, armor=None, level=1)
		self.__race = race
		self.__class_item = "Small Sheild"
		self.__armor = armor
		self.__health = health
		self.__attack = attack
		self.__speed = speed
		self.__level = level


	def set_items(self, race, armor=None, potion_type=None, level=1):
		self.__potion_type = potion_type
		return "Item list compiled"

	def get_items(self, race, armor=None, potion_type=None, level=1):
		self.set_items(potion_type)
		self.__potion_type = potion_type
		if self.__potion_type != None:
			line = "Your Brawlers held items are a Potion of " + self.__potion_type + " and " + self.__class_item + "."
		else:
			line = "Your Brawlers held item is a " + self.__class_item + "."
		return line

	def get_stats(self, race, armor=None, potion_type=None, level=1):
		self.set_stats(self)
		self.__health = str(self.__health)
		self.__attack = str(self.__attack)
		self.__speed = str(self.__speed)
		return "The stats of your level " + self.__level + " Brawler: \nHealth-" + self.__health + "\nAttack-" + self.__attack + "\nSpeed-" + self.__speed + "\nAttack Range-1 unit"

	def set_stats(self, race, armor=None, potion_type=None, level=1):
		self.__level = int(self.__level)
		self.__health += (15 * self.__level)
		self.__attack += (10 * self.__level)
		self.__speed += (5 * self.__level)
		self.__level = str(self.__level)


	def characteristics(self, race, armor=None, potion_type=None, level=1):
		self.__race = race
		self.__class_item = "Small Sheild"
		self.__armor = armor
		self.__level = level
		self.__potion_type = potion_type
		self.__level = str(self.__level)
		self.__race = str(self.__race)
		self.__armor = str(self.__armor)
		self.__class_item = str(self.__class_item)
		self.__potion_type = str(self.__potion_type)
		return "Your character is a level " + self.__level + " Brawler of race " + self.__race + ", with " + self.__armor + " armor, a " + self.__class_item + ", and a Potion of " + self.__potion_type

	def inventory(self, race, armor=None, potion_type=None, level=1):
		self.__armor = str(armor)
		self.__potion_type = str(potion_type)
		if self.__potion_type == "None":
			if self.__armor == "None":
				return "Your Brawler has 19 empty inventory slots with 1 empty armor slot. 1 slot is being taken up by the Small Shield."
			elif self.__armor == "Cloak":
				return "Your Brawler has 19 empty inventory slots with a cloak in the armor slot. 1 slot is being taken up by the Small Shield."
			else:
				return "Your Brawler has 19 empty inventory slots and has " + self. __armor + " armor in the armor slot. 1 slot is being taken up by the Small Shield."
		else:
			if self.__armor == "None":
				return "Your Brawler has 18 empty inventory slots with 1 empty armor slot. 2 inventory slots are taken by the Small Shield and the Potion of " + self.__potion_type + "."
			elif self.__armor == "Cloak":
				return "Your Brawler has 18 empty inventory slots with a cloak in the armor slot. 2 inventory slots are taken by the Small Shield and the Potion of " + self.__potion_type + "."
			else:
				return "Your Brawler has 18 empty inventory slots and has " + self. __armor + " armor in the armor slot. 2 inventory slots are taken by the Small Shield and the Potion of " + self.__potion_type + "."


class Archer(Character):
	def __init__(self, race, health=100, attack=100, speed=100, armor=None, arrow_type=None, level=1):
		Character.__init__(self, race, health=100, attack=100, speed=100, armor=None, level=1)
		self.__class_item = "Short Bow"
		self.__armor = armor
		attack_range = 15
		self.__health = health
		self.__attack = attack
		self.__speed = speed
		self.__level = level


	def set_items(self, race, armor=None, arrow_type=None, level=1):
		self.__arrow_type = arrow_type
		return "Item list compiled"

	def get_items(self, race, armor=None, arrow_type=None, level=1):
		self.set_items(arrow_type)
		self.__arrow_type = arrow_type
		if self.__arrow_type != None:
			line = "Your Archers held items are " + self.__class_item + " and a quiver filled with " + self.__arrow_type + " Arrows."
		else:
			line = "Your Archers held item is a " + self.__class_item + " and an empty quiver."
		return line

	def get_stats(self, race, armor=None, arrow_type=None, level=1):
		self.set_stats(self)
		self.__health = str(self.__health)
		self.__attack = str(self.__attack)
		self.__speed = str(self.__speed)
		return "The stats of your level " + self.__level + " Archer: \nHealth-" + self.__health + "\nAttack-" + self.__attack + "\nSpeed-" + self.__speed + "\nAttack Range-15 units"

	def set_stats(self, race, armor=None, arrow_type=None, level=1):
		self.__level = int(self.__level)
		self.__health += (5 * self.__level)
		self.__attack += (10 * self.__level)
		self.__speed += (10 * self.__level)
		self.__level = str(self.__level)	

	def characteristics(self, race, armor="No", arrow_type=None, level=1):
		self.__race = race
		self.__class_item = "Short Bow"
		self.__armor = armor
		self.__level = level
		self.__arrow_type = arrow_type
		self.__level = str(self.__level)
		self.__race = str(self.__race)
		self.__armor = str(self.__armor)
		self.__class_item = str(self.__class_item)
		self.__arrow_type = str(self.__arrow_type)
		if self.__arrow_type == "None":
			return "Your character is a level " + self.__level + " Archer of race " + self.__race + ", with " + self.__armor + " armor, a " + self.__class_item + ", and an empty quiver."
		else:
			return "Your character is a level " + self.__level + " Archer of race " + self.__race + ", with " + self.__armor + " armor, a " + self.__class_item + ", and a Arrows of " + self.__arrow_type + "."

	def inventory(self, race, armor=None, arrow_type=None, level=1):
		self.__armor = str(self.__armor)
		self.__arrow_type = arrow_type
		if self.__arrow_type == "None":
			if self.__armor == "None":
				return "Your Archer has 19 empty inventory slots with 1 empty armor slot. 2 slot is being taken up by the Short Bow."
			elif self.__armor == "Cloak":
				return "Your Archer has 19 empty inventory slots with a cloak in the armor slot. 1 slot is being taken up by the Short Bow."
			else:
				return "Your Archer has 19 empty inventory slots and has " + self. __armor + " armor in the armor slot. 1 slot is being taken up by the Short Bow."
		else:
			if self.__armor == "None":
				return "Your Archer has 18 empty inventory slots with 1 empty armor slot. 2 inventory slots are taken by the Short Bow and a quiver filled with " + self.__arrow_type + " Arrows."
			elif self.__armor == "Cloak":
				return "Your Archer has 18 empty inventory slots with a cloak in the armor slot. 2 inventory slots are taken by the Short Bow and a quiver filled with " + self.__arrow_type + " Arrows."
			else:
				return "Your Archer has 18 empty inventory slots and has " + self. __armor + " armor in the armor slot. 2 inventory slots are taken by the Short Bow and a quiver filled with " + self.__arrow_type + " Arrows."

class Rogue(Character):
	def __init__(self, race, health=100, attack=100, speed=100, armor=None, knife_type=None, level=1):
		Character.__init__(self, race, health=100, attack=100, speed=100, armor=None, level=1)
		self.__class_item = "Dagger"
		self.__armor = armor
		self.__health = health
		self.__attack = attack
		self.__speed = speed
		self.__level = level


	def set_items(self, race, armor=None, knife_type=None, level=1):
		self.__knife_type = knife_type
		return "Item list compiled"

	def get_items(self, race, armor=None, knife_type=None, level=1):
		self.set_items(knife_type)
		self.__knife_type = knife_type
		if self.__knife_type != None:
			line = "Your Rogues held items are " + self.__knife_type + " Throwing Knives and a " + self.__class_item + "."
		else:
			line = "Your Rogues held item is a " + self.__class_item + "."
		return line

	def get_stats(self, race, armor=None, knife_type=None, level=1):
		self.set_stats(self)
		self.__health = str(self.__health)
		self.__attack = str(self.__attack)
		self.__speed = str(self.__speed)
		return "The stats of your level " + self.__level + " Rogue: \nHealth-" + self.__health + "\nAttack-" + self.__attack + "\nSpeed-" + self.__speed + "\nAttack Range-5 units"

	def set_stats(self, race, armor=None, knife_type=None, level=1):
		self.__level = int(self.__level)
		self.__health += (5 * self.__level)
		self.__attack += (5 * self.__level)
		self.__speed += (15 * self.__level)
		self.__level = str(self.__level)

	def characteristics(self, race, armor=None, knife_type=None, level=1):
		self.__race = race
		self.__class_item = "Dagger"
		self.__armor = armor
		self.__level = level
		self.__knife_type = knife_type
		self.__level = str(self.__level)
		self.__race = str(self.__race)
		self.__armor = str(self.__armor)
		self.__class_item = str(self.__class_item)
		self.__knife_type = str(self.__knife_type)
		return "Your character is a level " + self.__level + " Rogue of race " + self.__race + ", with " + self.__armor + " armor, a " + self.__class_item + ", and a Throwing Knives of " + self.__knife_type

	def inventory(self, race, armor=None, knife_type=None, level=1):
		self.__armor = str(armor)
		self.__knife_type = str(knife_type)
		if self.__knife_type == "None":
			if self.__armor == "None":
				return "Your Rogue has 19 empty inventory slots with 1 empty armor slot. 2 slot is being taken up by the Dagger."
			elif self.__armor == "Cloak":
				return "Your Rogue has 19 empty inventory slots with a cloak in the armor slot. 1 slot is being taken up by the Dagger."
			else:
				return "Your Rogue has 19 empty inventory slots and has " + self. __armor + " armor in the armor slot. 1 slot is being taken up by the Dagger."
		else:
			if self.__armor == "None":
				return "Your Rogue has 18 empty inventory slots with 1 empty armor slot. 2 inventory slots are taken by the Dagger and the " + self.__knife_type + " Throwing Knives."
			elif self.__armor == "Cloak":
				return "Your Rogue has 18 empty inventory slots with a cloak in the armor slot. 2 inventory slots are taken by the Dagger and the " + self.__knife_type + " Throwing Knives."
			else:
				return "Your Rogue has 18 empty inventory slots and has " + self. __armor + " armor in the armor slot. 2 inventory slots are taken by the Dagger and the " + self.__knife_type + " Throwing Knives."



def main():
	player = Brawler("Dwarf", armor="Steel",potion_type="Speed", level=15)
	player2 = Archer("Elf", armor="Leather", arrow_type="Ice", level=15)
	player3 = Rogue("Human", armor="Cloak", knife_type="Poison", level=15)
	print(Brawler.inventory(player, "Human", armor="Steel", potion_type="Speed", level=15))
	print(Archer.inventory(player2, "Elf", armor="Leather", arrow_type="Ice", level=15))
	print(Rogue.inventory(player3, "Human", armor="Cloak", knife_type="Poison", level=15))


if __name__ == "__main__":				#main function
	main()
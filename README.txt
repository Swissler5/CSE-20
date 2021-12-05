This class simulates video game console running a dnd character maker. The customizations include the race of your character, the armor they wear, which held item they have based of off the three optional type of fighter chosen by the child class, and their level to see the stat progression for the character.

The race serves as the backbone of the character whether is a human, elf, orc, or dwarf.
The optional armor is a cosmetic look that helds give the characters more personality.
The held item is a way to futhermore put personality into the character but this in the case of a support item.
The level is the progression system of the stats and helps the chooser see which class would have the stats they perfer at certain levels.

A race is required for the creation of your character, but the armor, held item and level are optional. The optional classes will be defaulteed to None, None and 1 respectivly.

These are the main customization for the character but any string will fit:
	race: Human, Elf, Dwarf, Orc
	armor: Steel, Leather, Chain Mail, Dragon Scale , Cloak
	potion types: Health, Speed, Strength
	arrow types: Normal, Ice, Fire
	knive_types: Normal, Poison, Electric
	
level can be any positive integer

Methods: race, armor, and the specialized item need to be strings while the level should to be an integer.
	set_items(race, armor, held item, level):
		This will store your held item of the character by setting the held item to the specialized fighter class variable.
	get_items(race, armor, held item, level):
		This will return the special class item as well as the specialized class variable showing the user what the player is holding.
	set_stats(race, armor, held item, level):
		Adjusts the stats of the character based on the level progression of each stat and what level they are. Each fighter class has a differnt stat progression.
	get_stats(race, armor, held item, level)
		This returns the stats at the given level and fighter class as well as their built in attack range.
	characteristics(race, armor, held item, level):
	This returns the discription of the character
	inventory(race, armor, held item, level):

The user can run the program by choosing their class, the most basic option is the Character class, then the Brawler class, the Archer class, and finally the Rogue class. The Character class get only a race and armor, and the level does not change the stats of the character. The Brawler class gains the held item potion_type, the Archer class gains the held item arrow_type, and the Rogue class gains the held item knife_type. All three of these subclasses gain a class bonuses for leveling up. Each class has different bonuses for these stats. The code entry follows:
player = ClassType("Race", armor="Armor", (specific_held_item)="held item", level=Integer)
The different methods follow:
	ClassType.set_items(player, "Race", armor="Armor", classbaseditem="held item", level=Integer))
	ClassType.get_items(player, "Race", armor="Armor", (classbaseditem="held item", level=Integer))
	ClassType.set_stats(player, "Race", armor="Armor", classbaseditem="held item", level=Integer))
	ClassType.get_stats(player, "Race", armor="Armor", classbaseditem="held item", level=Integer))
	ClassType.characteristics(player, "Race", armor="Armor", classbaseditem="held item", level=Integer))
	ClassType.inventory(player, "Race", armor="Armor", classbaseditem="held item", level=Integer))
The classbaseditem is different based on the Character class chosen.
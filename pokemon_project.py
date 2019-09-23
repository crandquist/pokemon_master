class Pokemon():
    def __init__(self, name, pokemon_type, level = 1):
        self.name = name
        self.level = level
        self.pokemon_type = pokemon_type
        self.max_health = level * 5
        self.current_health = level * 5
        self.is_knocked_out = False 
        self.experience = 0

    def __repr__(self):
        return '{name} is level {level} and has {health} hit points remaining.'.format(name = self.name, level = self.level, health = self.current_health)

    def level_up(self):
        if self.experience >= 10:
            self.level += 1
            return print('{name} is now level {level}!'.format(name = self.name, level = self.level))

    def knock_out(self):
        self.current_health = 0
        self.is_knocked_out = True
        return print(self.name + ' was knocked out!')

    def lose_health(self, damage):
        if damage > self.current_health:
            self.current_health = 0
            self.knock_out()
            return
        else:
            self.current_health -= damage
            return print('{name} has {health} hit points!'.format(name = self.name, health = self.current_health))
    
    def gain_health(self, health_gain):
        if self.is_knocked_out == True:
            self.revive()
        self.current_health += health_gain
        if self.current_health >= self.max_health:
            self.current_health = self.max_health
        return print('{name} has {health} hit points!'.format(name = self.name, health = self.current_health)) 

    def revive(self):
        if self.current_health == 0:
            self.current_health = 1
            self.is_knocked_out = False
            print(self.name + ' has been revived!')
    
    def attack(self, other_pokemon):
        if self.is_knocked_out == True:
            print(self.name + ' is knocked out and unable to attack!')
            return
        if (self.pokemon_type == "Fire" and other_pokemon.pokemon_type == "Grass") or (self.pokemon_type == "Grass" and other_pokemon.pokemon_type == "Water") or (self.pokemon_type == "Water" and other_pokemon.pokemon_type == "Fire"):
            damage = self.level * 2
            print(self.name + ' attacked ' + other_pokemon.name + ' for ' + str(damage) + ' damage!')
            print('It was super effective!')
            other_pokemon.lose_health(damage)
            self.experience += 1
            if self.experience >= 10:
                self.level_up()
            return
        if (self.pokemon_type == "Grass" and other_pokemon.pokemon_type == "Fire") or (self.pokemon_type == "Water" and other_pokemon.pokemon_type == "Grass") or (self.pokemon_type == "Fire" and other_pokemon.pokemon_type == "Water"):
            damage = round(self.level / 2)
            print(self.name + ' attacked ' + other_pokemon.name + ' for ' + str(damage) + ' damage!')
            print('It was not very effective!')
            other_pokemon.lose_health(damage)
            self.experience += 1
            if self.experience >= 10:
                self.level_up()
            return
        if (self.pokemon_type == other_pokemon.pokemon_type):
            damage = self.level
            print(self.name + ' attacked ' + other_pokemon.name + ' for ' + str(damage) + ' damage!')
            other_pokemon.lose_health(damage)
            self.experience += 1
            if self.experience >= 10:
                self.level_up()
            return

class Charmander(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Bulbasaur", "Grass", level)

class Trainer():
    def __init__(self, name, pokemon_list, num_potions):
        self.name = name
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0

    def __repr__(self):
        return "{name} has {pokemon} Pokemon and {potions} potion(s). {active} is their active Pokemon.".format(name = self.name, pokemon = len(self.pokemons), potions = self.potions, active = self.pokemons[self.current_pokemon].name)
    
    def use_potion(self):
        if self.potions > 0:
            self.potions -= 1
            active_pokemon = self.pokemons[self.current_pokemon]
            print(self.name + ' used a potion!')
            active_pokemon.gain_health(active_pokemon.max_health)
        else:
            return 'You do not have any potions!'
    
    def attack_trainer(self, other_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

    def switch_pokemon(self, new_active):
        if new_active in self.pokemons:
            for pokemon in self.pokemons:
                if new_active.name == pokemon.name and pokemon.is_knocked_out == False:
                    self.current_pokemon = self.pokemons.index(new_active)
                    print('{name}, I choose you!'.format(name = new_active))
                    return
                elif new_active.name == pokemon.name and pokemon.is_knocked_out == True:
                    print(new_active.name + ' is knocked out and is not able to be your active Pokemon.')
                    return
        else:
            print('You do not have this pokemon.')



#Time to test all of the things!

#Pokemon
charmander = Pokemon("Charmander", "Fire", 9)
squirtle = Pokemon("Squirtle", "Water", 10)
bulbasaur = Pokemon("Bulbasaur", "Grass", 12)
growlithe = Pokemon("Growlithe", "Fire")
caterpie = Pokemon("Caterpie", "Grass")
magikarp = Pokemon("Magikarp", "Water")
pikachu = Pokemon("Pikachu", "Electic")

#Trainers
cat = Trainer("Cat", [growlithe, squirtle], 1)
grimus = Trainer("Grimus", [charmander, caterpie], 1)
atra = Trainer("Atra", [bulbasaur, magikarp], 1)

#Training Grounds

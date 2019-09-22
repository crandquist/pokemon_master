class Pokemon():
    def __init__(self, name, pokemon_type, level = 1):
        self.name = name
        self.level = level
        self.pokemon_type = pokemon_type
        self.max_health = level * 5
        self.current_health = level * 5
        self.is_knocked_out = False 

    def __repr__(self):
        return '{name} is level {level} and has {health} hit points remaining.'.format(name = self.name, level = self.level, health = self.current_health)

    def knock_out(self):
        self.current_health = 0
        self.is_knocked_out = True
        return self.name + ' is knocked out!'

    def lose_health(self, health_lost):
        if health_lost > self.current_health:
            self.current_health = 0
            self.knock_out
            return
        else:
            self.current_health -= health_lost
            return self.name + ' now has ' + str(self.current_health) + ' health.'
    
    def gain_health(self, health_gain):
        self.current_health += health_gain
        if self.current_health >= self.max_health:
            self.current_health = self.max_health
        return self.name + ' now has ' + str(self.current_health) + ' health.'

    def revive(self):
        if self.current_health == 0:
            self.current_health = 1
            print(self.name + ' has been revived!')
    
    def attack(self, other_pokemon):
        if self.is_knocked_out == True:
            print(self.name + ' is knocked out and unable to attack!')
            return
        if (self.pokemon_type == "Fire" and other_pokemon.pokemon_type == "Grass") or (self.pokemon_type == "Grass" and other_pokemon.pokemon_type == "Water") or (self.pokemon_type == "Water" and other_pokemon.pokemon_type == "Fire"):
            damage = self.level * 2
            other_pokemon.lose_health(damage)
            print(self.name + ' attacked ' + other_pokemon.name + ' for ' + str(damage) + '!')
            print('It was super effective!')
            return
        if (self.pokemon_type == "Grass" and other_pokemon.pokemon_type == "Fire") or (self.pokemon_type == "Water" and other_pokemon.pokemon_type == "Grass") or (self.pokemon_type == "Fire" and other_pokemon.pokemon_type == "Water"):
            damage = round(self.level / 2)
            other_pokemon.lose_health(damage)
            print(self.name + ' attacked ' + other_pokemon.name + ' for ' + str(damage) + '!')
            print('It was not very effective!')
        if (self.pokemon_type == other_pokemon.pokemon_type):
            damage = self.level
            other_pokemon.lose_health(damage)
            print(self.name + ' attacked ' + other_pokemon.name + ' for ' + str(damage) + '!')

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
            active_pokemon.current_health = active_pokemon.max_health
            print(self.name + ' used a potion!')
            print(active_pokemon + ' now has ' + str(active_pokemon.max_health)+ '!')
        else:
            return 'You do not have any potions!'
    
    def attack_trainer(self, other_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

    def switch_pokemon(self, new_active):
        for pokemon in self.pokemons:
            if new_active == pokemon and pokemon.is_knocked_out == False:
                self.current_pokemon = self.pokemons[new_active].index
            elif new_active == pokemon and pokemon.is_knocked_out == True:
                print(new_active + ' is knocked out and is not able to be your active Pokemon.')
            else: 
                print('You do not have this Pokemon.')



#Time to test all of the things!

#Pokemon
charmander = Pokemon("Charmander", "Fire", 9)
print(charmander)
squirtle = Pokemon("Squirtle", "Water", 10)
bulbasaur = Pokemon("Bulbasaur", "Grass", 12)
growlithe = Pokemon("Growlithe", "Fire")
caterpie = Pokemon("Caterpie", "Grass")
magikarp = Pokemon("Magikarp", "Water")

#Trainers
cat = Trainer("Cat", [growlithe, squirtle], 1)
print(cat)
grimus = Trainer("Grimus", [charmander, caterpie], 1)
atra = Trainer("Atra", [bulbasaur, magikarp], 1)
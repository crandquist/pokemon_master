class Pokemon():
    def __init__(self, name, pokemon_type, level = 1):
        self.name = name
        self.level = level
        self.pokemon_type = pokemon_type
        self.max_health = level * 5
        self.current_health = level * 5
        self.is_knocked_out = False 

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
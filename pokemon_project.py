class Pokemon():
    def __init__(self, name, level, pokemon_type, max_health, current_health, knocked_out):
        self.name = name
        self.level = level
        self.pokemon_type = pokemon_type
        self.max_health = max_health
        self.current_health = current_health
        self.is_knocked_out = knocked_out 

    def lose_health(self, health_lost):
        self.current_health -= health_lost
        return self.name + ' now has ' + str(self.current_health) + ' health.'
    
    def gain_health(self, health_gain):
        self.current_health += health_gain
        return self.name + ' now has ' + str(self.current_health) + ' health.'
    
    def kock_out(self):
        if self.current_health <= 0:
            self.is_knocked_out = True
            return self.name + ' is knocked out!'
    
    def revive(self):
        if self.current_health >= 0:
            self.is_knocked_out = False
            return self.name + ' has been revived!'
    
    def attack(self, other_pokemon):
        pass
    
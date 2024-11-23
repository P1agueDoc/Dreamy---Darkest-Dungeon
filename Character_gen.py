class char_gen():
    def __init__(self, name, size_type, class_of_char, race, character_class, attack, defense,
                 evasion, preception, armour, boots, hat, mask, gloves, weapon, pants):
        self.name = name
        self.size_type = size_type
        self.class_of_char = class_of_char
        self.race = race
        self.character_class = character_class
        self.attack = attack
        self.defense = defense
        self.evasion = evasion
        self.preception = preception
        self.armour = armour
        self.boots = boots
        self.hat = hat
        self.mask = mask
        self.gloves = gloves
        self.weapon = weapon
        self.pants = pants

    def write_into_save(self, player_number, save_name):
        pass

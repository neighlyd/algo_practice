ITEMS = {
    'Lantern': {
        'weight': 0.1,
        'description': 'A light'
    },
    'Bat Wing': {
        'weight': 0.1,
        'description': 'A leathery, tattered wing of a sky rat.',
        'price': 1
    },
}

WEAPONS = {
    'Sword': {
        'weight': 5.0,
        'atk_mod': 2,
        'slots': ['main_hand'],
        'price': 50,
        'description': 'A family heirloom that has seen better days.'
    },
    'Dagger': {
        'weight': 0.5,
        'atk_mod': 0,
        'slots': ['main_hand', 'off_hand'],
        'price': 25,
        'description': 'More rust now than metal; twisted and evil.'
    },
    'Staff': {
        'weight': 1.0,
        'atk_mod': 0,
        'slots': ['main_hand'],
        'price': 10,
        'description': 'A gnarled walking staff that you have used all your life.'
    }
}


class Item:

    def __init__(self, name=None, description=None, weight=None, price=0):
        self.name = name
        self.description = description
        self.weight = weight
        self.price = price


class Equipment(Item):

    def __init__(self, adjectives=None, lvl=0, slots=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adjectives = adjectives
        self.level = lvl
        self.slots = slots
        self.equipped = False


class Weapon(Equipment):

    def __init__(
            self,
            atk_mod=0.0,
            dam_min=0,
            dam_max=None,
            dam_type=None,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.atk_mod = atk_mod
        self.dam_min = dam_min
        self.dam_max = dam_max
        self.dam_type = dam_type


class Armor(Equipment):

    def __init__(self, phys_def=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phys_def = phys_def


def spawn_item(item):
    item = item.title()
    if item in ITEMS:
        return Item(name=item, **ITEMS[item])
    elif item in WEAPONS:
        return Weapon(name=item, **WEAPONS[item])


s = spawn_item('sword')
l = spawn_item('lantern')
b = spawn_item('bat wing')

print(s.name, s.atk_mod, s.price)
print(l.name, l.weight, l.price)
print(b.name)

class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self._available_dishes = set(self.INGREDIENTS.keys())
        self._total_ingredients = {}

        for value in self.INGREDIENTS.values():
            for ingredient in value:
                self._total_ingredients[ingredient] = 0

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if (
                self._total_ingredients[ingredient]
                < self.MINIMUM_INVENTORY[ingredient]
            ):
                self._total_ingredients[ingredient] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self._total_ingredients

    def get_available_dishes(self):
        for used_ingredient, used_value in self._total_ingredients.items():
            if used_value == self.MINIMUM_INVENTORY[used_ingredient]:
                for dish, ingredients in self.INGREDIENTS.items():
                    if used_ingredient in ingredients:
                        self._available_dishes.discard(dish)
        return self._available_dishes

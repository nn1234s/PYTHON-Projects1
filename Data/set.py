burger_ingredients = {"tomato","cheese","capsicum","chilli","2bun","garlic","2bun"}
chips_ingredients = {"tomato","cheese","capsicum","peri peri","potato","garlic","2bun"}

print(burger_ingredients) # Burger ingredients
print(len(burger_ingredients)) # 6 not 7

burger_ingredients.add("patty")
burger_ingredients.discard("garlic")
print(burger_ingredients)
all_ingredients = burger_ingredients.union(chips_ingredients)
common = burger_ingredients.intersection(chips_ingredients)
print("All Ingredients:", all_ingredients)
print("Common:",common)
only_pasta = burger_ingredients.difference(chips_ingredients)
unique_to_each = burger_ingredients.symmetric_difference(chips_ingredients)
print("Only In Burger:",only_pasta)
#burger_ingredients = {"tomato","cheese","capsicum","chilli","2bun","garlic","2bun"}

print("NotShared:",unique_to_each)

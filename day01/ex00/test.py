from book import Book
from recipe import Recipe
import datetime


rbook = Book("The Book", datetime.date(2019, 11, 4), datetime.date(2019, 11, 1), {'starter': [], 'lunch': [], 'dessert': []})
r1 = Recipe("gateau", 3, 60, ["ing1", "ing2", "ing3"], "d1", "lunch")
r2 = Recipe("crepe", 3, 60, ["ing1", "ing2", "ing3"], None, "dessert")
r3 = Recipe("tarte", 3, 60, ["ing1", "ing2", "ing3"], "d3", "starter")
r4 = Recipe("flan", 1, 6, ["ing1", "ing2", "ing3"], "d4", "starter")

rbook.add_recipe(r1)
rbook.add_recipe(r2)
rbook.add_recipe(r3)
rbook.add_recipe(r4)

rbook.get_recipe_by_name('gateau')
rbook.get_recipe_by_name('flan')
rbook.get_recipe_by_name('tarte')
rbook.get_recipe_by_name('crepe')

rbook.get_recipes_by_types('starter')
rbook.get_recipes_by_types('lunch')
rbook.get_recipes_by_types('dessert')

import sys
from datetime import date
from recipe import Recipe


class Book:
    def __init__(self, name, lu, cd, rl):
        if (isinstance(name, str) is False or not name
            or isinstance(lu, date) is False
            or isinstance(cd, date) is False
            or isinstance(rl, dict) is False
            or ('starter' not in rl.keys() and 'lunch' not in rl.keys() and 'dessert' not in rl.keys())):
            print('TypeError: the Book class should be instanced with the following arguments:')
            sys.stdout.write('Book(name (str), last_update (date), ')
            sys.stdout.write('creation_date (date), recipe_list (dict))\n')
        self.name = name
        self.last_update = lu
        self.creation_date = cd
        self.recipes_list = rl


    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for rec_type in self.recipes_list:
            for rec in self.recipes_list[rec_type]:
                if (rec.name == name):
                    print(str(rec))
                    return rec
        print("Error, this recipe doesn\'t exists.")


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if (isinstance(recipe_type, str) is False or 
            recipe_type not in self.recipes_list.keys()):
            print("Error, this type doesn\'t exists.")
        else:
            print("Here are the recipes of type \'" + recipe_type + "\':")
            for rec in self.recipes_list[recipe_type]:
                print(rec.name)


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe) is False:
            print("Cannot add this, it is not a recipe.")
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = date.today()

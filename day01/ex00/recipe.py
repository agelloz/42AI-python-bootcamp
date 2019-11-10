import sys


class Recipe:
    def __init__(self, name, cl, ct, ing, desc, rt):
        if (isinstance(name, str) is False or not name
            or isinstance(cl, int) is False or cl < 1 or cl > 5
            or isinstance(ct, int) is False or ct < 0
            or isinstance(ing, list) is False or not ing[0]
            or (isinstance(desc, str) is True and not desc) 
            or (isinstance(desc, str) is False and desc)
            or isinstance(rt, str) is False or rt not in ('starter', 'lunch', 'dessert')):
            print('TypeError: the Recipe class should be instanced with the following arguments:')
            sys.stdout.write('Recipe(name (str), cooking_lvl (int, range 1 to 5),\n')
            sys.stdout.write('cooking_time in minutes (positive int), ')
            sys.stdout.write('ingredients (list of str),\ndescription (str, none), recipe_type (str))\n')
            exit()
        self.name = name
        self.cooking_lvl = cl
        self.cooking_time = ct
        self.ingredients = ing
        self.description = desc
        self.recipe_type = rt


    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "The " + self.name + " recipe has a difficulty of " + str(self.cooking_lvl)
        txt += "/5 and a cooking time of " + str(self.cooking_time) + " min.\n"
        txt += "The ingredients for this " + self.recipe_type  + " are:\n"
        for ing in self.ingredients:
            txt += ing + "\n"
        if (self.description is not None):
            txt += "Here is a description of the recipe:\n" + self.description    
        return txt

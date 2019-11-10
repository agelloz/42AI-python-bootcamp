import sys

cookbook = {
    'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': '10'},
    'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': '60'},
    'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': '15'}
    }


def add_recipe(key):
    if key in cookbook:
        print("Recipe exists already.")
    else:
        ing = []
        sys.stdout.write("Recipe's ingredients (end with 0)?\n>> ")
        i = input()
        while (i != '0'):
            ing.append(i)
            sys.stdout.write("Recipe's ingredients (end with 0)?\n>> ")
            i = input()
        sys.stdout.write("Recipe's meal type?\n>> ")
        meal = input()
        sys.stdout.write("Recipe's preparation time?\n>> ")
        prep = input()
        cookbook[key] = {'ingredients': ing, 'meal': meal, 'prep_time': prep}
        print("Recipe successfully added.")


def delete_recipe(key):
    if key in cookbook:
        del cookbook[key]
        print("Recipe successfully deleted.")
    else:
        print("Recipe unknown.")


def print_recipe(key):
    if key in cookbook:
        print("Ingredients list: " + str(cookbook[key]['ingredients']))
        print("Meal: " + str(cookbook[key]['meal']))
        print("Preparation time: " + str(cookbook[key]['prep_time']) + " min")
    else:
        print("Recipe unknowned.")


sys.stdout.write('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> ')
a = input()
while (a != '5'):
    if (a == '1'):
        sys.stdout.write("Please enter the recipe's name to create it:\n>> ")
        key = input()
        add_recipe(key)
    elif (a == '2'):
        sys.stdout.write("Please enter the recipe's name to delete it:\n>> ")
        key = input()
        delete_recipe(key)
    elif (a == '3'):
        sys.stdout.write("Please enter the recipe's name to get its details:\n>> ")
        key = input()
        print_recipe(key)
    elif (a == '4'):
        print(cookbook)
    else:
        sys.stdout.write("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")
    sys.stdout.write('>> ')
    a = input()
print("Cookbook closed.")

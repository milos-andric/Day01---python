class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if(check_name(name) is False):
            exit()
        self.name = name
        if(check_lvl(cooking_lvl) is False):
            exit()
        self.cooking_lvl = cooking_lvl
        if(check_time(cooking_time) is False):
            exit()
        self.cooking_time = cooking_time
        if(check_ing(ingredients) is False):
            exit()
        self.ingredients = ingredients
        self.description = description
        if(check_type(recipe_type) is False):
            exit()
        self.recipe_type = recipe_type

    def __str__(self):
        txt = "name : " + self.name + "\n"
        txt += "cooking_lvl : " + str(self.cooking_lvl) + "\n"
        txt += "cooking_time : " + str(self.cooking_time) + "\n"
        txt += "ingredients : " + str(self.ingredients) + "\n"
        txt += "description : " + self.description + "\n"
        txt += "type : " + self.recipe_type
        return txt


def check_name(name):
    if len(name) == 0:
        print("Please provide a name")
        return (False)
    return(True)


def check_lvl(num):
    try:
        num = int(num)
        if (num < 0) or (num > 5):
            print("Please provide a number in correct range for cooking level")
            return (False)
        return(True)
    except ValueError:
        print('Please provide a number for the cooking level')
        return(False)


def check_time(num):
    try:
        num = int(num)
        if (num < 0):
            print("Please provide a positive time for the recipe")
            return (False)
        return(True)
    except ValueError:
        print('Please provide a number for the cooking time')
        return(False)


def check_ing(ings):
    for ing in ings:
        if (isinstance(ing, str) is False):
            print('please provide only strings for ingredients')
            return(False)
    return(True)


def check_type(type):
    if (type == 'starter' or type == 'lunch' or type == 'dessert'):
        return(True)
    else:
        print('Meal type can either be "lunch", "starter" or "dessert"')
        return(False)

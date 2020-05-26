import datetime

date_frm = '%Y-%m-%d'


class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        if(check_name(name) is False):
            exit()
        self.name = name
        try:
            last_update = datetime.datetime.strptime(last_update, date_frm)
        except ValueError:
            print("Incorrect format for last update, should be YYYY-MM-DD")
            exit()
        self.last_update = last_update
        try:
            creation_date = datetime.datetime.strptime(creation_date, date_frm)
        except ValueError:
            print("Incorrect format for creation date, should be YYYY-MM-DD")
            exit()
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        for i in self.recipes_list:
            for j in self.recipes_list[i]:
                if(j.name == name):
                    print(j)
                    return(j)

    def get_recipes_by_types(self, recipe_type):
        for types in self.recipes_list:
            if types == recipe_type:
                for rec in self.recipes_list[types]:
                    print(rec)
                    print('\n')

    def add_recipe(self, recipe):
        for types in self.recipes_list:
            if types == recipe.recipe_type:
                self.recipes_list[types].append(recipe)


def check_name(name):
    if len(name) == 0:
        print("Please provide a name")
        return (False)
    return(True)

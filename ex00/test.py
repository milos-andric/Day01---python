from recipe import Recipe
from book import Book

date_string = '2020-12-31'

list_pud = ['jelly', 'agaragar']
list_tir = ['eggs', 'mascarpone', 'coffe', 'biscuits']
list_cla = ['eggs', 'milk', 'cherry', 'sugar']
Pudding = Recipe("pudding", 3, 40, list_pud, "description", 'dessert')
Tiramisu = Recipe("Tiramisu", 2, 40, list_tir, "gateau pour robz", 'dessert')
Clafoutis = Recipe("Clafoutis", 2, 40, list_cla, "gateau cool", 'dessert')

list_mor = ['chicken', 'cream', 'wine', 'morels']
list_sal = ['salad', 'zuchini', 'eggplant']
Morels = Recipe("Poulet aux morilles", 3, 50, list_mor, "poulet ouf", 'lunch')
Salad = Recipe("Salade composee", 1, 5, list_sal, "salad", 'starter')

dict_rec = {
            'starter': [Salad],
            'lunch': [Morels],
            'dessert': [Pudding, Tiramisu, Clafoutis]
            }
CookBook = Book('CookBook', date_string, date_string, dict_rec)
CookBook.get_recipes_by_types('lunch')
list_foc = ['flour', 'yeast', 'water']
Foccacia = Recipe("Foccacia", 4, 50, list_foc, "une ouf foccacia", 'lunch')
CookBook.add_recipe(Foccacia)
CookBook.get_recipes_by_types('lunch')

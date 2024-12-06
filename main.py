
pizzas = ["4 fromages", "Véhétarienne", "Hawai", "Calzone"]

def print_pizza(collection):
    print(f"---- LISTE DES PIZZAS ({len(collection)})----")
    if not collection:
        print("AUCUNE PIZZA")
    else:
        for pizza in collection:
            print(pizza)
        print()
        print(f"# La prémière pizza : {collection[0]}")
        print(f"# La dernière pizza : {collection[-1]}")


"""
def user_add_pizza(collection):
    user = input("Pizza à ajouter : ")
    add_pizza = user
    collection = collection + (add_pizza,)
    return collection
"""
def pizza_exist(user, collection):
    if user in collection:
        return False
    else:
        return True


def user_add_pizza(collection):
    user_add = input("Pizza à ajouter : ")
    if pizza_exist(user_add, collection) is False:
        print("Erreur la pizza existe déjà dans la liste !")
    else:
        collection.append(user_add)
    


empty_pizza_list = ()

user_add_pizza(pizzas)

print_pizza(pizzas)

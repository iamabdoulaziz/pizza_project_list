
pizzas = ("4 fromages", "Véhétarienne", "Hawai", "Calzone")

def print_pizza():
    print(f"---- LISTE DES PIZZAS ({len(pizzas)})----")
    for pizza in pizzas:
        print(pizza)


print_pizza()

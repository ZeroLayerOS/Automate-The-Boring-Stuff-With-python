# pizza.py - a module: a separate file that holds functions we want to reuse.


def make_pizza(size, *toppings):
    """Print the size of the pizza and every topping requested."""
    # *toppings collects all extra arguments after `size` into a tuple.
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    # Loop over the tuple and print each topping on its own line.
    for topping in toppings:
        print(f"- {topping}")

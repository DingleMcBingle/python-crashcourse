sandwich_orders = ['ham','turkey','tuna']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("All sandwiches have been made.")
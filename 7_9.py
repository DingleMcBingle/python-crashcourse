sandwich_orders = ['ham','turkey','tuna','pastrami','pastrami','pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("All sandwiches have been made.")
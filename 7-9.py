sandwich_orders = [
    'Tuna Sandwich',
    'Pastrami',
    'Chicken Sandwich',
    'Pastrami',
    'Veggie Sandwich',
    'Pastrami'
]

finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.\n")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

def cartesian_product(sets):
    if not sets:
        return {()}
    result = set()
    for element in sets[0]:
        for product in cartesian_product(sets[1:]):
            result.add((element,) + product)
    return result

x = {4, 7}
y = {3, 2}
z = {1, 5}
print(cartesian_product([x, y, z]))
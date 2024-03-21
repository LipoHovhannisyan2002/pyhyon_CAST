def numberOfWeakCharacters(properties):
    properties.sort(key=lambda x: (-x[0], x[1]))
    
    weak_count = 0
    max_defense = float('-inf')

    for attack, defense in properties:
        if defense < max_defense:
            weak_count += 1
        else:
            max_defense = defense

    return weak_count


properties = [[5, 5], [6, 3], [3, 6]]
print(numberOfWeakCharacters(properties))
properties = [[2, 2], [3, 3]]
print(numberOfWeakCharacters(properties))
properties = [[1, 5], [10, 4], [4, 3]]
print(numberOfWeakCharacters(properties))

def numberOfWeakCharacters(properties):
        weak_count = 0
        for  i in range(len(properties)):
            is_weak = False
            current_attack,current_defense = properties[i]
            for j in range(len(properties)):
                if i!=j:
                    their_attack, other_defense = properties[j]
                    if their_attack > current_attack and other_defense > current_defense:
                        is_weak = True
                        break
            if is_weak:
                weak_count +=1
        return weak_count


properties = [[5,5],[6,3],[3,6]]
print(numberOfWeakCharacters(properties))
properties = [[2,2],[3,3]]
print(numberOfWeakCharacters(properties))
properties = [[1,5],[10,4],[4,3]]
print(numberOfWeakCharacters(properties))
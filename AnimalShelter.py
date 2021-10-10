from Animal import Animal

class AnimalShelter:
    
    def __init__(self):
        self.dict1 = {}

    def addAnimal(self, animal):
        if animal.species in self.dict1:
           l = self.dict1[animal.species]
           l.append(animal)
           self.dict1[animal.species] = l
        elif animal.species not in self.dict1:
            self.dict1[animal.species] = [animal]

    def removeAnimal(self, animal):
        if animal.species in self.dict1:
            if self.doesAnimalExist(animal):
                for i in range(len(self.dict1[animal.species])):
                    if (self.dict1[animal.species][i].weight == animal.weight) and (self.dict1[animal.species][i].species == animal.species) and (self.dict1[animal.species][i].name == animal.name) and (self.dict1[animal.species][i].age == animal.age):
                        x = i
                        self.dict1[animal.species].pop(x)
                        return True
                    else:
                        return False
            else:
               # print("You have tried to remove an non-existing animal.")
                return False
        else:
            return False

    def getAnimalsBySpecies(self, species):
        species1 = species.upper()
        z = ""
        if species1 not in self.dict1:
            return z
        elif species1 in self.dict1:
            l = self.dict1[species1]
            for i in range(len(l)):
                if i in range (len(l) - 1):
                    z = z +(l[i].toString()) + "\n"
                else:
                    z = z +(l[i].toString())
            return z

    def doesAnimalExist(self, animal):
        if animal.species not in self.dict1:
            return False
        elif animal.species in self.dict1:
            l = self.dict1.get(animal.species)
            for i in range(len(l)):
                if (l[i].weight == animal.weight) and (l[i].species == animal.species) and (l[i].name == animal.name) and (l[i].age == animal.age):
                    return True
        else:
            return False

    # def __eq__(self, rhs):
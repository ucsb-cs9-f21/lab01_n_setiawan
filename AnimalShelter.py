from Animal import Animal

class AnimalShelter:
    
    def __init__(self):
        self.dict1 = {}

    def addAnimal(self, animal):
        self.dict1[animal.species] = list.append(animal)

        keyList = list(self.dict1.keys())

        for i in range(len(keyList)):
            self.dict1[keyList[i]] = len(self.dict1)

        

    def removeAnimal(self, animal):
        if (self.dict1.get(animal.species) == None) and (self.dict)
            print("You have tried to remove an non-existing object.")
        elif self.dict1.get(animal.species) == True:

    def getAnimalBySpecies(self, species):


    def doesAnimalExist(self, animal):
        if self.dict1.get(animal.species) == None:
            return False
        elif self.dict1.get(animal.species) == True:
            animal.species = 

As = AnimalShelter()
a = Animal("dog", 23.3, 12, "JUDG")
b = Animal("cat", 23.3, 34, "Monev")

As.addAnimal(b)
print(As.dict1[a])

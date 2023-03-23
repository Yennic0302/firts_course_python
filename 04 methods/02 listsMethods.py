List = list([])

myFruits = ["banana", "apple", "watermelon", "pear"]
my_objects = ("hammer", "phone", "toy")
anotherArray = list(myFruits)

myFruits.append('phrase')
myFruits.insert(2, "cambur")
myFruits.extend(["pear", "apple"])

anotherArray.pop(2)
myFruits.remove("pear")
anotherArray.clear()

myFruits.sort()
myFruits.reverse()


print(len(myFruits))
print(myFruits)
print(anotherArray)


print(my_objects.index('hammer'))
print(my_objects.count('hammer'))


my_set = set(['yender','el pepee'])
my_set.add('pollo')
my_set.add('arroz')
my_objects

print(dir(my_set))
print(my_set)
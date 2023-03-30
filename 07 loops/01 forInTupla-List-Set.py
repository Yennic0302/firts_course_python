array = ("perro","gato","cocodrile")
numbs = (1,2,34)
my_set = {"horse","dog","cat"}

for animal in array:
    print(array.index(animal))


result = 0

for numb in numbs:
    result = result + numb

print(result)

for animal,numb in zip(array,numbs): 
    print(f"{animal} {numb}")

for animal in range(len(array)):
    print(array[animal])


#for else 
for index, animal in enumerate(array):
    print(index, animal)
else:
    print('el bucle termino')

# use of for in set

for index,animal in enumerate(my_set):
    print(index, animal)
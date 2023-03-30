fruits = ["banana", 'apple',"watermelon",'pharse']
numbs = [1,2,3,4]

for fruit in fruits:
    if fruit == "apple":
      continue
    if fruit == 'pharse':
      print("cause stomathead")
      break
    print(fruit)

text = "what is there for the deenin"

for letter in text:
  print(letter)

""" numbsTimes2 = list()

for numb in numbs:
  numbsTimes2.append(numb*2)

print(numbsTimes2) """

numbsTimes2 = [x*2 for x in numbs]
print(numbsTimes2)
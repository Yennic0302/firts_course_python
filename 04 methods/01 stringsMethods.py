string1 = "hello i am yender"
string2 = "welcometomyComputer"
string3 = "3hh"

print(dir(string1))

Upper = string1.upper()
Lower = string1.lower()
Capitalize = string2.capitalize()

Find = string1.find("i")
Index = string1.index("a") # if there is no some coincidence it throws an error

Is_numeric = string3.isnumeric()
Is_alpha = string2.isalpha()

Count = string1.count("a")
Len = len(string1)

Ends_with = string2.endswith("la")
Starts_with = string2.startswith("lo")

Replace = string1.replace ('i', "lo")


Split = string2.split(" ")
Join = string1.join(string2)

print(Split)
print(Find)
print(Capitalize)
print(Is_numeric)
print(Is_alpha)
print(Count)
print(Len)
print(Replace)
print(Join)



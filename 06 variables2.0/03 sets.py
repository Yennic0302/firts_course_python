my_set = frozenset(["dato 1", "dato 2"])
print(my_set)

conjunto = {"el pepe", my_set}

print(conjunto)
let = {
    "name": "yender"
}

set_numb = {1,3,5,7,9}
set_numb_2 = {1,7,9}
set_numb_3 = {2,4,6}

resultado1 = set_numb_2.issubset(set_numb)
resultado2 = set_numb_2 <= set_numb

resultado3 = set_numb_2.issuperset(set_numb)
resultado4 = set_numb_2 > set_numb

resultado5 = set_numb_2.isdisjoint(set_numb_3)

print(resultado1)
print(resultado2)
print(resultado5)
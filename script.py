#!/usr/bin/pyhton
# coding: utf-8

from random import randint

chefs=["Antoine", "Gabrielle", "Julian", "Olivier"]
equipages=["François", "Achille", "Aquiles", "Filles"]
 
while len(equipages) != 0 :
    indexChef = randint(0, len(equipages) - 1)
    chef = chefs[indexChef]
    indexEq = randint(0, len(equipages) - 1)
    eq = equipages[indexEq]
    print "{0} goes with {1}".format(chef, eq)
    del equipages[indexEq]
    del chefs[indexChef]


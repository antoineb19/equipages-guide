#!/usr/bin/env python3
# coding: utf-8

import random, time

chefs=["Antoine", "Gabrielle", "Julian", "Olivier"]
equipages=["François", "Achille", "Aquiles", "Filles"]

for countdown in range(5,0,-1):
	print (countdown)
	time.sleep(1)
 
while len(equipages) != 0 :
    indexChef = random.SystemRandom().randint(0,len(equipages)-1)
    chef = chefs[indexChef]
    indexEq = random.SystemRandom().randint(0,len(equipages)-1)
    eq = equipages[indexEq]
    print ("{0} goes with {1}".format(chef, eq))
    del equipages[indexEq]
    del chefs[indexChef]


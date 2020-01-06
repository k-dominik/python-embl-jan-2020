
#The code below will run on a label-printer for chicken eggs. A digital scale will report a chicken egg mass (in grams) to the computer and then the computer will print a label.
# Please re-write the code so that the if-block is folded into a function.

import random
 for i in range(10):

    # simulating the mass of a chicken egg
    # the (random) mass will be 70 +/- 20 grams
    mass=70+20.0*(2.0*random.random()-1.0)

    print(mass)

    #egg sizing machinery prints a label
    if(mass>=85):
       print("jumbo")
    elif(mass>=70):
       print("large")
    elif(mass<70 and mass>=55):
       print("medium")
    else:
       print("small")

#The simplified program follows. What function definition will make it functio
import random
for i in range(10):
    # simulating the mass of a chicken egg
    # the (random) mass will be 70 +/- 20 grams
    mass=70+20.0*(2.0*random.random()-1.0)
    print(mass,print_egg_label(mass))

#Create a function definition for print_egg_label() that will work with the revised program above. Note, the function’s return value will be significant. Sample output might be "71.23 large".
#A dirty egg might have a mass of more than 90 grams, and a spoiled or broken egg will probably have a mass that’s less than 50 grams. Modify your print_egg_label() function to account for these error conditions. Sample output could be "25 too light, probably spoiled".

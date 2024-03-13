#!/usr/bin/env python3
# 📚 Review With Students:
    # Introduction to Object Oriented programming, classes, instances, methods

# Importing the pet / owner classes 
from lib.pet import Pet
# from lib.cat import *

# Instance of the Pet class
cookie = Pet(name='cookie', age=1, breed='Dachshund', temperament='hyper')

# Instance of the Cat class
# grace = Cat('grace', 7, 'domestic longhair', 'affectionate', True)
if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
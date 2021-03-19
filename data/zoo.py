
"""data.py: Importing and preprocessing the Zoo-dataset from UCI. http://archive.ics.uci.edu/ml/datasets/Zoo """

__author__ = "Majd Jamal"

import numpy as np

data = np.loadtxt('data/zoo.txt', delimiter=',', dtype='str')

names = data[:, 0]	#used for annotations
y_animals = data[:,-2].astype('int')

x_animals = data[:, 1:-2].astype('float')

"""Modifying number of legs from numeric to bolean.
The intuition is that most land animals
has two or four legs. Such aimals are set to True, and
the rest False.
"""
x_legs = x_animals[:, 12]
x_legs = np.where(x_legs == 4, 2, x_legs)   #If animal has 4 legs, set value to 2, so that we can change it later to 1.
x_legs = np.where(x_legs == 2, 1, 0)
x_animals[:, 12] = x_legs

x_animals = x_animals.T

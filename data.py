
"""data.py: Importing and preprocessing the Zoo-dataset from UCI. http://archive.ics.uci.edu/ml/datasets/Zoo """

__author__ = "Majd Jamal"

import numpy as np

data = np.loadtxt('zoo.txt', delimiter=',', dtype='str')

names = data[:, 0]	#used for annotations
y = data[:,-1]
x = data[:, 1:-2].astype('int')

"""Modifying number of legs from numeric to bolean.
The intuition is that most land animals
has two or four legs. Such aimals are set to True, and
the rest False.
"""
x_legs = x[:, 12]
x_legs = np.where(x_legs == 4, 1, x_legs)
x_legs = np.where(x_legs == 2, 1, 0)
x[:, 12] = x_legs

x = x.T

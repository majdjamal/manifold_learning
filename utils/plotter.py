
"""plotter.py: Contains plotter functions for the experiments. """

__author__ = "Majd Jamal"

import matplotlib.pyplot as plt
import numpy as np


def swiss3D(X, color):
	""" Plotter for the Swiss Roll. It scatters
		data points in 3D. 
	:param X: Data Matrix with shape = (Ndim, Npts)
	:param color: Coloring of the data points 
	"""
	plt.style.use('ggplot')
	ax = plt.axes(projection='3d')
	ax.scatter3D(X[0], X[1], X[2], c = color, cmap="rainbow")
	ax.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False)
	plt.show()

def swiss(X, color):
	""" Plotter for the Swiss Roll. It scatters
		data points in 2D. 
	:param X: Data Matrix with shape = (Ndim, Npts)
	:param color: Coloring of the data points 
	"""
	plt.style.use('ggplot')
	plt.scatter(X[0], X[1], c=color, cmap='rainbow')
	plt.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False)
	plt.show()

def plotAnimals(X, labels, names, theme = 'dark_background', annot = False):
	""" Plotter for Zoo-data. 
	:param X: Data Matrix with shape = (Ndim, Npts)
	:param labels: Labels indicating which group a data point belongs to.
	:param names: Names of the animal for the data point.
	:param theme: Theme for the plotter. Dark_background scatter points on a black background. 
	:param annot: Bolean, to either annotate points or not. 
	"""

	clr = { 	# colors for each group of animals
	'1': 'tan', 
	'2': 'mediumpurple', 
	'3': 'lime', 
	'4': 'blue', 
	'5': 'white', 
	'6': 'yellow', 
	'7': 'crimson'
	}

	plt.style.use(theme)
	D, N = X.shape

	for i in range(N):

		x = X[0][i]
		y = X[1][i]
		group = labels[i]

		plt.scatter(x, y, color = clr[str(group)])
		
		if annot:
			plt.annotate(names[i], (x, y))
	
	plt.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False)
	plt.show()

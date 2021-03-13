
"""experiment.py: Experiments to compare dimensionality reduction algorithms. """

__author__ = "Majd Jamal"

import numpy as np
import matplotlib.pyplot as plt
from models.isomap import Isomap
from models.mds import mds
from models.pca import PCA


X = np.load('data/swiss_roll.npy')
c = np.load('data/color_positions.npy')

def plotter3D(X, color):
	plt.style.use('ggplot')
	ax = plt.axes(projection='3d')
	ax.scatter3D(X[0], X[1], X[2], c = color, cmap="rainbow")
	ax.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False) 
	plt.show()

def plotter(X, color):
	plt.style.use('ggplot')
	plt.scatter(X[0], X[1], c=color, cmap='rainbow')
	plt.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False)
	plt.show()


#-=-=-=-
# PCA
#-=-=-=-


pca = PCA()
pca.fit(X, 2)
emb_pca = pca.transform(X) 


#-=-=-=-
# MDS
#-=-=-=-

emb_mds = mds(X, 2)


#-=-=-=-
# isomap
#-=-=-=-

isomap = Isomap(k_neigh = 10)
emb_iso = isomap.fit_transform(X)


#-=-=-=-
# Visualize
#-=-=-=-

plotter3D(X, c)	#original data
plotter(emb_pca, c)	#pca
plotter(emb_mds, c)	#mds
plotter(emb_iso, c) #isomap

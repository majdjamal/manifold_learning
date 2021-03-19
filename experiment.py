
"""experiment.py: Experiments to compare dimensionality reduction algorithms. """

__author__ = "Majd Jamal"

import numpy as np
import matplotlib.pyplot as plt
from models.isomap import Isomap
from models.mds import mds
from models.pca import PCA
from utils.plotter import swiss3D, swiss, plotAnimals
from data.zoo import names, y_animals, x_animals

X = np.load('data/swiss_roll.npy')
c = np.load('data/color_positions.npy')

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

swiss3D(X, c)
swiss(emb_pca, c)
swiss(emb_mds, c)
swiss(emb_iso, c)

#-=-=-=-
# Animals
#-=-=-=-

iso_animals = Isomap(k_neigh = 10)
emb_animals = iso_animals.fit_transform(x_animals)

plotAnimals(emb_animals, y_animals, names, theme = 'seaborn', annot = True)


"""mds.py: Performs dimensionality reduction on a data matrix with Multidimensional Scaling."""

__author__ = "Majd Jamal"

import numpy as np
import scipy as sp
from scipy.spatial import distance_matrix

def mds(X, dim):
	"""Classic Multidimensional Scaling with Similarity Matrix.
	:param X: Data points
	:param dim: Dimensions of the representation
	:return embedding: Data representation
	"""

	Ndim, Npts = X.shape

	D = distance_matrix(X.T, X.T, p=2)
	D = np.square(D)

	ones = np.ones((Npts,1))

	# Double centering trick
	fT = D @ ones @ ones.T / Npts
	sT = ones @ ones.T @ D / Npts
	tT = ones @ ones.T @ D @ ones @ ones.T / (Npts**2)

	S = -1 * (D - fT - sT + tT)/2

	# Embedding
	dimensions = np.arange(start=-1, stop = -dim - 1, step = -1)
	w, v = sp.linalg.eigh(S)
	lmd = np.sqrt(np.diag(w[dimensions]))
	v = v[:, dimensions]

	embedding = lmd @ v.T

	return embedding


"""pca.py: Performs dimensionality reduction on a data matrix with Principal Component Analysis."""

__author__ = "Majd Jamal"

import numpy as np

class PCA:
	"""
	Principal Component Analysis
	"""

	def __init__(self):
		self.W = None	#Weights

	def center(self, X):
		""" Centers a matrix
		:param X: Data matrix
		:return: A row centered data matrix.
		"""
		avgRow = np.mean(X, axis=0)
		return X - avgRow

	def getWeights(self):
		""" Extract weights
		:return: Weights that are used to transform data
		"""
		return self.W

	def fit(self, X, dim):
		""" Trains the model
		:param X: Patterns. Data points are represented by columns and attributres by rows.
		:param dim: Dimensions of the representation
		"""
		Ndim, Npts = X.shape

		if dim > Ndim:
			print("Your request is asking for larger dimensions than the original data. Adjust the dimension in your request.")
			return 

		centeredX = self.center(X)

		U, _, _ = np.linalg.svd(centeredX)

		cols = np.arange(start=0, stop = dim, step = 1)

		self.W = U[:, cols]

	def transform(self, X):
		""" Train the weights
		:param X: patterns
		:param dim: dimensions of the representation
		"""
		return self.W.T @ X

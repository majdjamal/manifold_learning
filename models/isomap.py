
"""isomap.py: Isomap, used for dimensionality reduction and to capture manifold. """

__author__ = "Majd Jamal"


import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.csgraph import shortest_path
from scipy.spatial import distance_matrix
from models.mds import mds


class Isomap:
	"""
	Isomap
	"""
	def __init__(self, k_neigh = 10):
		self.k_neigh = k_neigh	#Number of neighbors 

	def graph(self, D):
		""" Builds a graph representation in an array-format
		:param D: Matrix containing pair-wise distances 
		:return graph: A graph representation
		"""
		N, N = D.shape

		graph = {}

		#Extract closest neighbors to a given point
		for pnt in range(N):

			neighbors = D[pnt].argsort()[:self.k_neigh]
			graph[pnt] = neighbors[:self.k_neigh]

		#Make the graph directed
		for i in graph:
			for j in graph[i]:
				if np.any(graph[j] == i):
					continue
				else:
					graph[j] = np.append(graph[j], i)

		#Generate the graph matrix
		graph_matrix = np.full((N,N), np.inf)

		for i in range(N):
			graph_matrix[i][graph[i]] = D[i][graph[i]]

		return graph_matrix

	def fit_transform(self, X):
		""" Embedds a data matrix with Isomap. 
		:param X: Data Matrix with shape = (Ndim, Npts)
		:return emb: Embedding
		"""

		D = distance_matrix(X.T, X.T)	

		G = self.graph(D)

		Q = shortest_path(csgraph = G, method="FW")	# Compute shortest distance using Floyd-Warshall 

		#Modifying the shortest-path matrix.
		Q = Q ** 2
		Q *= - 0.5
		Q += - np.mean(Q, axis=0)

		emb = mds(Q, 2)	

		return emb

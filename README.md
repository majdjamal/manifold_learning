# Manifold Learning

## Overview
High-dimensional data can lie on low-dimensional manifolds. This experiment compares three different dimensionality reduction algorithms, focusing on how well they capture a manifold. The algorithms are PCA, MDS, and isomap.

## Requirements
This project requires packages: NumPy, SciPy, and Matplotlib

## Data
A swiss roll will be used in this experiment. The manifold is shown in figure 1, and stored in "swiss_roll.npy"

<img src="https://i.ibb.co/SnxyGT0/data.png" width="330" height="265">
(Figure 1. A swiss roll visualized in 3D. This data is used when comparing the dimensionality reduction algorithms.)

## PCA
Principal Component Analysis is a powerful dimensionality reduction algorithm. However, it does not capture manifolds. Figure 2 demonstrates the result when PCA is used with the swiss roll.

<img src="https://i.ibb.co/gPcdS79/pca.png" width="320" height="240">
(Figure 2. PCA used to embed the swiss roll. The manifold is not captured.)

## MDS
Multidimensional Scaling takes us one step closer to our goal. This model captures the pattern of a manifold, as seen in Figure 3. 

<img src="https://i.ibb.co/ygT7Pnr/mds.png" width="320" height="240">
(Figure 3. MDS used with swiss roll. It does not cature the manifold, but the pattern of it.)

## isomap
Isomap is the optimal solution to capture manifolds, because it considers neighborhood. Figure 3 demonstrate isomap used with the swiss roll. It captures the manifold.

<img src="https://i.ibb.co/bQ2mnRv/isomap.png" width="320" height="240">
(Figure 3. Isomap used with a swiss roll. It captures the manifold. )

## Testing

To test the model, install the required packages, navigate to the repository in your terminal and type:

```bash
python experiment.py
```

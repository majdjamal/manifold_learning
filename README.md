# Manifold Learning

## Overview
High-dimensional data can lie on low-dimensional manifolds. This project creates and compares three dimensionality reduction algorithms, namely PCA, MDS, and isomap. These algorithms are tested with two experiments. The first experiment demonstrates how each embedder captures the manifold from a swiss roll. The second experiment applies isomap to a real-life scenario using a dataset of animals.

## Swiss Roll
This project will use a swiss roll to investigate how each dimensionality reduction algorithm can capture manifolds. The swiss roll is shown in figure 1, and stored in "swiss_roll.npy."

<img src="https://i.ibb.co/SnxyGT0/data.png" width="330" height="265">
(Figure 1. A swiss roll visualized in 3D. This data is used when comparing the dimensionality reduction algorithms.)

### PCA
Principal Component Analysis is a powerful dimensionality reduction algorithm. However, it does not capture manifolds. Figure 2a demonstrates the result when PCA is used with the swiss roll.

### MDS
Multidimensional Scaling takes us one step closer to our goal. This model captures the pattern of a manifold, as seen in Figure 2b.

### isomap
Isomap is the optimal solution to capture manifolds because it considers neighborhood. Figure 2c demonstrates the result of using isomap with the swiss roll.

<img src="https://i.ibb.co/Ph0Sk8H/Ska-rmavbild-2021-03-19-kl-05-47-57.png" width="850" height="250">
(Figure 2. Swiss roll used with (A) PCA, (B) MDS, and (C) Isomap.)


## Animals

### Data
Data of animals are gathered from the UCI machine learning repository. [1](http://archive.ics.uci.edu/ml/datasets/Zoo) It consists of 101 instances and 17 attributes.

#### Preprocessing
The 14:th attributes indicate the number of legs. It stores a set of integers, [0, 2, 4, 5, 6, 8]. This is different from the other attributes which store booleans. Attribute 14 is converted from numerical to boolean values by storing True for 2 and 4, and False for the other values. The intuition is that most land animals have either 2 or 4 legs, and it would be convenient to split on these values.

### Result
Isomap is used with the Zoo-data, and the result is found in figure 3.

<img src="https://i.ibb.co/hf22KR9/Ska-rmavbild-2021-03-19-kl-05-35-28.png" width="650" height="400">
(Figure 3. Isomap is used with the Zoo-dataset. Images of animals are added to make the plot more interpretable.) 

### Discussion & Conclusion
Land animals such as Gorillas and Lions were placed to the right in the 2D-plane. Animals that live in or close to the water were placed in the center. For example, we see frogs at origo. Moving upwards, we start to see penguins and flamingos. Moving downwards, we start to see fishes such as Tuna and Dolphins. Furthermore, insects were placed to the right of the 2D-plane.  


Isomap is a powerful dimensionality reduction algorithm that is good at capturing manifolds, and the experiments confirm this.


## Requirements
This project requires packages: NumPy, SciPy, and Matplotlib.


## Testing

To test the model, install the required packages, navigate to the repository in your terminal, and type:

```bash
python experiment.py
```

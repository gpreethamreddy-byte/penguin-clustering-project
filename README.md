# Penguin Clustering Using K-Means

## Project Overview
This project uses the K-Means clustering algorithm to group penguins based on their physical measurements.

## Objective
To identify groups of penguins with similar measurements using unsupervised machine learning.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab

## Project Steps
1. Load the dataset.
2. Clean missing values.
3. Select numerical features.
4. Scale the features using StandardScaler.
5. Apply K-Means clustering.
6. Use the Elbow Method.
7. Compare Silhouette Scores.
8. Visualize the clusters.

## Model Evaluation
The final two-cluster model achieved a Silhouette Score of approximately 0.531.

## Results
The model created two clusters:
- Cluster 0: 221 penguins
- Cluster 1: 123 penguins

These groups represent similarities in measurements, not confirmed penguin species.

## Cluster Visualization

![Penguin Clustering Results](Screenshot%202026-10-10%20110215.png)

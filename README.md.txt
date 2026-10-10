# Penguin Clustering Using K-Means

## Project Overview
This project uses the K-Means clustering algorithm to group penguins based on their physical measurements.

## Objective
The objective is to identify groups of penguins with similar measurements using unsupervised machine learning.

## Dataset
The dataset contains penguin measurements, including:
- Culmen length
- Culmen depth
- Flipper length
- Body mass
- Sex

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
2. Explore the data.
3. Clean missing and suspicious values.
4. Visualize the measurements.
5. Select numerical features.
6. Scale the features using StandardScaler.
7. Apply K-Means clustering.
8. Use the Elbow Method.
9. Compare Silhouette Scores.
10. Visualize and save the final clusters.

## Model Evaluation
The Silhouette Score for the final two-cluster model was approximately 0.531.

## Results
The final model created two clusters:
- Cluster 0: 221 penguins
- Cluster 1: 123 penguins

These clusters represent groups based on measurement similarity. They are not confirmed penguin species.

## Files
- `penguin_clustering.ipynb`: Project code and analysis.
- `penguins.csv`: Original dataset.
- `penguin_clusters.csv`: Dataset with cluster assignments.

## Conclusion
This project demonstrates how K-Means clustering can be used to explore patterns in data without predefined labels.
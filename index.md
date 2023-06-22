---
layout: default
---



<h1 style="text-align: center;">Data Science Projects</h1>

---

<p>&nbsp;</p>

<div style="display: flex; justify-content: center;">
  <img src="images/Data-Science.gif?raw=true" 
  alt="Description of image"
  style="max-width: 80%; box-shadow: 0px 10px 16px rgba(0, 0, 0, 0.1); border-radius:7px;">
</div>


<p>&nbsp;</p>

This repository offers some insight data science portfolio, showcasing the multitude of ways Python can be utilized for various data-centric tasks.

<h2>Table of Content</h2>

<ul>
  <li><a href="#machine-learning">Machine Learning</a></li>
  <li><a href="#data-visualisation">Data Visualisation</a></li>
  <li><a href="#probability-and-statistics">Probability and Statistics</a></li>
  <li><a href="#data-cleaning">Data Cleaning</a></li>
  <li><a href="#getting-started">Getting Started</a></li>
</ul>

---

<h2 id="machine-learning">Machine Learning</h2>

[Link to project folder](https://github.com/David-vanderByl/Data-Science-Projects/tree/main/Machine%20Learning)

Machine learning is an intrinsic part of modern data science. The projects in this section demonstrate a strong foundation in machine learning concepts, coupled with the ability to implement, evaluate, and fine-tune models using the Scikit-learn library in Python. From building predictive models to understanding the importance of model validation, these projects cover an array of machine learning techniques.

- Supervised Machine Learning - Predicting Heart Disease
<p>&nbsp;</p>

<div style="display: flex; justify-content: center;">
  <img src="images/heart_disease.png?raw=true" 
  alt="Description of image"
  style="max-width: 80%; box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.05); border-radius:7px;">
</div>


<p>&nbsp;</p>

<h3> Machine learning Examples:</h3>

<h4>- Hyperparameter Tuning using Grid-Search:</h4>

```python
# Selecting the desired features from the DataFrame
X = df_features[onehot_features]
y = df_features["HeartDisease"]

# Splitting data into training and test sets with an 80:20 ratio
X_train_grid, X_test_grid, y_train_grid, y_test_grid = train_test_split(
    X, y, test_size=0.20, random_state=417)

# Normalizing features using MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_train_scaled_grid = scaler.transform(X_train_grid)
X_test_scaled_grid = scaler.transform(X_test_grid)

# Reduce the dimensionality of X_train_scaled (and test data too)
# using array indexing
X_train_reduced_grid = X_train_scaled_grid[:, feature_indices]
X_test_reduced_grid = X_test_scaled_grid[:, feature_indices]

# Define the parameters for the KNeighborsClassifier grid search
grid_params = {
    "n_neighbors": range(1, 100),
    "metric": ["minkowski", "manhattan"],
    "weights": ["uniform", "distance"],
    "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
    "leaf_size": [10, 20, 30],
    "p": [1, 2]
}

# Create an instance of the KNeighborsClassifier and GridSearchCV
knn_1 = KNeighborsClassifier()
knn_grid_1 = GridSearchCV(knn_1, grid_params, scoring='accuracy')

# Fit the grid search on the training data
knn_grid_1.fit(X_train_scaled_grid, y_train_grid)

# Retrieve the best model's accuracy score and parameters
best_score = knn_grid_1.best_score_
best_params = knn_grid_1.best_params_

# Print the results
print(f"Best model's accuracy: {best_score*100:.2f}")
print(f"Best model's parameters: {best_params}")
```


OUTPUT: 


```python
Best model's accuracy: 87.58
Best model's parameters: 
'algorithm': 'auto', 
'leaf_size': 10, 
'metric': 'minkowski', 
'n_neighbors': 65, 
'p': 1, 
'weights': 'distance'
```

<h2 id="data-visualisation">Data Visualisation</h2>


[Link to project folder](https://github.com/David-vanderByl/Data-Science-Projects/tree/main/Data%20Visualisation)

Visualisation is a powerful tool for communicating complex data stories. In this section, projects underscore the capacity to convert raw data into insightful visual narratives using Python libraries like Matplotlib, and Seaborn. Through a balanced mix of bar plots, scatter plots, histograms, and more, these projects demonstrate the value of visualisation in conveying patterns and correlations present in the data.

- Visualisation - Politics and Exchange Rates

<p>&nbsp;</p>


<div style="display: flex; justify-content: center;">
  <img src="images/data_vis_1.png?raw=true" 
  alt="Description of image"
  style="max-width: 80%; box-shadow: 0px 10px 16px rgba(0, 0, 0, 0.1); border-radius:7px;">
</div>

<p>&nbsp;</p>

<h2 id="probability-and-statistics">Probability and Statistics</h2>

[Link to project folder](https://github.com/David-vanderByl/Data-Science-Projects/tree/main/Probability%20and%20Statistics)

Probability and statistics serve as the bedrock of data science. The projects in this section apply these fundamental concepts to real-world problems, illustrating how mathematical theory can drive practical solutions. These projects explore statistical hypothesis testing, Bayesian probabilities, distribution analysis, and more, thereby presenting an integrated view of statistics and probability in action.

- Statistics 1 - Investigating Fandango Movie Ratings
- Probability - Mobile App for Lottery Addiction
- Conditional Probability - Building a Spam Filter with Naive Bayes
- Hypothesis Testing - Winning Jeopardy

<h2 id="data-cleaning">Data Cleaning</h2>

[Link to project folder](https://github.com/David-vanderByl/Data-Science-Projects/tree/main/Data%20Cleaning)

The data cleaning projects within this repository highlight the importance and necessity of data pre-processing in any data science workflow. Leveraging Python libraries such as Pandas and NumPy, these projects underscore the art of wrangling data into a suitable format for analysis. From handling missing values, formatting inconsistencies, to dealing with outliers, these projects cover a vast spectrum of data cleaning techniques.

- Clean and Analysing - NYC High School Data
- Clean and Analysing - Star Wars Survey



<h2 id="getting-started">Getting Started</h2>

To explore these projects:

1. To clone this repository open a terminal and run this command:
```bash
git clone https://github.com/David-vanderByl/Data-Science-Projects.git
``` 
2. Navigate into the repository: 
```bash
cd Data-Science-Projects
```
3. To launch Jupyter Notebook or jupyterlab run either: 
```bash
jupyter notebook
``` 
```bash
jupyterlab
``` 
4. Navigate to the project you'd like to view/run in the Jupyter Notebook dashboard that opens in your web browser.
If you do not have jupyter notebook or jupyterlab installed in terminal run either:

```bash
pip install notebook
```
```bash
pip install jupyterlab
```

---




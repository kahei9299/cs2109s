# Inital imports and setup

import os
import numpy as np

###################
# Helper function #
###################
def load_data(filepath):
    '''
    Load in the given csv filepath as a numpy array

    Parameters
    ----------
    filepath (string) : path to csv file

    Returns
    -------
        X, y (np.ndarray, np.ndarray) : (n, num_features), (n,) numpy matrices
    '''
    *X, y = np.genfromtxt(
        filepath,
        delimiter=',',
        skip_header=True,
        unpack=True,
    ) # default dtype: float
    X = np.array(X, dtype=float).T # cast features to int type
    return X, y

data_filepath = 'housing_data.csv'
X, y = load_data(data_filepath)

### Task 1.1: Mean Squared Error (MSE)

def mean_squared_error(y_true, y_pred):
    '''
    Calculate mean squared error between y_pred and y_true.

    Parameters
    ----------
    y_true (np.ndarray) : (n,) numpy matrix consists of true values
    y_pred (np.ndarray) : (n,) numpy matrix consists of predictions
    
    Returns
    -------
        The mean squared error value.
    '''
    
    """ YOUR CODE HERE """
    n = len(y_true)
    return np.sum((y_true - y_pred) ** 2) / (2 * n)
    """ YOUR CODE END HERE """

def test_task_1_1():
    y_true, y_pred = np.array([3, 5]), np.array([12, 15])
    
    assert np.isclose(mean_squared_error(y_true, y_pred), 45.25)

### Task 1.2: Mean Absolute Error (MAE)

def mean_absolute_error(y_true, y_pred):
    '''
    Calculate mean absolute error between y_pred and y_true.

    Parameters
    ----------
    y_true (np.ndarray) : (n, ) numpy matrix consists of true values
    y_pred (np.ndarray) : (n, ) numpy matrix consists of predictions
    
    Returns
    -------
        The mean absolute error value.
    '''
  
    """ YOUR CODE HERE """
    return np.mean(np.abs(y_true - y_pred))
    """ YOUR CODE END HERE """

def test_task_1_2():
    y_true, y_pred = np.array([3, 5]), np.array([12, 15])
    
    assert mean_absolute_error(y_true, y_pred) == 9.5

### Task 2.1: Adding a bias column

def add_bias_column(X):
    '''
    Create a bias column and combine it with X.

    Parameters
    ----------
    X : (n, d) numpy matrix representing a feature matrix
    
    Returns
    -------
        new_X (np.ndarray):
            the numpy matrix (n, d + 1) with the first column consisting of all 1s
    '''
  
    """ YOUR CODE HERE """
    ones = np.ones((X.shape[0], 1))
    return np.hstack((ones, X))
    """ YOUR CODE END HERE """

def test_task_2_1():
    without_bias = np.array([[1, 2], [3, 4]])
    expected = np.array([[1, 1, 2], [1, 3, 4]])
    
    assert np.array_equal(add_bias_column(without_bias), expected)

### Task 2.2: Find optimal bias and weights using normal equation

def get_bias_and_weight(X, y, include_bias = True):
    '''
    Calculate bias and weights that give the best fitting line.

    Parameters
    ----------
    X (np.ndarray) : (n, d) numpy matrix representing feature matrix
    y (np.ndarray) : (n, ) numpy matrix representing target values
    include_bias (boolean) : Specify whether the model should include a bias term
    
    Returns
    -------
        bias (float):
            If include_bias = True, return the bias constant. Else,
            return 0
        weights (np.ndarray):
            A (d,) numpy matrix representing the weight(s).
    '''
  
    """ YOUR CODE HERE """
    if include_bias:
        X_aug = add_bias_column(X)
        theta = np.linalg.inv(X_aug.T @ X_aug) @ X_aug.T @ y
        bias = theta[0]
        weights = theta[1:]
    else:
        theta = np.linalg.inv(X.T @ X) @ X.T @ y
        bias = 0
        weights = theta
    return bias, weights
    """ YOUR CODE END HERE """

def test_task_2_2():
    public_X, public_y = np.array([[1, 3], [2, 3], [3, 4]]), np.arange(4, 7)
    
    test_1 = (np.round(get_bias_and_weight(public_X, public_y)[0], 5) == 3)
    test_2 = np.array_equal(np.round(get_bias_and_weight(public_X, public_y)[1], 1), np.array([1.0, 0.0]))
    test_3 = np.array_equal(np.round(get_bias_and_weight(public_X, public_y, False)[1], 2), np.round(np.array([0.49, 1.20]), 2))
    assert get_bias_and_weight(public_X, public_y)[1].shape == (2,)
    assert get_bias_and_weight(public_X, public_y, False)[1].shape == (2,)
    assert test_1 and test_2 and test_3

### Task 2.3: Get the prediction line

def get_prediction_linear_regression(X, y, include_bias = True):
    '''
    Calculate the best fitting line.

    Parameters
    ----------
    X (np.ndarray) : (n, d) numpy matrix representing feature matrix
    y (np.ndarray) : (n,) numpy matrix representing target values
    include_bias (boolean) : Specify whether the model should include a bias term

    Returns
    -------
        y_pred (np.ndarray): (n,) numpy matrix representing prediction values.
    '''
  
    """ YOUR CODE HERE """
    bias, weights = get_bias_and_weight(X, y, include_bias)
    return X @ weights + bias
    """ YOUR CODE END HERE """

def test_task_2_3():
    test_X, test_y = np.array([[1, 3], [2, 3], [3, 4]]), np.arange(4, 7)
    assert get_prediction_linear_regression(test_X, test_y).shape == (3,)
    assert round(mean_squared_error(test_y, get_prediction_linear_regression(test_X, test_y)), 5) == 0

import matplotlib.pyplot as plt

area = X[:, 0].reshape((-1, 1))
predicted = get_prediction_linear_regression(area, y)
plt.scatter(area, y)
plt.plot(area, predicted, color = 'r')
plt.xlabel("Size in square meter")
plt.ylabel("Price in SGD")
plt.show()

### Task 2.4 : Create Polynomial Matrix

def create_polynomial_matrix(X, power = 2):
    '''
    Create a polynomial matrix.
    
    Parameters
    ----------
    X: (n, 1) numpy matrix

    Returns
    -------
        A (n, power) numpy matrix where the i-th column denotes
            X raised to the power of i.
    '''
    """ YOUR CODE HERE """
    return np.hstack([X ** i for i in range(1, power + 1)])
    """ YOUR CODE END HERE """

def test_task_2_4():
    vector = np.array([[1], [2], [3]])
    poly_matrix = np.array([[1, 1, 1], [2, 4, 8], [3, 9, 27]])
    assert create_polynomial_matrix(vector, 3).shape == (3, 3)
    assert np.array_equal(create_polynomial_matrix(vector, 3), poly_matrix)

### Task 2.5: Get the prediction line

def get_prediction_poly_regression(X, y, power = 2, include_bias = True):
    '''
    Calculate the best polynomial line.

    Parameters
    ----------
    X (np.ndarray) : (n, 1) numpy matrix representing feature matrix
    y (np.ndarray) : (n, ) numpy matrix representing target values
    power (int) : Specify the degree of the polynomial
    include_bias (boolean) : Specify whether the model should include a bias term

    Returns
    -------
        A (n, ) numpy matrix representing prediction values.
    '''
    """ YOUR CODE HERE """
    poly_X = create_polynomial_matrix(X, power)
    return get_prediction_linear_regression(poly_X, y, include_bias)
    """ YOUR CODE END HERE """

def test_task_2_5():
    test_X, test_y = np.arange(3).reshape((-1, 1)), np.arange(4, 7)
    pred_y = get_prediction_poly_regression(test_X, test_y, 2)
    assert pred_y.shape == (3,)
    assert np.round(mean_squared_error(test_y, pred_y), 5) == 0

import matplotlib.pyplot as plt

schools = X[:, 2].reshape((-1, 1))
predicted = get_prediction_poly_regression(schools, y, 3)
plt.scatter(schools, y)
plt.scatter(schools, predicted, color = 'r', s = 100)
plt.xlabel("Number of schools within 1km")
plt.ylabel("Price in SGD")
plt.show()

### Task 2.6: Gradient Descent on multiple features

def gradient_descent_multi_variable(X, y, lr = 1e-5, number_of_epochs = 250):
    '''
    Bias and weight that gives the best fitting line.

    Parameters
    ----------
    X (np.ndarray) : (n, d) numpy matrix representing feature matrix
    y (np.ndarray) : (n,) numpy matrix representing target values
    lr (float) : Learning rate
    number_of_epochs (int) : Number of gradient descent epochs
    
    Returns
    -------
        bias (float):
            The bias constant
        weights (np.ndarray):
            A (d, ) numpy matrix that specifies the weights.
        loss (list):
            A list where the i-th element denotes the MSE score at i-th epoch.
    '''
    # Do not change
    bias = 0
    weights = np.full((X.shape[1], ), 0).astype(float)
    loss = []

    n = X.shape[0]
    pred = X @ weights + bias
    for _ in range(number_of_epochs):
        """ YOUR CODE HERE """
        loss.append(mean_squared_error(y, pred))
        error = pred - y
        weights -= lr * (1 / n) * (X.T @ error)
        bias -= lr * (1 / n) * np.sum(error)
        pred = X @ weights + bias
        """ YOUR CODE END HERE """

    return bias, weights, loss

def test_task_2_6():
    _, _weights, loss = gradient_descent_multi_variable(X, y, lr = 1e-5, number_of_epochs = 250)
    loss_initial = loss[0]
    loss_final = loss[-1]
    assert _weights.shape == (X.shape[1], )
    assert loss_initial > loss_final
    
    public_X = np.array([[0], [40], [60], [100]])
    public_y = np.array([0, 40, 60, 100])
    public_bias, public_weights, _ = gradient_descent_multi_variable(public_X, public_y)
    assert np.allclose(public_bias, 0.0131, rtol=1e-2)
    assert np.allclose(public_weights, np.array([0.99976]), rtol=1e-2)

### Task 2.7 Feature Scaling

def feature_scaling(X):
    '''
    Standardize each feature column.

    Parameters
    ----------
    X (np.ndarray) : (n, d) numpy matrix representing feature matrix

    Returns
    -------
        A (n, d) numpy matrix where each column has been standardized.
    '''
    """ YOUR CODE HERE """
    return (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    """ YOUR CODE END HERE """

def test_task_2_7():
    public_X = np.array([[1, 133], [4, 700], [5, 133], [8, 700]])
    expected = np.array([[-1.4, -1], [-0.2, 1], [0.2, -1], [1.4, 1]])
    
    assert np.array_equal(feature_scaling(public_X), expected)

### Task 2.8: Finding the number of epochs for gradient descent to converge

def find_number_of_epochs(X, y, lr, delta_loss):
    '''
    Do gradient descent until convergence and return number of epochs
    required.

    Parameters
    ----------
    X (np.ndarray) : (n, d) numpy matrix representing feature matrix
    y (np.ndarray) : (n, ) numpy matrix representing target values
    lr (float) : Learning rate
    delta_loss (float) : Termination criterion
    
    Returns
    -------
        bias (float):
            The bias constant
        weights (np.ndarray):
            A (d, ) numpy matrix that specifies the weights.
        num_of_epochs (int):
            Number of epochs to reach convergence.
        current_loss (float):
            The loss value obtained after convergence.
    '''
    # Do not change
    bias = 0
    weights = np.full((X.shape[1], ), 0).astype(float)
    num_of_epochs = 0
    previous_loss = 1e14
    current_loss = -1e14

    n = X.shape[0]
    pred = X @ weights + bias
    current_loss = mean_squared_error(y, pred)
    while abs(previous_loss - current_loss) >= delta_loss:
        """ YOUR CODE HERE """
        previous_loss = current_loss
        error = pred - y
        weights -= lr * (1 / n) * (X.T @ error)
        bias -= lr * (1 / n) * np.sum(error)
        pred = X @ weights + bias
        current_loss = mean_squared_error(y, pred)
        num_of_epochs += 1
        """ YOUR CODE END HERE """

    return bias, weights, num_of_epochs, current_loss

def test_task_2_8():
    poly_X = create_polynomial_matrix(X[:, 2].reshape((-1, 1)), 3)
    _, _weights, num_of_epochs, current_loss = find_number_of_epochs(poly_X, y, 1e-5, 1e7)
    assert _weights.shape == (3,)
    assert num_of_epochs > 0
    assert np.isclose(current_loss, 72890526768.94409, rtol=0.0, atol=1e-4)

### Task 2.9: Which algorithm should we use for Linear Regression?

### Task 2.10: Analyze the effects of feature scaling on Gradient Descent

# Initial imports and setup

import numpy as np
import os
import pandas as pd

# Read credit card data into a Pandas dataframe for large tests

dirname = os.getcwd()
credit_card_data_filepath = os.path.join(dirname, 'credit_card.csv')

credit_df = pd.read_csv(credit_card_data_filepath)
X_task5 = credit_df.values[:, :-1]
y_task5 = credit_df.values[:, -1:]

print(credit_df.head())

# Inspect the number of fraudulent and non-fraudulent transactions.
print(credit_df['Class'].value_counts())

# Select the 'Class' column in the credit dataframe
print(credit_df['Class'])

# Obtain the first 2 rows
print(credit_df[0:2])

print(credit_df['Class'] == 0)

# Obtain the credit dataframe where the 'Class' field is 0
print(credit_df[credit_df['Class'] == 0])

pd.concat([credit_df[:2], credit_df[-2:]], axis=0)

### Task 3.1: Problem with imbalanced data

### Task 3.2: Cost function

def cost_function(X: np.ndarray, y: np.ndarray, weight_vector: np.ndarray):
    '''
    Binary cross entropy error for logistic regression

    Parameters
    ----------
    X: np.ndarray
        (n, d) training dataset (features).
    y: np.ndarray
        (n,) training dataset (corresponding targets).
    weight_vector: np.ndarray
        (d,) weight parameters.

    Returns
    -------
    BCE cost
    '''
    
    # Machine epsilon for numpy `float64` type
    eps = np.finfo(np.float64).eps

    """ YOUR CODE HERE """
    n = X.shape[0]
    h = 1 / (1 + np.exp(-X @ weight_vector))
    h = np.clip(h, eps, 1 - eps)
    return -(1 / n) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    """ YOUR CODE END HERE """

def test_task_3_2():
    data1 = [[111.1, 10, 0], [111.2, 20, 0], [111.3, 10, 0], [111.4, 10, 0], [111.5, 10, 0], [111.6, 10, 1], [111.4, 10, 0], [111.5, 10, 1], [111.6, 10, 1]]
    df1 = pd.DataFrame(data1, columns = ['V1', 'V2', 'Class'])
    X1 = df1.iloc[:, :-1].to_numpy()
    y1 = df1.iloc[:, -1].to_numpy()
    w1 = np.transpose([0.002, 0.1220])
    
    assert np.round(cost_function(X1, y1, w1), 5) == np.round(1.29333, 5)

### Task 3.3: Weight update for batch gradient descent

def weight_update(X: np.ndarray, y: np.ndarray, gamma: np.float64, weight_vector: np.ndarray) -> np.ndarray:
    '''
    Do the weight update for one step in gradient descent

    Parameters
    ----------
    X: np.ndarray
        (n, d) training dataset (features).
    y: np.ndarray
        (n,) training dataset (corresponding targets).
    gamma: np.float64
        logistic regression learning rate.
    weight_vector: np.ndarray
        (d,) weight parameters.

    Returns
    -------
    New (d,) weight vector after one round of update.
    '''

    """ YOUR CODE HERE """
    n = X.shape[0]
    h = 1 / (1 + np.exp(-X @ weight_vector))
    gradient = (1 / n) * (X.T @ (h - y))
    return weight_vector - gamma * gradient
    """ YOUR CODE END HERE """

def test_task_3_3():
    data1 = [[111.1, 10, 0], [111.2, 20, 0], [111.3, 10, 0], [111.4, 10, 0], [111.5, 10, 0], [111.6, 10, 1],[111.4, 10, 0], [111.5, 10, 1], [111.6, 10, 1]]
    df1 = pd.DataFrame(data1, columns = ['V1', 'V2', 'Class'])
    X1 = df1.iloc[:, :-1].to_numpy()
    y1 = df1.iloc[:, -1].to_numpy()
    w1 = np.transpose([2.2000, 12.20000])
    a1 = 1e-5
    nw1 = np.array([2.199,12.2])
    
    assert np.array_equal(np.round(weight_update(X1, y1, a1, w1), 3), nw1)

### Task 3.4: Logistic regression classification

def logistic_regression_classification(X: np.ndarray, weight_vector: np.ndarray, prob_threshold: np.float64=0.5):
    '''
    Do classification task using logistic regression.

    Parameters
    ----------
    X: np.ndarray
        (n, d) training dataset (features).
    weight_vector: np.ndarray
        (d,) weight parameters.
    prob_threshold: np.float64
        the threshold for a prediction to be considered fraudulent.

    Returns
    -------
    Classification result as an (n,) np.ndarray
    '''

    """ YOUR CODE HERE """
    h = 1 / (1 + np.exp(-X @ weight_vector))
    return (h >= prob_threshold).astype(int)
    """ YOUR CODE END HERE """

def test_task_3_4():
    data1 = [[111.1, 10, 0], [111.2, 20, 0], [111.3, 10, 0], [111.4, 10, 0], [111.5, 10, 0], [211.6, 80, 1],[111.4, 10, 0], [111.5, 80, 1], [211.6, 80, 1]]
    df1 = pd.DataFrame(data1, columns = ['V1', 'V2', 'Class'])
    X1 = df1.iloc[:, :-1].to_numpy()
    y1 = df1.iloc[:, -1].to_numpy()
    w1 = np.transpose([-0.000002, 0.000003])
    expected1 = np.transpose([0, 0, 0, 0, 0, 0, 0, 1, 0])
    result1 = logistic_regression_classification(X1, w1)
    
    assert result1.shape == expected1.shape and (result1 == expected1).all()

### Task 3.5: Logistic regression using stochastic gradient descent

def logistic_regression_stochastic_gradient_descent(X_train: np.ndarray, y_train: np.ndarray, max_num_iterations: int=250, threshold: np.float64=0.05, gamma: np.float64=1e-5, seed: int=43) -> np.ndarray:
    '''
    Initialize the weights to zeros and run stochastic-gradient iterations until a terminating condition is met.
    Get the resulting weight vector.

    Parameters
    ----------
    X_train: np.ndarray
        (n, d) training dataset (features).
    y_train: np.ndarray
        (n,) training dataset (corresponding targets).
    max_num_iterations: int
        Maximum number of stochastic-gradient iterations.
        The function should perform at most max_num_iterations iterations.
    threshold: np.float64
        Terminate when the full-dataset cost is <= threshold, or when the maximum number of iterations is reached.
    gamma: np.float64
        logistic regression learning rate.
    seed: int
        seed for random number generation.

    Returns
    -------
    The final (d,) weight parameters
    '''

    """ YOUR CODE HERE """
    np.random.seed(seed)
    weights = np.zeros(X_train.shape[1])
    n = X_train.shape[0]

    for _ in range(max_num_iterations):
        if cost_function(X_train, y_train, weights) <= threshold:
            break
        i = np.random.randint(0, n)
        weights = weight_update(X_train[i:i+1], y_train[i:i+1], gamma, weights)

    return weights
    """ YOUR CODE END HERE """

def test_task_3_5():
    data1 = [[111.1, 10, 0], [111.2, 20, 0], [111.3, 10, 0], [111.4, 10, 0], [111.5, 10, 0], [211.6, 80, 1],[111.4, 10, 0], [111.5, 80, 1], [211.6, 80, 1]]
    df1 = pd.DataFrame(data1, columns = ['V1', 'V2', 'Class'])
    X1 = df1.iloc[:, :-1].to_numpy()
    y1 = df1.iloc[:, -1].to_numpy()
    expected1 = cost_function(X1, y1, np.transpose(np.zeros(X1.shape[1])))
    
    assert np.allclose(logistic_regression_stochastic_gradient_descent(X1, y1, max_num_iterations=0), [0, 0])
    assert logistic_regression_stochastic_gradient_descent(X1, y1, seed=2109)[0] != logistic_regression_stochastic_gradient_descent(X1, y1, seed=69)[0]
    assert np.allclose(logistic_regression_stochastic_gradient_descent(X1, y1, max_num_iterations=1), [-5.575e-04, -5.000e-05])
    
    default_weights = logistic_regression_stochastic_gradient_descent(X1, y1)
    assert default_weights.shape == (2,) and np.allclose(default_weights, [-0.0031107978886271, 0.0231664124558984]) and cost_function(X1, y1, default_weights) < expected1
    assert np.allclose(logistic_regression_stochastic_gradient_descent(X1, y1, max_num_iterations=20000), [-0.0441142166936007, 0.1481291955136605])

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler

df_neg = credit_df[credit_df["Class"] == 0]
df_pos = credit_df[credit_df["Class"] == 1]
df_neg = resample(df_neg, replace=True, n_samples=500, random_state=42)
df_pos = resample(df_pos, replace=True, n_samples=500, random_state=42)

df_balanced = pd.concat([df_neg, df_pos])
df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

X = df_balanced.drop(columns=["Class"]).to_numpy()
y = df_balanced["Class"].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train = add_bias_column(X_train)
X_test = add_bias_column(X_test)

weights = logistic_regression_stochastic_gradient_descent(X_train, y_train)

y_pred_train = logistic_regression_classification(X_train, weights)
y_pred_test = logistic_regression_classification(X_test, weights)

train_acc = accuracy_score(y_train, y_pred_train)
test_acc = accuracy_score(y_test, y_pred_test)

print(f"Training Accuracy: {train_acc:.5f}")
print(f"Test Accuracy: {test_acc:.5f}")


### Task 3.6: Stochastic gradient descent vs batch gradient descent


if __name__ == '__main__':
    test_task_1_1()
    test_task_1_2()
    test_task_2_1()
    test_task_2_2()
    test_task_2_3()
    test_task_2_4()
    test_task_2_5()
    test_task_2_6()
    test_task_2_7()
    test_task_2_8()
    test_task_3_2()
    test_task_3_3()
    test_task_3_4()
    test_task_3_5()
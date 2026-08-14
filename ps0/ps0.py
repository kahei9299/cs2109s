x = 2109        # Declares and assigns a value to the variable x
print(x + 1)   # Addition ; prints 2110
print(x - 1)   # Subtraction ; prints 2108
print(x * 2)   # Multiplication ; prints 4218
print(x / 2)   # Floating point division ; prints 1054.5
print(x // 2)  # Integer division ; prints 1054
print(x % 2)   # Modulo division ; prints 1

a = True        # Assigns true to variable a
b = False       # Assigns false to variable b
print(a and b) # Logical and; prints False
print(a or b)  # Logical or; prints True
print(not a)   # Logical negation ; prints False

s1 = 'hello'
s2 = "world"
print(s1)
print(s2)

arr = [1, 2, 3]     # Creates a list
print(arr[2])       # Accesses the element at index 2 (0- indexed); prints 3
print(arr[-1])      # Accesses the element at the last index ; prints 3
arr[1] = 'foo'     # Re - assigns the value at index 1 to 'foo'
arr.append(4)       # Adds a new element 4 to the end of the list
x = arr.pop()      # Removes and returns the last element
y = arr.pop(1)     # Removes and returns the element at index 1
print(x, y)         # Prints '4 foo'
arr = [ None ] * 3  # Creates the list [None, None, None]
print(arr)

arr = [1, 2, 3, 4, 5] # Creates a list
print(arr[1:3])       # Prints [2, 3]
print(arr[2:])        # Prints [3, 4, 5]
print(arr[:3])        # Prints [1, 2, 3]
arr[2:] = [5]        
print(arr)            # Prints [1, 2, 5]

t = (1 , 'cool')                  # Declares a tuple containing two elements
print (t[0], t[1], sep=" ... ") # Prints "1 ... cool "

i = 0
while (i < 5):
    print(i, end="")
    i += 1

for i in range(5):
    print(i, end="")

for i in range (2, 5):
    print(i, end="")

for i in range(3, 10, 2):
    print(i, end="")

def foo(x):
    for i in range(4):
        if i == 0:
            print('Zero here!')
        elif i == 1:
            print('One here!')
        else:
            print(i)
            print(x)
foo('hello')

def foo(x):
    for i in range(4):
        if i == 0:
            print('Zero here!')
        elif i == 1:
            print('One here!')
        else:
            print(i)
        print(x) # Additional level of indentation
foo('hello')

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True
print(a is b) # False

c = a         # Now , c points to the same object as a
print(a == c) # True
print(a is c) # True

c[0] = 'hello'
print(a) # Prints ['hello', 2, 3]

a = [1, 2, 3]
c = a.copy()
c[0] = 'hello'
print(a) # Prints [1, 2, 3]
print(c) # Prints ['hello', 2, 3]

import copy

print('Shallow copy')
a = [[1, 2], [3, 4]]
b = a.copy() # Performs a shallow copy of variable a
b[0][0] = 5  # Modifies both a and b
print(a)     # Prints [[5, 2], [3, 4]]
print(b)     # Prints [[5, 2], [3, 4]]

print('Deep copy')
x = [[1, 2], [3, 4]]
y = copy.deepcopy(x) # Performs a deep copy of variable x
y[0][0] = 5          # Modifies y only
print(x)             # Prints [[1, 2], [3, 4]]
print(y)             # Prints [[5, 2], [3, 4]]

a = 1
b = 2
a, b = b, a
print(a) # Prints 2
print(b) # Prints 1

def increment_by_one(x):
    return x + 1
print(increment_by_one(2108))   # Prints 2109
print((lambda x : x + 1)(2108)) # Prints 2109

# Initialize an empty dictionary
a = {}
# or
a = dict()

print(a) # Prints {}

# We can also initialize a dictionary with some items
a = {'foo': 'bar', 'one': 1}

print(a) # Prints a as initialized

print(a['foo']) # Prints "bar"

a['two'] = 2         # Adds a new key "two" with value 2
a['foo'] = 'cs2109s' # Updates the value of key "foo" with "cs2109s"
del a['one']         # Deletes the key "one"

print(a) # Prints the updated a

print('two' in a)   # True
print('three' in a) # False

b = {1: 'one', 2: 'two'} # Creates a new dictionary

c = {**a, **b} # Merges dictionaries a and b
print(c)

try:
    a = {}
    a['test'] = 1      # String: OK
    print(a)
    
    a[0] = 1           # Number: OK
    print(a)
    
    a[('test', 0)] = 1 # Tuple of string and number: OK
    print(a)
    
    a[['test', 0]] = 1 # List: FAIL
    print(a)
except Exception as e:
    print(e)

# Initialize an empty set
a = set()

print(a) # Prints set()

# Initialize a set with some elements
a = set([0, 1, 2])

print(a)    # Prints {0, 1, 2}

a.add(3)    # Adds 3

print(a)    # Prints {0, 1, 2, 3}

a.remove(0) # Remove 0

print(a)    # Prints {1, 2, 3}

print(1 in a) # True
print(4 in a) # False

a2 = set([3, 4, 5])

print(a2)

print(a.intersection(a2))          # Intersection of two sets
print(a & a2)                      # Intersection of two sets
print(a.union(a2))                 # Union of two sets
print(a | a2)                      # Union of two sets
print(a.symmetric_difference(a2))  # Symmetric difference of two sets
print(a ^ a2)                      # Symmetric difference of two sets
print(a - a2)                      # Difference of two sets
print(a2 - a)                      # Difference of two sets

print(a == set([3, 2, 1]))    # True
print(a == set([3, 2, 1, 0])) # False

print('Method 1')
X = [None] * 2
X[0] = [5, 7, 9]
X[1] = [1, 4, 3]
print(X)

print('Method 2')
X = [[5, 7, 9],
     [1, 4, 3]]
print(X)

### Task 1.1 Scalar Multiplication

def mult_scalar(A, c):
    """
    Returns a new matrix created by multiplying elements of matrix A by a scalar c.
    Note
    ----
    Do not use numpy for this question.
    """
    """ YOUR CODE HERE """
    res = []
    for i, row in enumerate(A):
        curr = []
        for j, value in enumerate(row):
            value *= c
            curr.append(value)
        res.append(curr)

    return res

    """ YOUR CODE END HERE """

def test_task_1_1():
    A = [[5, 7, 9], [1, 4, 3]]
    A_copy = copy.deepcopy(A)
    
    actual = mult_scalar(A_copy, 2)
    expected = [[10, 14, 18], [2, 8, 6]]
    assert(A == A_copy) # check for aliasing
    assert(actual == expected)
    
    
    A2 = [[6, 5, 5], [8, 6, 0], [1, 5, 8]]
    A2_copy = copy.deepcopy(A2)
    
    actual2 = mult_scalar(A2_copy, 5)
    expected2 = [[30, 25, 25], [40, 30, 0], [5, 25, 40]]
    assert(A2 == A2_copy) # check for aliasing
    assert(actual2 == expected2)

### Task 1.2 Matrix Addition

def add_matrices(A, B):
    """
    Returns a new matrix that is the result of adding matrix B to matrix A.
    Note
    ----
    Do not use numpy for this question.
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception('A and B cannot be added as they have incompatible dimensions!') 
    """ YOUR CODE HERE """
    res = []
    for rowa, rowb in zip(A, B):
        row = []
        for a,b in zip(rowa, rowb):
            val = a + b
            row.append(val)
        res.append(row)

    return res
    """ YOUR CODE END HERE """

def test_task_1_2():
    A = [[5, 7, 9], [1, 4, 3]]
    B = [[2, 3, 4], [5, 6, 7]]
    A_copy = copy.deepcopy(A)
    B_copy = copy.deepcopy(B)
    
    actual = add_matrices(A_copy, B_copy)
    expected = [[7, 10, 13], [6, 10, 10]]
    assert(A == A_copy) # check for aliasing
    assert(B == B_copy) # check for aliasing
    assert(actual == expected)

### Task 1.3 Transpose a Matrix

def transpose_matrix(A):
    """
    Returns a new matrix that is the transpose of matrix A.
    Note
    ----
    Do not use numpy for this question.
    """
    """ YOUR CODE HERE """
    cols = len(A)
    rows = len(A[0])
    res = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[j][i])
        res.append(row)

    return res


    """ YOUR CODE END HERE """

def test_task_1_3():
    A = [[5, 7, 9], [1, 4, 3]]
    A_copy = copy.deepcopy(A)
    
    actual = transpose_matrix(A_copy)
    expected = [[5, 1], [7, 4], [9, 3]]
    assert(A == A_copy)
    assert(actual == expected)

### Task 1.4 Multiply Two Matrices

def mult_matrices(A, B):
    """
    Multiplies matrix A by matrix B, giving AB.
    Note
    ----
    Do not use numpy for this question.
    """
    if len(A[0]) != len(B):
        raise Exception('Incompatible dimensions for matrix multiplication of A and B')
    """ YOUR CODE HERE """
    res = []
    rows = len(A)
    cols = len(B[0])

    for i in range(rows):
        row = []
        for j in range(cols):
            curr = 0
            for k in range(len(A[0])):
                val = A[i][k] * B[k][j]
                curr = curr + val 
            row.append(curr)
        res.append(row)
    return res
    """ YOUR CODE END HERE """

def test_task_1_4():
    A = [[5, 7, 9], [1, 4, 3]]
    B = [[2, 5], [3, 6], [4, 7]]
    A_copy = copy.deepcopy(A)
    B_copy = copy.deepcopy(B)
    
    actual = mult_matrices(A, B)
    expected = [[67, 130], [26, 50]]
    assert(A == A_copy and B == B_copy)
    assert(actual == expected)
    
    A2 = [[-13, -10], [-24, 14]]
    B2 = [[1, 0], [0, 1]]
    A2_copy = copy.deepcopy(A2)
    B2_copy = copy.deepcopy(B2)
    
    actual2 = mult_matrices(A2, B2)
    expected2 = [[-13, -10], [-24, 14]]
    assert(A2 == A2_copy and B2 == B2_copy)
    assert(actual2 == expected2)

import random
import time

import numpy as np
import matplotlib.pyplot as plt

random.seed(2109)
matrix_sizes = [5, 10, 20, 50, 100, 200]
runtimes_list = [0 for i in range(len(matrix_sizes))]
runtimes_numpy = [0 for i in range(len(matrix_sizes))]

for i, matrix_size in enumerate(matrix_sizes):
    for j in range(10):
        A = [[random.random() for j in range(matrix_size)] for i in range(matrix_size)]
        B = [[random.random() for j in range(matrix_size)] for i in range(matrix_size)]

        start = time.time()
        _ = mult_matrices(A, B)
        end = time.time()
        runtimes_list[i] += end - start

        start = time.time()
        _ = np.matmul(A, B)
        end = time.time()
        runtimes_numpy[i] += end - start

    runtimes_list[i] /= 10
    runtimes_numpy[i] /= 10

fig, ax = plt.subplots()
ax.plot(matrix_sizes, runtimes_list, color='red', label='Python mult_matrices')
ax.plot(matrix_sizes, runtimes_numpy, color='blue', label='NumPy matmul')
ax.legend()
ax.set_xlabel('Size of Sq Matrix (cols/rows)')
ax.set_ylabel('Avg Runtime (s)')

# OPTIONAL: Compare runtimes on log scale to see from a different perspective.
# ax.set_yscale('log')

plt.show()

import numpy
a = numpy.arange(5) # Returns a NumPy array [0, 1, 2, 3, 4]

import numpy as np
a = np.arange(5) # Note that here we use `np` instead of `numpy`

import numpy as np

a = np.array([1, 2, 3]) # Create 1D array vector
print(a.shape)          # Prints(3, )
print(a[0], a[1], a[2]) # Prints 1, 2, 3
a[0] = 9                # Change the zeroth element to 9
print(a)                # Prints[9 2 3]

b = np.array([[1, 2, 3], [4, 5, 6]])  # Creates 2D array (matrix)
print(b.shape)                        # Prints(2, 3)
print(b[0, 0], b[1, 1], b[0, 2])      # Prints 1, 5, 3


a = np.zeros((3, 3))        # Create 3x3 matrix with all zeros
b = np.ones(2)              # Create vector of size 2 with all ones
c = np.ones((3, 3))         # Create 3x3 matrix with all ones
d = np.full((2, 3), False)  # Create a constant array
e = np.arange(5)            # Creates a 1D array with values [0, 5)

print('Object a')
print(a)
print('Object b')
print(b)
print('Object c')
print(c)
print('Object d')
print(d)
print('Object e')
print(e)

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[0, 0])                       # Prints 1
print(a[1, 2])                       # Prints 6

import numpy as np

a = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
print(a[0, 1:3])                            # Prints [2, 3]
print(a[:, 1:3])                            # Prints [[2 3]
                                            #         [5 6]]

b = a                                       # Aliasing
b[0, 0] = 5
print(a[0, 0])                              # Prints "5"

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(x + y)                   # Prints [[ 6  8]
                               #         [10 12]]

print(x * y)                   # Prints [[ 5 12]
                               #         [21 32]]

import numpy as np

print(np.sum([]))                       # 0.0
print(np.sum([0.5, 1.5]))               # 2.0
print(np.sum([[0, 1], [0, 5]]))         # 6
print(np.sum([[0, 1], [0, 5]], axis=0)) # array([0, 6])
print(np.sum([[0, 1], [0, 5]], axis=1)) # array([1, 5])

a = np.array([[1, 2], [3, 4]])
print(np.mean(a))         # 2.5
print(np.mean(a, axis=0)) # array([2., 3.])
print(np.mean(a, axis=1)) # array([1.5, 3.5])

a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
print(np.floor(a)) # array([-2., -2., -1.,  0.,  1.,  1.,  2.])
print(np.ceil(a))  # array([-1., -1., -0.,  1.,  2.,  2.,  2.])

a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.max(a, axis=0)) # array([4, 5, 6]); maximum of each column
print(np.max(a, axis=1)) # array([3, 6]); maximum of each row

cumulative = np.array([2, 5, 5, 9])
print(np.diff(cumulative))            # array([3, 0, 4])
print(np.diff(cumulative, prepend=0)) # array([2, 3, 0, 4])

values = np.array([[1, 3, 5], [2, 4, 6]])
row_limits = np.array([2, 5])
print(values > row_limits[:, None]) # array([[False, True,  True],
                                    #        [False, False, True]])

cases_cumulative = np.array([[0, 1, 2, 3], [0, 20, 21, 35]])

healthcare_spending = np.array([[0, 100, 0, 200], [0, 0, 0, 1000]])

mask_prices = np.array([4, 5, 20, 18])

stringency_values = np.array([[[0, 0, 0, 0], [1, 0, 0, 0]],\
    [[0, 0, 0, 0], [0, 1, 2, 0]]])

from prepare_data import * # loads the `get_...` helper funtions

df = get_data()
cases_cumulative = get_n_cases_cumulative(df)
deaths_cumulative = get_n_deaths_cumulative(df)
healthcare_spending = get_healthcare_spending(df)
mask_prices = get_mask_prices(healthcare_spending.shape[1])
stringency_values = get_stringency_values(df)
cases_top_cumulative = get_n_cases_top_cumulative(df)

## Task 2.1: Computing Death Rates

print(np.nan_to_num(np.inf)) #1.7976931348623157e+308
print(np.nan_to_num(-np.inf)) #-1.7976931348623157e+308
print(np.nan_to_num(np.nan)) #0.0
x = np.array([np.inf, -np.inf, np.nan, -128, 128])
np.nan_to_num(x)
np.nan_to_num(x, nan=-9999, posinf=33333333, neginf=33333333)  # Specify nan to be -9999, and both posinf and neginf to be 33333333
np.nan_to_num(y, nan=111111, posinf=222222) # Specify nan to be 111111, and both posinf and neginf to be 222222

def compute_death_rate_first_n_days(n, cases_cumulative, deaths_cumulative):
    '''
    Computes the average number of deaths recorded for every confirmed case
    that is recorded from the first day to the nth day (inclusive).
    Parameters
    ----------
    n: int
        How many days of data to return in the final array.
    cases_cumulative: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the cumulative number of
        confirmed cases in that country, i.e. the ith row of `cases_cumulative`
        contains the data of the ith country, and the (i, j) entry of
        `cases_cumulative` is the cumulative number of confirmed cases on the
        (j + 1)th day in the ith country.
    deaths_cumulative: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the cumulative number of
        confirmed deaths (as a result of COVID-19) in that country, i.e. the ith
        row of `n_deaths_cumulative` contains the data of the ith country, and
        the (i, j) entry of `n_deaths_cumulative` is the cumulative number of
        confirmed deaths on the (j + 1)th day in the ith country.
    
    Returns
    -------
    Average number of deaths recorded for every confirmed case from the first day
    to the nth day (inclusive) for each country as a 1D `ndarray` such that the
    entry in the ith row corresponds to the death rate in the ith country as
    represented in `cases_cumulative` and `deaths_cumulative`.
    Note
    ----
    `cases_cumulative` and `deaths_cumulative` are such that the ith row in the 
    former and that in the latter contain data of the same country. In addition,
    if there are no confirmed cases for a particular country, the expected death
    rate for that country should be zero. (Hint: to deal with NaN look at
    `np.nan_to_num`)
    Your implementation should not involve any iteration, including `map` and `filter`, 
    recursion, or any iterative approaches like for-loops.
    '''
    """ YOUR CODE HERE """
    c = cases_cumulative[:,n - 1]
    d = deaths_cumulative[:,n - 1]
    return np.nan_to_num(d/c)
    """ YOUR CODE END HERE """

def test_task_2_1():
    n_cases_cumulative = cases_cumulative[:3, :] #Using data from CSV. Make sure to run relevant cell above
    n_deaths_cumulative = deaths_cumulative[:3, :]
    expected = np.array([0.0337837838, 0.0562347188, 0.1410564226])
    np.testing.assert_allclose(compute_death_rate_first_n_days(100, n_cases_cumulative, n_deaths_cumulative), expected)
    
    sample_cumulative = np.array([[1,2,3,4,8,8,10,10,10,10], [1,2,3,4,8,8,10,10,10,10]])
    sample_death = np.array([[0,0,0,1,2,2,2,2,5,5], [0,0,0,1,2,2,2,2,5,5]])
    
    expected2 = np.array([0.5, 0.5])
    assert(np.all(compute_death_rate_first_n_days(10, sample_cumulative, sample_death) == expected2))
    
    sample_cumulative2 = np.array([[1,2,3,4,8,8,10,10,10,10]])
    sample_death2 = np.array([[0,0,0,1,2,2,2,2,5,5]])
    
    expected3 = np.array([0.5])
    assert(compute_death_rate_first_n_days(10, sample_cumulative2, sample_death2) == expected3)
    expected4 = np.array([0.25])
    assert(compute_death_rate_first_n_days(5, sample_cumulative2, sample_death2) == expected4)

## Task 2.2: Computing Daily Increase in Cases

x = np.array([1, 2, 4, 7, 0])
np.diff(x) # array([1, 2, 3, -7])
np.diff(x, n=2) # array([1, 1, -10])

x = np.array([[1, 3, 6, 10], [0, 5, 6, 8]])
np.diff(x) # array([[2, 3, 4], [5, 1, 2]])
np.diff(x, axis=0) # array([[-1, 2, 0, -2]])

def compute_increase_in_cases(n, cases_cumulative):
    '''
    Computes the daily increase in confirmed cases for each country for the first n days, starting
    from the first day.
    Parameters
    ----------    
    n: int
        How many days of data to return in the final array. If the input data has fewer
        than n days of data then we just return whatever we have for each country up to n. 
    cases_cumulative: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the cumulative number of
        confirmed cases in that country, i.e. the ith row of `cases_cumulative`
        contains the data of the ith country, and the (i, j) entry of
        `cases_cumulative` is the cumulative number of confirmed cases on the
        (j + 1)th day in the ith country.
    
    Returns
    -------
    Daily increase in cases for each country as a 2D `ndarray` such that the (i, j)
    entry corresponds to the increase in confirmed cases in the ith country on
    the (j + 1)th day, where j is non-negative.
    Note
    ----
    The number of cases on the zeroth day is assumed to be 0, and we want to
    compute the daily increase in cases starting from the first day.
    Your implementation should not involve any iteration, including `map` and `filter`, 
    recursion, or any iterative approaches like for-loops.
    '''
    """ YOUR CODE HERE """
    c = cases_cumulative[:, :n]
    return np.diff(c, axis = 1, prepend = 0)
    """ YOUR CODE END HERE """

def test_task_2_2():
    cases_cumulative = np.zeros((100, 20))
    cases_cumulative[:, :] = np.arange(1, 21)
    actual = compute_increase_in_cases(100, cases_cumulative)
    assert(np.all(actual == np.ones((100, 20))))
    
    sample_cumulative = np.array([[1,2,3,4,8,8,10,10,10,10],[1,1,3,5,8,10,15,20,25,30]])
    expected = np.array([[1, 1, 1, 1, 4.], [1, 0, 2, 2, 3]])
    assert(np.all(compute_increase_in_cases(5,sample_cumulative) == expected))
    
    expected2 = np.array([[1, 1, 1, 1, 4, 0, 2, 0, 0, 0],[1, 0, 2, 2, 3, 2, 5, 5, 5, 5]])
    assert(np.all(compute_increase_in_cases(10,sample_cumulative) == expected2))
    assert(np.all(compute_increase_in_cases(20,sample_cumulative) == expected2))
    
    sample_cumulative2 = np.array([[51764, 51848, 52007, 52147, 52330, 52330],\
                                [55755, 56254, 56572, 57146, 57727, 58316],\
                                [97857, 98249, 98631, 98988, 99311, 99610]])
    expected3 = np.array([\
                [51764, 84, 159, 140, 183, 0],\
                [55755, 499, 318, 574, 581, 589],\
                [97857, 392, 382, 357, 323, 299]])
    assert(np.all(compute_increase_in_cases(6,sample_cumulative2) == expected3))

import numpy as np

a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(np.sum(a, axis=0))      # Prints [[ 6,  8],
                              #         [10, 12]]
print(np.sum(a, axis=1))      # Prints [[ 4,  6],
                              #         [12, 14]]
print(np.sum(a, axis=2))      # Prints [[ 3,  7],
                              #         [11, 15]]

## Task 2.3: Finding Maximum Daily Increase in Cases

a = np.arange(4).reshape((2,2)) # array([[0, 1], [2, 3]])
np.amax(a)  # 3 ->  Maximum of the flattened array
np.amax(a, axis=0)  # array([2, 3]) -> Maxima along the first axis (first column) 
np.amax(a, axis=1)  # array([1, 3]) -> Maxima along the second axis (second column)
np.amax(a, where=[False, True], initial=-1, axis=0) # array([-1,  3])
b = np.arange(5, dtype=float) # array([0., 1., 2., 3., 4.])
b[2] = np.nan  # array([ 0., 1., nan, 3., 4.])
np.amax(b) # nan

def find_max_increase_in_cases(n_cases_increase):
    '''
    Finds the maximum daily increase in confirmed cases for each country.
    Parameters
    ----------
    n_cases_increase: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the daily increase in the
        number of confirmed cases in that country, i.e. the ith row of 
        `n_cases_increase` contains the data of the ith country, and the (i, j) entry of
        `n_cases_increase` is the daily increase in the number of confirmed cases on the
        (j + 1)th day in the ith country.
    
    Returns
    -------
    Maximum daily increase in cases for each country as a 1D `ndarray` such that the
    ith entry corresponds to the increase in confirmed cases in the ith country as
    represented in `n_cases_increase`.
    Your implementation should not involve any iteration, including `map` and `filter`, 
    recursion, or any iterative approaches like for-loops.
    '''
    """ YOUR CODE HERE """
    return np.max(n_cases_increase, axis = 1)
    """ YOUR CODE END HERE """

def test_task_2_3():
    n_cases_increase = np.ones((100, 20))
    actual = find_max_increase_in_cases(n_cases_increase)
    expected = np.ones(100)
    assert(np.all(actual == expected))
    
    sample_increase = np.array([[1,2,3,4,8,8,10,10,10,10],[1,1,3,5,8,10,15,20,25,30]])
    expected2 = np.array([10, 30]) # max of [1,2,3,4,8,8,10,10,10,10] => 10, max of [1,1,3,5,8,10,15,20,25,30] => 30
    assert(np.all(find_max_increase_in_cases(sample_increase) == expected2))
    
    sample_increase2 = np.array([\
                [51764, 84, 159, 140, 183, 0],\
                [55755, 499, 318, 574, 581, 589],\
                [97857, 392, 382, 357, 323, 299]])
    expected3 = np.array([51764, 55755, 97857])
    assert(np.all(find_max_increase_in_cases(sample_increase2) == expected3))
    
    n_cases_increase2 = compute_increase_in_cases(cases_top_cumulative.shape[1], cases_top_cumulative)
    expected4 = np.array([ 68699.,  97894., 258110.])
    assert(np.all(find_max_increase_in_cases(n_cases_increase2) == expected4))

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[0, 1, 2]])
c = np.array([[0, 1, 2], [0, 1, 2]])
d = np.full((2, 3), 5)

print(a + b)                           # Prints [[1 3 5]
                                       #         [4 6 8]]
                                       # Equivalent to a + c
print(a + 5)                           # Prints [[ 6,  7,  8],
                                       #         [ 9, 10, 11]]
                                       # Equivalent to a + d

a = np.array([4, 5, 6])
print(a)                        # Prints [4, 5, 6]
b = np.array([1, 2])
print(b)                        # Prints [1, 2]
c = a[:, None] 
print(c)                        # Prints [[4]
                                #         [5]
                                #         [6]]
d = b[None, :]
print(d)                        # Prints [[1 2]]
e = c + d
print(e)                        # Prints [[5 6]
                                #         [6 7]
                                #         [7 8]]

c = a.reshape((3, 1)) + b
print(c) # Prints [[5 6]
         #         [6 7]
         #         [7 8]]

## Task 2.4: Computing Number of Purchaseable Masks

def compute_n_masks_purchaseable(healthcare_spending, mask_prices):
    '''
    Computes the total number of masks that each country can purchase if she
    spends all her emergency healthcare spending on masks.
    Parameters
    ----------
    healthcare_spending: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the emergency healthcare
        spending made by that country, i.e. the ith row of `healthcare_spending`
        contains the data of the ith country, and the (i, j) entry of
        `healthcare_spending` is the amount which the ith country spent on healthcare
        on (j + 1)th day.
    mask_prices: np.ndarray
        1D `ndarray` such that the jth entry represents the cost of 100 masks on the
        (j + 1)th day.
    
    Returns
    -------
    Total number of masks which each country can purchase as a 1D `ndarray` such
    that the ith entry corresponds to the total number of masks purchaseable by the
    ith country as represented in `healthcare_spending`.
    Note
    ----
    The masks can only be bought in batches of 100s.
    Your implementation should not involve any iteration, including `map` and `filter`, 
    recursion, or any iterative approaches like for-loops.
    '''
    """ YOUR CODE HERE """
    batches = np.floor(healthcare_spending / mask_prices)
    return np.sum(batches * 100, axis = 1)
    """ YOUR CODE END HERE """

def test_task_2_4():
    prices_constant = np.ones(5)
    healthcare_spending_constant = np.ones((7, 5))
    actual = compute_n_masks_purchaseable(healthcare_spending_constant, prices_constant)
    expected = np.ones(7) * 500
    assert(np.all(actual == expected))
    
    healthcare_spending1 = healthcare_spending[:3, :]  #Using data from CSV
    expected2 = [3068779300, 378333500, 6208321700]
    assert(np.all(compute_n_masks_purchaseable(healthcare_spending1, mask_prices)==expected2))
    
    healthcare_spending2 = np.array([[0, 100, 0], [100, 0, 200]])
    mask_prices2 = np.array([4, 3, 20])
    expected3 = np.array([3300, 3500])
    assert(np.all(compute_n_masks_purchaseable(healthcare_spending2, mask_prices2)==expected3))

a = np.array([[1,1],[1,2]]) # array([[1, 1], [1, 2]])
b = np.array([[1],[1]])  # array([[1], [1]])
c = a @ b
print(c) # Prints [[2]
         #         [3]]

## Task 2.5: Computing Stringency Index

def compute_stringency_index(stringency_values):
    '''
    Computes the daily stringency index for each country.
    Parameters
    ----------
    stringency_values: np.ndarray
        3D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the stringency values as a
        vector. To be specific, on each day, there are four different stringency
        values for 'school closing', 'workplace closing', 'stay at home requirements'
        and 'international travel controls', respectively. For instance, the (i, j, 0)
        entry represents the `school closing` stringency value for the ith country
        on the (j + 1)th day.
    
    Returns
    -------
    Daily stringency index for each country as a 2D `ndarray` such that the (i, j)
    entry corresponds to the stringency index in the ith country on the (j + 1)th
    day.
    In this case, we shall assume that 'stay at home requirements' is the most
    restrictive regulation among the other regulations, 'international travel
    controls' is more restrictive than 'school closing' and 'workplace closing',
    and 'school closing' and 'workplace closing' are equally restrictive. Thus,
    to compute the stringency index, we shall weigh each stringency value by 1,
    1, 3 and 2 for 'school closing', 'workplace closing', 'stay at home
    requirements' and 'international travel controls', respectively. Then, the 
    index for the ith country on the (j + 1)th day is given by
    `stringency_values[i, j, 0] + stringency_values[i, j, 1] +
    3 * stringency_values[i, j, 2] + 2 * stringency_values[i, j, 3]`.
    Note
    ----
    Use matrix operations and broadcasting to complete this question. Please do
    not use iterative approaches like for-loops.
    '''
    """ YOUR CODE HERE """
    raise NotImplementedError
    """ YOUR CODE END HERE """

def test_task_2_5():
    stringency_values = np.ones((10, 20, 4))
    stringency_values[:, 10:, :] *= 2
    actual = compute_stringency_index(stringency_values)
    expected = np.ones((10, 20)) * (1 + 1 + 3 + 2)
    expected[:, 10:] *= 2
    assert(np.all(actual == expected))
    
    stringency_values2 = np.array([[[0, 0, 0, 0], [1, 0, 0, 0]], [[0, 0, 0, 0], [0, 1, 2, 0]]])
    actual2 = compute_stringency_index(stringency_values2)
    expected2 = np.array([[0, 1], [0, 7]])
    assert(np.all(actual2 == expected2))

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[:, [0, 2]])                   # Prints [[1 3]
                                      #         [4 6]]
print(a[[1, 0], [1, 2]])              # Prints [5 3]

import numpy as np

a = np.array([4, 3, 1, 5, 10])
desired_indices = a > 3
print(a[desired_indices])        # Selects values in `a` that are
                                 # greater than 3; prints [ 4  5 10]

import matplotlib.pyplot as plt
import numpy as np

# Generate x values from -5 to 5
x = np.linspace(-5, 5, 400)

# Define two functions
y1 = x**2
y2 = np.sin(x)

# Create a new figure and axis
plt.figure(figsize=(8, 6))
plt.title('Plotting Two Functions')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Plot the first function in blue
plt.plot(x, y1, label='y = x^2', color='blue')

# Plot the second function in red
plt.plot(x, y2, label='y = sin(x)', color='red')

# Add a legend
plt.legend()

# Show the plot
plt.show()

## Task 2.6: Average Daily Increase in Cases

a = np.array([1, 2, 3, 4, 5, 6])
print(np.lib.stride_tricks.sliding_window_view(a, 3)) # Create a sliding window of length 3
'''
[[1, 2, 3],
 [2, 3, 4],
 [3, 4, 5],
 [4, 5, 6]]
'''

a[:2].fill(0) # Fill the first two elements of the array a with 0

print(a) # array([0, 0, 3, 4, 5, 6])

def average_increase_in_cases(n_cases_increase, n_adj_entries_avg=7):
    '''
    Averages the increase in cases for each day using data from the previous
    `n_adj_entries_avg` number of days and the next `n_adj_entries_avg` number
    of days.
    Parameters
    ----------
    n_cases_increase: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the daily increase in the
        number of confirmed cases in that country, i.e. the ith row of 
        `n_cases_increase` contains the data of the ith country, and the (i, j) entry of
        `n_cases_increase` is the daily increase in the number of confirmed cases on the
        (j + 1)th day in the ith country.
    n_adj_entries_avg: int
        Number of days from which data will be used to compute the average increase
        in cases. This should be a positive integer.
    
    Returns
    -------
    Mean increase in cases for each day, using data from the previous
    `n_adj_entries_avg` number of days and the next `n_adj_entries_avg` number
    of days, as a 2D `ndarray` such that the (i, j) entry represents the
    average increase in daily cases on the (j + 1)th day in the ith country,
    rounded down to the smallest integer.
    
    The average increase in cases for a particular country on the (j + 1)th day
    is given by the mean of the daily increase in cases over the interval
    [-`n_adj_entries_avg` + j, `n_adj_entries_avg` + j]. (Note: this interval
    includes the endpoints).
    Note
    ----
    Since this computation requires data from the previous `n_adj_entries_avg`
    number of days and the next `n_adj_entries_avg` number of days, it is not
    possible to compute the average for the first and last `n_adj_entries_avg`
    number of days. Therefore, set the average increase in cases for these days
    to `np.nan` for all countries.
    Your implementation should not involve any iteration, including `map` and `filter`, 
    recursion, or any iterative approaches like for-loops.
    '''
    """ YOUR CODE HERE """
    raise NotImplementedError
    """ YOUR CODE END HERE """

def test_task_2_6():
    n_cases_increase = np.array([[0, 5, 10, 15, 20, 25, 30]])
    actual = average_increase_in_cases(n_cases_increase, n_adj_entries_avg=2)
    expected = np.array([[np.nan, np.nan, 10, 15, 20, np.nan, np.nan]])
    assert(np.array_equal(actual, expected, equal_nan=True))

def visualise_increase(n_cases_increase, n_cases_increase_avg=None):
    '''
    Visualises the increase in cases for each country that is represented in
    `n_cases_increase`. If `n_cases_increase_avg` is passed into the
    function as well, visualisation will also be done for the average increase in
    cases for each country.

    NOTE: If more than 5 countries are represented, only the plots for the first 5
    countries will be shown.
    '''
    days = np.arange(1, n_cases_increase.shape[1] + 1)  # Our x axis will be "days"
    plt.figure() # Start a new graph
    for i in range(min(5, n_cases_increase.shape[0])):   # A curve for each row (country)
        plt.plot(days, n_cases_increase[i, :], label='country {}'.format(i))
    plt.legend()
    plt.title('Increase in Cases')

    if n_cases_increase_avg is None:
        plt.show()
        return
    
    plt.figure() # Start a new graph     
    for i in range(min(5, n_cases_increase_avg.shape[0])): # A curve for each row (country)
        plt.plot(days, n_cases_increase_avg[i, :], label='country {}'.format(i))
    plt.legend()
    plt.title('Average Increase in Cases')
    plt.show() # Show all graphs

n_cases_increase = np.array([[0, 2, 5, 3, 11, 9, 12, 1, 15, 30], [20, 12, 1, 7, 12, 9, 9, 28, 4, 16]])
visualise_increase(n_cases_increase, average_increase_in_cases(n_cases_increase, n_adj_entries_avg=2))

## Task 2.7: Finding Peaks in Daily Increase

import numpy as np

a = np.array([[0, 1, 7, 0], [3, 0, 2, 19]])
print(np.count_nonzero(a)) # 5

a = np.array([1, 2, np.nan])
print(np.isnan(a)) # [False, False, True]

a = np.array([[1, np.nan], [3, 5]])
print(np.nanmean(a)) # 3.0

def is_peak(n_cases_increase_avg, n_adj_entries_peak=7):
    '''
    Determines whether the (j + 1)th day was a day when the increase in cases
    peaked in the ith country.
    Parameters
    ----------
    n_cases_increase_avg: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the average daily increase in the
        number of confirmed cases in that country, i.e. the ith row of 
        `n_cases_increase` contains the data of the ith country, and the (i, j) entry of
        `n_cases_increase` is the average daily increase in the number of confirmed
        cases on the (j + 1)th day in the ith country. In this case, the 'average'
        is computed using the output from `average_increase_in_cases`.
    n_adj_entries_peak: int
        Number of days that determines the size of the window in which peaks are
        to be detected. 
    
    Returns
    -------
    2D `ndarray` with the (i, j) entry indicating whether there is a peak in the
    daily increase in cases on the (j + 1)th day in the ith country.
    Suppose `a` is the average daily increase in cases, with the (i, j) entry
    indicating the average increase in cases on the (j + 1)th day in the ith
    country. Moreover, let `n_adj_entries_peak` be denoted by `m`.
    In addition, an increase on the (j + 1)th day is deemed significant in the
    ith country if `a[i, j]` is greater than 10 percent of the mean of all
    average daily increases in the country.
    Now, to determine whether there is a peak on the (j + 1)th day in the ith
    country, check whether `a[i, j]` is maximum in {`a[i, j - m]`, `a[i, j - m + 1]`,
    ..., `a[i, j + m - 1]`, `a[i, j + m]`}. If it is and `a[i, j]` is significant,
    then there is a peak on the (j + 1)th day in the ith country; otherwise,
    there is no peak.
    Note
    ----
    Let d = `n_adj_entries_avg` + `n_adj_entries_peak`, where `n_adj_entries_avg`
    is that used to compute `n_cases_increase_avg`. Observe that it is not
    possible to detect a peak in the first and last d days, i.e. these days should
    not be peaks.
    
    As described in `average_increase_in_cases`, to compute the average daily
    increase, we need data from the previous and the next `n_adj_entries_avg`
    number of days. Hence, we won't have an average for these days, precluding
    the computation of peaks during the first and last `n_adj_entries_avg` days.
    Moreover, similar to `average_increase_in_cases`, we need the data over the
    interval [-`n_adj_entries_peak` + j, `n_adj_entries_peak` + j] to determine
    whether the (j + 1)th day is a peak.
    Hint: to determine `n_adj_entries_avg` from `n_cases_increase_avg`,
    `np.count_nonzero` and `np.isnan` may be helpful.

    Your implementation should not involve any iteration, including `map` and `filter`, 
    recursion, or any iterative approaches like for-loops.
    '''
    """ YOUR CODE HERE """
    raise NotImplementedError
    """ YOUR CODE END HERE """

def test_task_2_7():
    n_cases_increase_avg = np.array([[np.nan, np.nan, 10, 10, 5, 20, 7, np.nan, np.nan], [np.nan, np.nan, 15, 5, 16, 17, 17, np.nan, np.nan]])
    n_adj_entries_peak = 1
    
    actual = is_peak(n_cases_increase_avg, n_adj_entries_peak=n_adj_entries_peak)
    expected = np.array([[False, False, False, False, False, True, False, False, False],
                         [False, False, False, False, False, True, False, False, False]])
    assert np.all(actual == expected)
    
    n_cases_increase_avg2 = np.array([[np.nan, np.nan, 10, 20, 20, 20, 20, np.nan, np.nan], [np.nan, np.nan, 20, 20, 20, 20, 10, np.nan, np.nan]])
    n_adj_entries_peak2 = 1
    
    actual2 = is_peak(n_cases_increase_avg2, n_adj_entries_peak=n_adj_entries_peak2)
    expected2 = np.array([[False, False, False, True, False, False, False, False, False],
                        [False, False, False, False, False, False, False, False, False]])
    assert np.all(actual2 == expected2)
    
    n_cases_increase_avg3 = np.array([[np.nan, np.nan, 20, 20, 20, 20, 20, np.nan, np.nan],
                                    [np.nan, np.nan, 10, 10, 20, 20, 20, np.nan, np.nan]])
    n_adj_entries_peak3 = 2
    actual3 = is_peak(n_cases_increase_avg3, n_adj_entries_peak=n_adj_entries_peak3)
    expected3 = np.array([[False, False, False, False, False, False, False, False, False],
                        [False, False, False, False, True, False, False, False, False]])
    assert np.all(actual3 == expected3)
    
    n_cases_increase_avg4 = np.array([[np.nan, np.nan, 10, 20, 20, 20, 20, np.nan, np.nan],
                                    [np.nan, np.nan, 20, 10, 20, 20, 20, np.nan, np.nan]])
    n_adj_entries_peak4 = 2
    
    actual4 = is_peak(n_cases_increase_avg4, n_adj_entries_peak=n_adj_entries_peak4)
    expected4 = np.array([[False, False, False, False, False, False, False, False, False],
                        [False, False, False, False, False, False, False, False, False]])
    assert np.all(actual4 == expected4)
    
    
    n_cases_increase_avg5 = np.array([[np.nan, np.nan, 1, 4, 1, 97, 97, np.nan, np.nan]])
    n_adj_entries_peak5 = 1
    
    actual5 = is_peak(n_cases_increase_avg5, n_adj_entries_peak=n_adj_entries_peak5)
    expected5 = np.array([[False, False, False, False, False, True, False, False, False]])
    assert np.all(actual5 == expected5)

def visualise_peaks(n_cases_increase_avg, peaks):
    '''
    Visualises peaks for each of the country that is represented in
    `n_cases_increase_avg` according to variable `peaks`.
    
    NOTE: If there are more than 5 countries, only the plots for the first 5
    countries will be shown.
    '''
    days = np.arange(1, n_cases_increase_avg.shape[1] + 1) # Days will be our x-coordinates

    plt.figure() # Start a graph
    
    for i in range(min(5, n_cases_increase_avg.shape[0])): # A curve for each row (country) 
        plt.plot(days, n_cases_increase_avg[i, :], label='country {}'.format(i)) # Plot the daily increase curve
        peak = (np.nonzero(peaks[i, :]))[0]
        peak_days = peak + 1 # since data starts from day 1, not 0
        plt.scatter(peak_days, n_cases_increase_avg[i, peak]) # Scatterplot of peak(s) that lay on top of the curve
    
    plt.legend()
    plt.show() # Display graph

# Visualise the results on the test case
visualise_peaks(n_cases_increase_avg, is_peak(n_cases_increase_avg, n_adj_entries_peak=n_adj_entries_peak))


if __name__ == '__main__':
    test_task_1_1()
    test_task_1_2()
    test_task_1_3()
    test_task_1_4()
    test_task_2_1()
    test_task_2_2()
    test_task_2_3()
    test_task_2_4()
    test_task_2_5()
    test_task_2_6()
    test_task_2_7()

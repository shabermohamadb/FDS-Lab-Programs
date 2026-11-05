"""
EXPERIMENT 1
Title: INSTALL THE DATA ANALYSIS AND VISUALIZATION TOOL: PYTHON
       (NumPy, SciPy, and Pandas Exploration)
Aim:
  - 1A: To download, install and explore the features of NumPy package.
  - 1B: To download, install and explore the features of Scipy package.
  - 1C: To download, install and explore the features of Panda packages.
"""

# =============================================================================
# Sub-experiment 1A: NumPy Package Exploration
# =============================================================================
print("=" * 60)
print("EXPERIMENT 1A: NumPy Package Exploration")
print("=" * 60)

import numpy as np

# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

print("\nResult 1A: Thus, the NumPy package is downloaded, installed and the features are explored.\n")


# =============================================================================
# Sub-experiment 1B: SciPy Package Exploration
# =============================================================================
print("=" * 60)
print("EXPERIMENT 1B: SciPy Package Exploration")
print("=" * 60)

from scipy import special

a = special.exp10(3)
print("special.exp10(3) =", a)

b = special.exp2(3)
print("special.exp2(3)  =", b)

c = special.sindg(90)
print("special.sindg(90)=", c)

d = special.cosdg(45)
print("special.cosdg(45)=", d)

print("\nResult 1B: Thus, the SciPy package is downloaded, installed and the features are explored.\n")


# =============================================================================
# Sub-experiment 1C: Pandas Package Exploration (DataFrame & Series)
# =============================================================================
print("=" * 60)
print("EXPERIMENT 1C: Pandas Package Exploration")
print("=" * 60)

import pandas as pd

# Sample program - DataFrame creation
data = pd.DataFrame({
    "x1": ["y", "x", "y", "x", "x", "y"],
    "x2": range(16, 22),
    "x3": range(1, 7),
    "x4": ["a", "b", "c", "d", "e", "f"],
    "x5": range(30, 24, -1)
})
print("Sample DataFrame:")
print(data)

# Series to DataFrame creation
s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])
Data = {'first': s1, 'second': s2, 'third': s3}

dfseries = pd.DataFrame(Data)
print("\nDataFrame from Series:")
print(dfseries)

print("\nResult 1C: Thus, the Panda package is downloaded, installed and the features were explored.")

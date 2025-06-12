import numpy as np
import pandas as pd

# 1. Creating a DataFrame from a structured NumPy array (row and column labels)
data = np.array([['', 'Col1', 'Col2'],
                 ['Row1', 1, 2],
                 ['Row2', 3, 4]])
df1 = pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])
print("DataFrame from structured NumPy array:")
print(df1)
print("\n" + "-"*50 + "\n")

# 2. Creating a DataFrame from a 2D NumPy array
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
df2 = pd.DataFrame(my_2darray)
print("DataFrame from 2D NumPy array:")
print(df2)
print("\n" + "-"*50 + "\n")

# 3. Creating a DataFrame from a dictionary
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
df3 = pd.DataFrame(my_dict)
print("DataFrame from dictionary:")
print(df3)
print("\n" + "-"*50 + "\n")

# 4. Creating a DataFrame from a 1D list with custom column
my_df = pd.DataFrame(data=[4, 5, 6, 7], index=range(0, 4), columns=['A'])
print("DataFrame from list with column name:")
print(my_df)
print("\n" + "-"*50 + "\n")

# 5. Creating a DataFrame from a Series (countries and their capitals)
my_series = pd.Series({
    "UnitedKingdom": "London",
    "India": "NewDelhi",
    "United States": "Washington",
    "Belgium": "Brussels"
})
df5 = pd.DataFrame(my_series, columns=["Capital"])
print("DataFrame from Series:")
print(df5)
print("\n" + "-"*50 + "\n")

# 6. Creating a DataFrame and printing its shape and index length
df6 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
print("Shape of DataFrame df6:", df6.shape)
print("Number of rows (index):", len(df6.index))

# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
# + [Duplicate labels](#Duplicate-labels) 
# + [Topic 2 Title](#Topic-2-Title)

# # Duplicate labels
#
# **Xinyi Liu**
# **xyiliu@umich.edu**

import numpy as np
import pandas as pd

# * Some methods cannot be applied on the data series which have duplicate labels (such as `.reindex()`, it will cause error!),
# * Error message of using the function above: "cannot reindex from a duplicate axis".

series1 = pd.Series([0, 0, 0], index=["A", "B", "B"])
#series1.reindex(["A", "B", "C"]) 

# * When we slice the unique label, it returns a series,
# * when we slice the duplicate label, it will return a dataframe.

df1 = pd.DataFrame([[1,1,2,3],[1,1,2,3]], columns=["A","A","B","C"])
df1["B"]
df1["A"]

# * Check if the label of the row is unique by apply `index.is_unique ` to the dataframe, will return a boolean, either True or False.
# * Check if the column label is unique by `columns.is_unique`, will return a boolean, either True or False.

df1.index.is_unique
df1.columns.is_unique

# * When we moving forward of the data which have duplicated lables, to keep the data clean, we do not want to keep duplicate labels. 
# * In pandas version 1.2.0 (cannot work in older version), we can make it disallowing duplicate labels as we continue to construct dataframe by `.set_flags(allows_duplicate_labels=False)`
# * This function applies to both row and column labels for a DataFrame.

# +
#df1.set_flags(allows_duplicate_labels=False) 
## the method above cannot work on my end since my panda version is 1.0.5
# -

# Reference: https://pandas.pydata.org/docs/user_guide/duplicates.html

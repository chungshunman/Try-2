"""
Microeconometrics: Self Study.

Group Assignment:
    
Alec Eisenkolb, Chung-Shun Man, Nicolas Greber, Tim Hug

Spring Semester 2021.

University of St. Gallen.
"""

# import modules
import os
import numpy as np
import pandas as pd

# set working directory to current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# import own functions
import self_study_functions as ssf

# set the seep for replicability
np.random.seed(270421)

# define name of data
DATA = 'data_group_1.csv'

# load in the data
data = pd.read_csv(DATA)


# --------------------------------------------------------------------------- #

# Data Cleaning

# Testing


print('hello there')


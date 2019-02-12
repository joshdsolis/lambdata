#!/usr/bin/env python
""" lambdata - a Data Science Helper
"""
import numpy as np
import pandas as pd
import random

VERSION = 0
ONES = np.ones(100)
ONES_DF = pd.DataFrame(ONES)

def check_nulls(df):
	print(df.isnull().sum())



def more_rows(df,num):
	cols = []
	for n in range(1, num):
		for c in df.columns:
			cols.append(random.choice(df[c].unique()))
		df.loc[len(df.index)+n] = cols
		cols = []


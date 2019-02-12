#!/usr/bin/env python
""" lambdata - a Data Science Helper
"""
import numpy as np
import pandas as pd

VERSION = 0
ONES = np.ones(100)
ONES_DF = pd.DataFrame(ONES)

def check_nulls(df):
	print(df.isnull().sum())



def more_rows(df,num):
	cols = []
	for n in ramge(1, num):
		for c in df.column:
			cols.append(random.choice(df[c]))
		df.loc[len(df.index)+n] = cols


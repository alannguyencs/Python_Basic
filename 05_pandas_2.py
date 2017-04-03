import os
print (os.listdir())

import pandas

df1 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")
print (df1)
print (df1.shape)
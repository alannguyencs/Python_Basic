import pandas

df1 = pandas.DataFrame([[2,4,6], [10, 20, 30]])
print (df1)

df1 = pandas.DataFrame([[2,4,6], [10, 20, 30]], columns=["Price", "Age", "Value"])
print (df1)

df1 = pandas.DataFrame([[2,4,6], [10, 20, 30]], columns=["Price", "Age", "Value"], index = ["First", "Second"])
print (df1)

df2 = pandas.DataFrame([{"Name":"John", "Age":20}, {"Name":"Jack"}])
print (df2)

print (type(df1))
print (df1.mean())
print (df1.mean().mean())
print (df1.Price.mean())
print (df1.Price.max())
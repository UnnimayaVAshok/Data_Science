import pandas as pd

data = {
    "names":["akhil","meera","rahul","arun"],
    "age":[25,28,30,31],
    "dept":["it","hr","testing","hr"],
    "salary":[10000,20000,17000,25000]
}

result = pd.DataFrame(data)
print(result)

print(result.head())  # return the first few values from the dataframe
print(result.tail()) # return the last few values from the dataframe
print(result.shape)  
print(result.columns)
result.columns = ["Names","Age","Dept","Salary"] # update the column names
print(result)
result["place"] = ["kochi","tvm","allapey","chennai"]
print(result)
print(result.describe()) # returns the statistical summary of the dataframe
# columns contains the numerical values
print(result["place"])
print(result["Age"])
print(result.sort_values(by="Age"))
print(result.sort_values(by="Age",ascending=False))
print()
print(result.sample())
print(result.dtypes)
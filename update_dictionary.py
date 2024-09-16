my_dict = {"name": "Aasif", "age": 22, "country": "India"}
my_dict.update({"age": 25})
print(my_dict)

# merging two dictionaries

dic1={"apple":3,"banana":1}
dic2={"orange":2,"pear":4}

merged_dict={**dic1,**dic2}
print(merged_dict)
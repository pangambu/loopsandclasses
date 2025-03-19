mydict = {"name": "Max", "age": 28, "city": "New York", "email": "max@xyz.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")
print(mydict)


try:
    print(mydict["name"])
except:
    print("Error")



for key in mydict:
    print(f"(--{key}--)")  

for key in mydict.keys():
    print(f"(*--{key}--*)")

for value in mydict.values():
    print(f"{value}")

for key, value in mydict.items():
    print(f"{key} : {value}")



# copy a dictionary
mydict_cpy = dict(mydict)

#mydict_cpy["email"] = "max@xyz.com"

print(mydict_cpy)
print(mydict)

# merge two dictionaries
mydict.update(my_dict_2)
print(mydict)

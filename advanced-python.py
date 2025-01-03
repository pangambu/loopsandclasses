# Basic unpacking 
a,b,c = [1,2,3]
print(f"a: {a}, b: {b}, c: {c}\n")

# Extended iterable Unpacking with * operator
*a, b, c = [1,2,3,4,5]
print(f"a: {a}, b: {b}, c: {c}\n")

# Ignoring Values
a,b,_,c = [1,2,3,4]

# unpacking nested structures
data = ("Alice", (25, "Engineer"))
name, (age, profession) = data
print(f"name is {name}, age {age}, and my profession is {profession}")

# unpacking in fuction arguments
def print_names(*names):
    for name in names:
        print(name)

print_names("Alice", "Bob", "Charlie")


# Combining Lists with Unpacking
list1 = [1,2,3]
list2 = [4,5,6]
combined = [*list1, *list2]
print(f"Combined list: {combined}\n")

# Unpacking Dictionaries with ** operator
dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
combined_dict = {**dict1, **dict2}
print(f"Combined dictionary: {combined_dict}\n")

#Swapping variables
x = 10
y = 20
print(f"Before swap - x: {x}, y: {y}\n")

x, y = y, x
print(f"After swap - x: {x}, y: {y}\n")



def demonstrate_exec():
    code = """def greet(name):
    return f"Hello, {name}!\""""

    #Execute the code string
    local_scope = {}
    exec(code, {}, local_scope)
    print(local_scope["greet"]("Alice"))

demonstrate_exec()
numbers = [10,20,33,40,50,60,70,80]
result = 0
for num in numbers:
    result += num


print(result)

result = sum(numbers)
print(result)


for idx, val in enumerate(numbers, start=1):
    print(idx, val)


a =[1,2,3]
b = ["a","b","c"]
for val1, val2  in zip(a,b, strict=True):
    print(val1,val2)

print()

events = [("learn", 5), ("learn", 10), ("relaxed", 20)]

minutes_studied = 0 
for event in events:
    if event[0] == "learn":
        minutes_studied += event[1]
print(minutes_studied)


study_times = (event[1] for event in events if event[0]=="learn")
minutes_studied = sum(study_times)
print(minutes_studied)

for y in range(3):
    for x in range(1,10):
        print(x, end="")
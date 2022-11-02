ages = []
highs = []
for i in range(1, 6):
    print("%d Person" %i)
    age = int(input("Type your age: "))
    high = float(input("Type your High:"))
    ages.append(age)
    highs.append(high)

print("Inverse Order")
print("Highs")
print(highs[::-1])
print("Ages")
print(ages[::-1])

print("Normal order")
print("Highs")
print(highs)

print("Ages")
print(ages)

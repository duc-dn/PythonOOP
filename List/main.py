list1 = ["banana", "apple", "orange", 3, "Java", False]

print(list1[::3])

# for i in list1:
#     print(i, end=", ")

presidents = ["washington", "Adams", "Jefferson",
              "Madison", "Monroe", "Adams", "Jackson"]

for index, value in enumerate(presidents):
    print(f'Index: {index}, value: {value}')

for i in zip(list1, presidents):
    print(i)
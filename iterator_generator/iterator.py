# itera = [x for x in range(3)]
# print(itera)
# print(type(itera))

# taoj ra mot iterator
itera = (x for x in range(3))
print(itera)

# De lay ra cac phan tu trong iterator phai su dung next method
print(next(itera))
print(next(itera))
print(next(itera))

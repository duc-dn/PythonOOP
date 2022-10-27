# def square(lst):
#     sq_lst = []
#     for num in lst:
#         sq_lst.append(num ** 2)
#
#     return sq_lst
#
# kteam_ret = square([1,2,3])
# for value in kteam_ret:
#     print(value)

def square(lst):
    for num in lst:
        yield num ** 2

kteam_ret = square([1,2,3])
print(kteam_ret)
for value in kteam_ret:
    print(value)

for value in square([1,2,3,4]):
    print(value)
info = {"name": "duc", "age": 21, "handsome": True, "address": "Ha Nam"}

print(info)
# mac dinh in ra key
for d in info:
    print(d)

# cap nhat 1 gia tri bat ky thi dict thay doi
info["name"] = "hoai"
print(info)
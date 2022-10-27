try:
    x = 1 / 2
    print(x)
except Exception as e:
    print('error: ' + str(e))
else:
    print("khong co loi dau")
finally:
    print("Khong co loi, ngon roi")

# else duoc execute neu code block trong try laf dung
# finally duocj exec du co ngoaij le hay laf khong


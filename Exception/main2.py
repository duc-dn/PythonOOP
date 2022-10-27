try:
    x = 5
    b = 0
    print(x / b)
except TypeError:
    print("Unsupported opeation")
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print("Thanh cong")
finally:
    print("done")
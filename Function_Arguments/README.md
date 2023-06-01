## Tham số
***
- Có 2 loại tham số trong python:
    - Mặc định
    - Bắt buộc
  
```commandline
def print_name (name, greeting):
    print(f'{name}, {greeting}')
```
- name, greeting được gọi là tham số bắt buộc. Vì khi gọi lại hàm
print_name() bắt buộc phải truyền 2 tham số là `name` và `greeting`

```commandline
def print_name(name, greeting="Welcome cac ban"):
    print(f'{name}, {greeting}')
```
- `greeting` là tham số mặc định
***
## *arg, **kwargs
- `*args` và `**kwargs` đều chủ yếu được sử dụng trong định nghia hàm.
- Hai cú phám đặc biệt này giúp chúng ta có thể truyên bao nhiêu tham số vào hàm cũng được
***
### args
- VD:
```commandline
def foo(x, y):
    return x + y
foo(1, 2)
```
=> Hàm này hoạt động tốt nhưng sẽ gặp vấn đề khi muốn mở rộng. Nếu muốn tính tổng của nhiều số hơn, chúng ta phải định nghĩa
lại hàm với nhiều tham số hơn.
- Nhưng nếu muốn tính tổng của số có nhiều số nhưng số lượng không biết trước thì
cách này không còn phù hợp nữa
==> Sử dụng *args
```commandline
def foo(*args):
    result = 0
    for x in args:
        result += x
    return result
```
- Tất cả các tham số truyền vào sẽ là phần tử của args và chúng ta có thể duyệt qua nó như một `tuple` bình thường.
- Lưu ý rằng, `args` là một `tuple` chứ không phải `list`.
- Ngoài ra, chúng ta hoàn toàn có thể kết hợp *args với các tham số khác của hàm với ý nghĩa "những tham số còn lại". Trong trường hợp này, *args sẽ phải đặt ở cuối cùng nếu không sẽ gặp lỗi ngay.
```commandline
def foo(a, b, *args):
     print('normal arguments', a, b)
     for x in args:
         print('another argument through *args', x)
>>> foo(1, 2, 3, 4)
normal arguments 1 2
another argument through *args 3
another argument through *args 4
```
=> Nếu chúng ta biết chắc chắn một số lượng tham số nào đó, chúng ta có thể sử dụng tên tham số bình thường, 
và với các tham số còn lại chúng ta sẽ dùng `*args`
***
### kwargs
- Cách sử dụng **kwargs cũng tương tự như như *args, tuy nhiên, nó không dùng cho các tham số thông thường truyền vào lần lượt, mà nó được sử dụng cho các tham số đặt tên 
(thuật ngữ chính xác là named arguments hoặc keyword arguments).
- VD1:
```commandline
>>> def foo(**kwargs):
...     for key, value in kwargs.items():
...         print(key, value)
...
>>> foo(a=1, b=2)
a 1
b 2
```
- VD2:
```
def test(*args, **kwargs):
    for i in args:
        print(i, end="\n")
    for key, val in kwargs.items():
        print(f"key: {key}, val: {val}")

test(1,2,3,4,5,a="Duc",b=1)
result:
1
2
3
4
5
key: a, val: Duc
key: b, val: 1
```
***
## Unpack (giải nén)
- `*`và `**`

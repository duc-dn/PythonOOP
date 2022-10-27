# Generator
***
- Iterable thuận tiên cho lưu trữ và truy xuât thông tin, do đó phải lưu trữ thông
tin trong các vùng nhớ máy tính 
=> Sẽ có trường hợp không cần lưu trữ thông tin đó vì nó qua nhiều 
=> Từ đó sinh ra gennerator
***
- Gennerator là iterator (là 1 dạng của iterable) nhưng khác ở chỗ không thể tái sử dụng
- => Vì nó không lưu trữ các giá trị trong bộ nhớ mà nó sinh ra lần lượt
***
## So sánh yield và return
- Cả yield và return đều trả lại một vài giá trị cho hàm
### Return
- Return trả về một object, và kết thúc một hàm, hàm sẽ dừng lại hoàn toàn
- VD với return
```commandline
def square(lst):
    sq_lst = []
    for num in lst:
        sq_lst.append(num ** 2)

    return sq_lst

kteam_ret = square([1,2,3])
for value in kteam_ret:
    print(value)
```
- Kết quả
``1 4 9``
- Đối với return nó sẽ trả về 1 list và lưu nó trong bộ nhớ để có thể tái sử dụng
### Yield
- VD với yield
```commandline
def square(lst):
    for num in lst:
        yield num ** 2

kteam_ret = square([1,2,3])
for value in kteam_ret:
    print(value)
```
- Yield sẽ tạm dừng function,  lưu tất cả các trạng thái của hàm (các biến local và trang thái của hàm) và sau đó tiếp tục từ
trạng thái đó với các lệnh gọi kế tiếp

## Iterable
***
- Là một đối tượng cho phép duyet qua các phần tử của nó với vòng lặp for
- Là một object có phương thức __iter__ trả về một iterator hoặc là một phương
thức __getitem__ cho phép lấy bất cứ phần  tử nào bằng indexing. VD: str, lis, tuple
- Có thể được hiểu như là một danh sách với mỗi phần tử trong Iterable là 
- VD: List, tuple, ... 

## Iterator
***
- Các đối tượng iterable đều trả về một đối tượng iterator khi đưa chúng vào phương 
thức iter() trong python
- Là một đối tượng cho phép ta lấy từng giá trị một của nó (không truy cập index bất kỳ để lấy, khác so với list
và tuple)
- Sử dụng hàn next để lấy từng giá trị một. Sẽ có lỗi StopIteration
---
VD: n = 1000000
```
def square_generator(n):
    for i in range(1, n+1):
        yield i**2

def square_sum_return(n):
    squares = [i**2 for i in range(1, n+1)]
    return sum(squares)

generator = square_generator(1000000)
print(type(generator))
print("sum: {}".format(sum(generator)))
```
#### Square_sum_return(n):
  - Ham nay se luu lai toan bo 1 trieu gia tri trong list squares
  - Sau do, dung ham sum de tinh tong toan bo list squares
  - return sum(squares) de ket thuc ham
=> Lang phi tai nguyen

#### square_generator(n)
- Khac voi return, generator dung den dau thi tinh den do
- Dung yeild de tra ra 1 generator va yeild se luu lai trang thai tai thoi diem do
  phuc vu cho lan tiep theo.
- Bien generator sẽ trả về một generator object chứa các giá trị từ 1 đến 1 triệu. Khi chúng ta gọi hàm square_generator(1000000) và gán kết quả cho biến generator, nó không thực thi ngay lập tức. Thay vào đó, nó trả về một generator object.
```
generator = square_generator(1000000)
print(next(generator))  # Output: 1
print(next(generator))  # Output: 4
print(next(generator))  # Output: 9
# ...
print(next(generator))  # Output: 999996001
print(next(generator))  # Output: 999998001
print(next(generator))  # Output: 1000000000
```
- Các giá trị trong generator object sẽ được tạo ra và trả về dựa trên vòng lặp trong hàm square_generator(). Mỗi lần lặp, giá trị mới sẽ được tính toán bằng cách bình phương giá trị i từ 1 đến 1 triệu và được trả về bằng câu lệnh yield. Khi chúng ta lặp qua generator object, các giá trị này sẽ được tạo ra dần dần khi cần thiết, tiết kiệm bộ nhớ.
- Khi chúng ta gọi hàm sum(generator) trên một generator object, nó sẽ gọi phương thức __next__() của generator để tính toán dần dần từng giá trị một và cộng dồn chúng lại.
- Hàm sum() trong Python được thiết kế để làm việc với các iterable object, bao gồm cả generator object. Khi chúng ta gọi sum(generator), nó sẽ tự động lặp qua generator object và lấy từng giá trị bằng cách gọi phương thức __next__() cho đến khi generator object không còn giá trị nào hoặc gặp lỗi StopIteration.
- Note:
  - câu lệnh yield i**2 trong hàm square_generator() không trả về một generator object. Thay vào đó, nó trả về các giá trị bình phương dần dần khi được yêu cầu.

  - Khi chúng ta gọi hàm square_generator(1000000) và lặp qua generator object, mỗi lần gọi yield i**2, giá trị bình phương tương ứng của i sẽ được trả về và luồng thực thi sẽ tạm dừng. Generator object không phải là kết quả trực tiếp của câu lệnh yield, mà chỉ là một cơ chế để tạo ra và quản lý việc trả về các giá trị từ hàm generator.
  => Tom lai no tra ve 1 gia tri
---
#### Vai tro cua yield
- Từ khóa yield được sử dụng trong hàm square_generator() để tạo ra một generator object và trả về các giá trị bình phương từ 1 đến n.

- Khi chúng ta gọi hàm square_generator(1000000) và lặp qua generator object, mỗi lần gọi yield, luồng thực thi sẽ tạm dừng và giá trị bình phương tương ứng sẽ được trả về. Sau đó, khi chúng ta tiếp tục lặp qua generator object, luồng thực thi sẽ tiếp tục từ điểm tạm dừng trước đó và tính toán giá trị bình phương tiếp theo.

- Sự khác biệt quan trọng ở đây là yield cho phép hàm square_generator() trả về giá trị bình phương dần dần mà không cần tính toán và lưu trữ toàn bộ danh sách bình phương. Thay vào đó, generator object sẽ tạo ra giá trị khi cần thiết và chỉ lưu trữ trạng thái hiện tại của luồng thực thi.

- Khi chúng ta sử dụng hàm sum(generator) để tính tổng, nó sẽ sử dụng từng giá trị từ generator object một cách tuần tự bằng cách gọi phương thức __next__() của generator. Do đó, việc sử dụng yield trong hàm square_generator() cho phép tính toán và trả về các giá trị bình phương dần dần khi được yêu cầu, tiết kiệm tài nguyên và hỗ trợ tính toán cho các dãy số lớn.
---
#### Su khac nhau giua yield va return
- Trong Python, yield và return là hai cách khác nhau để trả về giá trị và điều khiển luồng thực thi của một hàm. Dưới đây là sự khác nhau chính giữa hai từ khóa này:

- `yield`:
  - yield được sử dụng trong các hàm sinh giá trị (generator functions) và tạo ra một đối tượng generator.
  - Khi một hàm có từ khóa yield, nó trở thành một generator function. Khi gọi hàm, nó không thực thi ngay lập tức, mà trả về một generator object.
  - Generator object có thể được lặp qua (iterable) để nhận các giá trị mà hàm yield đã trả về.
  -Khi gặp từ khóa yield trong generator function, luồng thực thi tạm dừng và giá trị được trả về. Khi generator object được lặp qua tiếp, luồng thực thi tiếp tục từ điểm tạm dừng đó.
  - Generator object tiếp tục tạo và trả về giá trị trong mỗi lần lặp cho đến khi hàm kết thúc hoặc gặp từ khóa return.
- `return`:
  - return được sử dụng để trả về giá trị từ một hàm thông thường.
  - Khi gặp từ khóa return, giá trị được trả về và luồng thực thi của hàm kết thúc. Hàm không tiếp tục thực thi các câu lệnh sau dòng return.
  - Khi gọi một hàm và nhận giá trị được trả về, luồng thực thi chuyển đến nơi gọi hàm và tiếp tục thực thi từ đó.
  - Tóm lại, yield và return đều được sử dụng để trả về giá trị từ một hàm. yield được sử dụng trong generator function để tạo ra một generator object và cho phép luồng thực thi tạm dừng và tiếp tục. Trong khi đó, return trả về giá trị và kết thúc luồng thực thi của hàm.
## Iterable
***
- Là một đối tượng cho phép duyejt qua các phần tử của nó với vòng lặp for
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
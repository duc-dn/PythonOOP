## Async trong Python
---
#### Originary code (Lap trinh tuan tu)
- cong viec 1: 3s
- cong viec 2: 5s
- cong viec 3: 7s
```
Thuc hien tuan tu, cv1 xong thi den cv2, xong cv2 thi den cv3

------
      ----------
                --------------

------------------------------ Tong thoi gian thuc hien

```
---
#### Thread/MultiThreading
```
Chay dong thoi, khi cv1 chay thi cv2 cung gan nhu ngay lap tuc chay, cv3 tuong tu nhu vay  

Thread mo nhieu luong, mot luong cho 1 worker lam
- worker1 lam tren luong 1
- worker2 lam tren luong 2
- worker3 lam tren luong 3

Thread 1    ------
Thread 2      ----------
Thread 3     --------------

            --------------- Tong thoi gian chay

```
#### Async
```
Trong khi cv1 chay chua chay xong thi no goi cv2 lam
Cv 2 chua xong thi co the goi cv3 de chay

Async chi chay tren 1 Thread

a Thread
------
  ----------
   --------------
```
=> Async nhanh hon thread va muti thread vi thread/multi thread can tao ra nhieu thread de chay task trong khi async chi can 1 thread de chay

VD: co 10 task, thi thread/multi thread can mo 10 thread de thuc hien cac task. Trong khi do, async chi chay tren 1 thread va 1 core CPU
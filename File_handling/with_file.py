## Dung with open() de write file ma khong can quan tam den viec dong file
with open("test1.txt", "a", encoding="utf-8") as f:
    f.write("Xin chao tat ca moi nguoi\n")
    f.writelines("Hello\n")
    f.writelines("Chao 500 anh em\n")
    f.write("hahaha\n")
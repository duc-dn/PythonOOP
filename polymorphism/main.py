# Tinh da hinh: các đối tượng có thể có các phương thức (hành động) giông nhau
# nhưng mục đích của các cái hành động đó có thể khác nhau tùy vào từng tình huống khác nhau

class Vietnam(object):
    def language(self):
        print("Language: Vietnamese")

class Japan(object):
    def language(self):
        print("Language: Japanese")

def aboutContry(obj):
    obj.language()

vn = Vietnam()
jp = Japan()

aboutContry(vn)
aboutContry(jp)

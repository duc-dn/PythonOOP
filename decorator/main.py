def show_text(info):
    return 'This is a first information: {}'.format(info)


# x = show_text
# print(x('Duc'))

# Van de dat ra muon them 1 vaof dau This is ... mot vai chu ma khong can viet lai ham
# ===========================================================================

def decor_func(func):
    def wrapper(info):
        return "Phan them vao ham: {}".format(func(info))
    return wrapper

x = decor_func(show_text)

print(x('Duc'))

# =============== Viet ngan gon ==========================
@decor_func
def show_info(info="Duc"):
    return 'This is a first information: {}'.format(info)

print(show_info('Duc'))
# warrper
def a_new_decorator(a_func):
    
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def function_exe():
    print("I am execting a_function()")

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()


# ==========================================================================================
# cách viết @a_new_decorator là cách viết tắt thay cho: 
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to")

a_function_requiring_decoration()


# function decorator la mot wrapper cua mot function co san. 
# Decorator wrap mot function va thay doi cach hoat dong cua no


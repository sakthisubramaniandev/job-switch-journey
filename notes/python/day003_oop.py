
#decorator: a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
def logger(func):
    def wrapper(*args, **kargs):
        print(f"Function {func.__name__} is starting...")
        result = func(*args, **kargs)
        print(f"Function {func.__name__} is done!!")
        return result
    return wrapper

@logger
def sub(a,b):
    return a - b

@logger
def mul(a,b):
    return a * b


#

def even_numbers():
    a = 0
    while True:
        yield a
        a += 2
even_no = even_numbers()

for _ in range(5):
    print(next(even_no))
    

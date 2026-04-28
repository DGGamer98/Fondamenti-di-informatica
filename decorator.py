def decorator(function):
    def wrapper(*args, **kwargs):
        print("Prima")
        result = function(*args, **kwargs)
        print("Dopo")
        return result
    return wrapper

@decorator
def ciao():
    print("Ciao")

ciao()
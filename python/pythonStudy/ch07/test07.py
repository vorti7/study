def outer(x) :
    def inner(y) :
        return x+y
    print(inner)
    return inner

inner = outer(5)
print(inner(3))

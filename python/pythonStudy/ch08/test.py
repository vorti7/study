# def key_args(x,y,z,*args) :
#     local = locals()
#     # varnames = key_args.__code__.co_varnames
#     # x = local[varnames[0]]
#     # y = local[varnames[1]]
#     # z = local[varnames[2]]
#     # print(type(x))
#     print(type(y))
#     print(local)
#     return y
#
#
# print(key_args(1,z = 2,y=1,12))


# def var_pos_args_(*args, x) :
#     print(type(args))
#     print(locals())
#
#
# print(var_pos_args_(1,2,3,4,5,x=6))


# def  var_key_args(**kwargs) :
#     print(type(kwargs),kwargs)
#     for k,v in kwargs.items() :
#         print("key ", k, "value ", v)
#     vSum = 0
#     for v in kwargs.values() :
#         vSum += v
#     print(vSum)
#
# print(var_key_args())
# print(var_key_args(a=1,b=2,c=3))


# def var_pos_key_args(*args, **kwargs) :
#     print(type(args),args)
#     print(type(kwargs),kwargs)
#     result = 0
#     for v in args :
#         result += v
#     for v in kwargs.values() :
#         result += v
#     return result
#
#
# print(var_pos_key_args(1,2,3,4, a=1, b=3, c=5))


# def all_args(x,y,*args,z,**kwargs):
#     print(locals())
#
# all_args(1,2,3,4,5,z=6,a=7,b=8)



# def key_args(x,y,*,z):
#     print(locals())
# print(key_args(10,10,z=10))

# def add(x,y,z):
#     print(locals())
#     return x+y+z
#
# t=(1,2,3)
# print(add(*t))
# s="str"
# print(add(*s))
# l=[1,2,3]
# print(add(*l))


# def add(*args) :
#     print(locals())
#     if isinstance(locals()["args"][0], str) :
#         result = ""
#     else :
#         result = 0
#     for i in args :
#         result += i
#     return result
#
# t=(1,2,3)
# print(add(*t))
# s="str"
# print(add(*s))
# l=[1,2,3]
# print(add(*l))


# def mul(x,y,z) :
#     print(locals())
#     return x*y*z
#
# d = {'x':1,'y':2,'z':3}
# # print(**d)
# print(mul(**d))

# def mul(**kwargs) :
#     print(locals())
#     result = 1
#     for i in kwargs.values():
#         result *= i
#     return result
#
# d = {'a':1,'b':2,'c':3}
# print(mul(**d))



def rtn_tuple(a,b,c):
    print(locals())
    return a,b,c
def rtn_list(*args):
    print(locals())
    return list(args)
def rtn_str(*args):
    print(locals())
    return "".join(args)


a,*b = rtn_tuple(1,2,3)
print(a,b)

a,*b = rtn_list(*[1,2,3])
print(a,b)

a,*b = rtn_str(*"str")
print(a,b)

def rtn_dict(**kwargs) :
    print(locals())
    return kwargs
a,*b = rtn_dict(a=1,b=2,c=3)
print(a,b)

# print(type(rtn_tuple(1,2,3)))
# print(rtn_tuple(1,2,3))
# print(type(atuple))
# print(atuple)

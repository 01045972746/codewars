import operator, math
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }

def zero(*args): #your code here
    if not args:
        return 0
    else:
        oper, other = args[0]
        return startOperation(0, oper, other)
    pass
def one(*args): #your code here
    if not args:
        return 1
    else:
        oper, other = args[0]
        return startOperation(1, oper, other)
    pass
def two(*args): #your code here
    if not args:
        return 2
    else:
        oper, other = args[0]
        return startOperation(2, oper, other)
    pass
def three(*args): #your code here
    if not args:
        return 3
    else:
        oper, other = args[0]
        return startOperation(3, oper, other)
    pass
def four(*args): #your code here
    if not args:
        return 4
    else:
        oper, other = args[0]
        return startOperation(4, oper, other)
    pass
def five(*args): #your code here
    if not args:
        return 5
    else:
        oper, other = args[0]
        return startOperation(5, oper, other)
def six(*args): #your code here
    if not args:
        return 6
    else:
        oper, other = args[0]
        return startOperation(6, oper, other)
    pass
def seven(*args): #your code here
    if not args:
        return 7
    else:
        oper, other = args[0]
        return startOperation(7, oper, other)
    pass
def eight(*args): #your code here
    if not args:
        return 8
    else:
        oper, other = args[0]
        return startOperation(8, oper, other)
    pass
def nine(*args): #your code here
    if not args:
        return 9
    else:
        oper, other = args[0]
        return startOperation(9, oper, other)
    pass

def plus(add): #your code here
    return "+", add
def minus(subtract): #your code here
    return "-", subtract
def times(multiple): #your code here
    return "*", multiple
def divided_by(divide): #your code here
    return "/", divide


def startOperation(a, oper, b):
    return math.floor(ops[oper](a, b))


# Clever
'''
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y
'''

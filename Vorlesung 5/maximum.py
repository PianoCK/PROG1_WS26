def maximum(a: int, b: int, c: int) -> int:
    '''Diese Funktion gibt das Maximum von den Parametern a, b und c zurück.'''
    if a >= b and a >=c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

m = maximum()
m = maximum(3.5,9.1,5.3)
print(m)
m = maximum(9,3,5)
print(m)
m = maximum(3,5,9)
print(m)
m = maximum(-3, -2, -8)
print(m)
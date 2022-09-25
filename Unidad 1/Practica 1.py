def producto(*n):
    producto = 1
    for number in n:
        producto = producto * number
    return producto

x = producto(1,2,3)
print(x)
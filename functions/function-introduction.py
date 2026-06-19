def multiply(x,y):
    """
    tha values of x and y will multiply
    :param x: put the x value here
    :param y: put the y value here
    :return: the multiple of x and y will be return
    """
    result = x * y
    return result

forty_two = multiply(6,7)
print(forty_two)
twenty = multiply(5,4)
print(twenty)

for i in range(1,5):
    result = multiply(2,i)
    print(result)

help(multiply)

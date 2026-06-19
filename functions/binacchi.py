def binacchi(n: int) -> int:
    if 0<= n <=1:
        return n
    first_value , second_value = 0,1
    result = None
    for f in range(n-1):
        result = first_value + second_value
        first_value = second_value
        second_value = result

    return result

for i in range(10):
    print(i, binacchi(i))

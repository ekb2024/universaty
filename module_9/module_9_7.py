def is_prime(fun):
    def wrapper(*args):
        sum = fun(*args)
        if sum % 2 == 0:
            result  = "Составное"
        else:
            result  = "Простое"
        return result
    return wrapper

@is_prime
def sum_three(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

result = sum_three(2, 3, 6)
print(result)

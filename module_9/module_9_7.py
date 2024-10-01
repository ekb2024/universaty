def is_prime(fun):
    def wrapper(*args):
        sum = 0
        result = fun(*args)
        for i in result:
             sum += i
        if sum % 2 == 0:
              return "Составное"
        else:
              return "Простое"
    return wrapper

@is_prime
def sum_three(*args):
    return args

result = sum_three(2, 3, 6)
print(result)
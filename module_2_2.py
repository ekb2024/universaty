first =  input('введите первое число :')
second = input('введите второе число :')
third =  input('введите третье число :')

if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')
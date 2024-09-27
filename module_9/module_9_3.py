first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

firs_result = (len(i[0])-len(i[1]) for i in zip(first,second) if len(i[0])!=len(i[1]))
second_result = ( len(first[i])==len(second[i]) for i in range(len(first)) )

print(list(firs_result))
print(list(second_result))


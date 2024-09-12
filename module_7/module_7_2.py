def custom_write(file_name,string):
    string_position = {}
    file = open(file_name,'w',encoding='utf-8')
    n_str = 0
    for i in string:
      n_str += 1
      string_position.update({(n_str,file.tell()):i})
      file.write(i+'\n')
    file.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
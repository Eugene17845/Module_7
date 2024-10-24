def custom_write(file_name, *strings):
    strings_positions = {}
    n = 0

    for i in strings[0]:
        file = open(file_name, 'a',encoding='utf-8')
        tell = (file.tell())
        file.write(f'{i}\n')
        n += 1
        file.close()
        strings_positions.update({(n, tell): i})
    return strings_positions




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
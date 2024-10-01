def custom_write(file_name, strings):
    string_position = {}

    with open(file_name, 'w', encoding='utf-8') as f:
        for index, string in enumerate(strings, start=1):
            byte_pos = f.tell()
            f.write(string + '\n')
            string_position[(index, byte_pos)] = string

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

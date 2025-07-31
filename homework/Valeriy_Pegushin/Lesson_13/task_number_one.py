import os


base_path = os.path.dirname(__file__)
# file_path = f'{base_path}/data.txt'
file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'data2.txt')
print(file_path)


def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        data_line = data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)

homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_okulik_file_path)


with open(eugene_okulik_file_path) as eugene_okulik_file:
    print(eugene_okulik_file.read())





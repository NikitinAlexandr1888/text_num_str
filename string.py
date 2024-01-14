def count_string(file_name):
  try:
    file = open(file_name, encoding='utf-8')
    string = file.readlines()
    return(len(string))
  except FileNotFoundError:
    print("File not found")
  finally:
    file.close()


file_dict = {}
for file_name in file_dict:
  file_dict[file_name] = count_string(file_name)
sorted_files = sorted(file_dict)

for file_name in sorted_files:
  with open(file_name) as f:
    lines = f.readlines()
  with open('txtfile.txt', 'a', encoding='utf-8') as f_all:
    print(f'{file_name} \n {len(lines)} \n {lines}', file=f_all)
# не понимаю мочему не вносятся запись в файл txtfile.txt


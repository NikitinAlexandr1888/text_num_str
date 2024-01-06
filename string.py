def count_string(file_name):
  try:
    file = open(file_name, encoding='utf-8')
    string = file.readlines()
    print(len(string))
  except FileNotFoundError:
    print("File not found")
  finally:
    file.close()

    file_dict = {}
    for file_name in file_list:
        file_dict[file_name] = count_string(file_name)
    return sorted(file_dict)


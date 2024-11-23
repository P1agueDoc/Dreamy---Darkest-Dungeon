import os
from Level_gen import *
def write_edit_save(path_to_save, save_name, row):
    save_path = os.path.join(path_to_save, save_name + '.txt')
    if not os.path.exists(path_to_save):
        os.mkdir(save_path)

    with open(save_path, 'w', encoding = 'utf-8') as file:
        file.write(row)

a1 = str(input("enter name of save"))
row = Map(16,16)
row1 = row.map_gen()
write_edit_save('./Saves', a1, row1)
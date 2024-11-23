import os

class save_file():
    def __init__(self, level_grid, character_data, name_of_save, row):
        self.level_grid = level_grid
        self.character_data = character_data
        self.name_of_save = name_of_save
        self.path_to_save = "./Saves"
        self.row = row

    def write_edit_save_first(self, row):
        save_path = os.path.join(self.path_to_save, self.name_of_save + '.txt')
        if not os.path.exists(self.path_to_save):
            os.mkdir(self.path_to_save)

        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(self.row)

a1 = save_file
a1.write_edit_save_first()
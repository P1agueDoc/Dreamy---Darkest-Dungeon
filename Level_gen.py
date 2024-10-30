import random


class Map:
    safe = "🌫 " #:fog:
    danger = "🔥 "

    def __init__(self, height, length):
        self.height = height
        self.length = length
        self.level_row_data = "\n"

    def map_gen(self):
        for i in range(1, self.height + 1):
            for b in range(1, self.length + 1):
                level_id = random.randint(0, 1)
                if level_id == 0:
                    self.level_row_data += str(self.safe)
                elif level_id == 1:
                    self.level_row_data += str(self.danger)
            self.level_row_data += "\n"
        return self.level_row_data
import random


class Map:
    safe = "🌫 " #:fog:
    danger = "🔥 "
    trap_room ="❄️ "
    random_stuff = "🎲 "
    trader_room ="🧮 "
    no_way = "🏔 "

    def __init__(self, height, length):
        self.height = height
        self.length = length
        self.level_row_data = "\n"

    def map_gen(self):
        for i in range(1, self.height + 1):
            for b in range(1, self.length + 1):
                level_id = random.randint(0, 4)
                if level_id == 0:
                    self.level_row_data += str(self.safe)
                elif level_id == 1:
                    self.level_row_data += str(self.danger)
                elif level_id == 2:
                    self.level_row_data += str(self.trap_room)
                elif level_id == 3:
                    self.level_row_data += str(self.random_stuff)
                elif level_id == 4:
                    a = random.randint(0, 2)
                    if a == 0:
                        self.level_row_data += str(self.trader_room)
                    else:
                        self.level_row_data += str(self.no_way)

            self.level_row_data += "\n"
        return self.level_row_data
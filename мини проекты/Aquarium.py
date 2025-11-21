class Aquarium():
    def __init__(self):
        # длина
        self.length = 40
        # ширина
        self.width = 20
        # высота
        self.height = 20
        # список декоративных элементов
        self.decor = [("камни",1), ("деревце",4)]
    def get_total_volume(self):
        self.aquariumr_volume = (self.length * self.width * self.height) / 1000
        return self.aquariumr_volume
    def get_water_volume(self):
        self.get_total_volume()
        self.waters_volume = self.aquariumr_volume - 5
        return self.waters_volume
    def  calculate_food(self, fish_count, food_per_liter):
        self.food_per_liter = food_per_liter
        self.food_count = fish_count
        fish_count = 2
        food_per_liter = 4
        self.get_water_volume()
        food = self.food_per_liter * self.food_count * self.get_water_volume()

    def show_info(self):
        print(self.length, self.width, self.height, self.decor, self.get_total_volume(), self.get_water_volume())

if __name__ == '__main__':
    aquarium = Aquarium()
    aquarium.show_info()
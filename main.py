class Warehouse:
    translations = {
        'beef': 'говядины, ',
        'pork': 'свинины, ',
        'mutton': 'баранины, '
    }

    beef = 0
    pork = 0
    mutton = 0

    def add_meat(self, meat, weight):
        print('Приняли: ', self.translations[meat], 'вес: ', weight)
        old_weight = self.get_meat(meat)
        new_weight = old_weight + weight
        setattr(self, meat, new_weight)
        self.print_remains(meat)

    def remove_meat(self, meat, weight):
        print('Отпустили: ', self.translations[meat], 'вес: ', weight)
        old_weight = self.get_meat(meat)
        new_weight = old_weight - weight
        setattr(self, meat, new_weight)
        self.print_remains(meat)

    def get_meat(self, meat):
        return getattr(self, meat)

    def print_remains(self, meat):
        print('Остатки', self.translations[meat], self.get_meat(meat))



my_sklad = Warehouse()
my_sklad.add_meat('beef', 100)
my_sklad.add_meat('pork', 230)
my_sklad.add_meat('mutton', 10)
my_sklad.add_meat('mutton', 35)
my_sklad.remove_meat('pork', 33)





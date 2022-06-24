# samostatne promenne (bez struktur)
vojak_x = 10
vojak_y = 15
print(vojak_x, vojak_y)

# tuple (neda se menit)
vojak = (10, 15)
print(vojak[0], vojak[1])

# seznam
vojak = [10, 15]
print(vojak[0], vojak[1])

# slovnik
vojak = {'x': 10, 'y': 15}
print(vojak['x'], vojak['y'])

# trida a objekty
class Vojak:
    def __init__(self, x, y):
        self.x = x
        self.y = y

vojak = Vojak(10, 15)
print(vojak.x, vojak.y)
